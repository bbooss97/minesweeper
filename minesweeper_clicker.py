
import pyautogui
import pygetwindow as gw
import cv2
import numpy as np
import time
import json
import os

# --- Funzioni di supporto ---

def find_game_window():
    try:
        game_windows = [w for w in gw.getAllWindows() if 'Minesweeper Online' in w.title]
        if not game_windows:
            print("Finestra del gioco non trovata.")
            return None
        return game_windows[0]
    except Exception as e:
        print(f"Errore nel trovare la finestra: {e}")
        return None

def load_colors(file_path='colors.json'):
    if not os.path.exists(file_path):
        print(f"Errore: File di configurazione '{file_path}' non trovato.")
        return None
    with open(file_path, 'r') as f:
        print(f"Caricamento colori da '{file_path}'...")
        return json.load(f)

def capture_game_screen(window):
    if not window:
        return None, 0
    try:
        window.activate()
        time.sleep(0.2)
    except Exception:
        window.maximize()
        time.sleep(0.5)
        window.activate()

    x, y, width, height = window.left, window.top, window.width, window.height
    y_offset = 110  # Offset per barra del titolo e indirizzi

    region = (x, y + y_offset, width, height - y_offset)
    screenshot = pyautogui.screenshot(region=region)
    img = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    
    cv2.imwrite("debug_screenshot.png", img)
    print("Screenshot di debug salvato come 'debug_screenshot.png'.")
    
    return img, y_offset

# --- Funzione Principale ---

def click_revealed_numbers():
    # Imposta la pausa di PyAutoGUI a zero per la massima velocità
    pyautogui.PAUSE = 0

    colors = load_colors()
    if not colors:
        return

    game_window = find_game_window()
    if not game_window:
        return

    screen, y_offset = capture_game_screen(game_window)
    if screen is None:
        print("Impossibile catturare la schermata del gioco.")
        return

    click_points = []
    color_tolerance = 10 # Tolleranza per leggere il colore

    for color_name, bgr_value in colors.items():
        target_color = np.array(bgr_value, dtype=np.uint8)
        lower_bound = np.array([max(0, c - color_tolerance) for c in bgr_value])
        upper_bound = np.array([min(255, c + color_tolerance) for c in bgr_value])
        
        mask = cv2.inRange(screen, lower_bound, upper_bound)
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for c in contours:
            # Filtra i contorni troppo piccoli per essere numeri reali
            if cv2.contourArea(c) > 2:
                M = cv2.moments(c)
                if M["m00"] > 0:
                    cx = int(M["m10"] / M["m00"])
                    cy = int(M["m01"] / M["m00"])
                    click_points.append((game_window.left + cx, game_window.top + y_offset + cy))

    if not click_points:
        print("Nessun numero trovato da cliccare. Prova ad aggiornare i valori in 'colors.json' usando 'color_picker.py'.")
        return

    print(f"Trovati {len(click_points)} punti validi. Cliccando...")
    unique_points = sorted(list(set(click_points)), key=lambda p: (p[1], p[0]))

    for point in unique_points:
        pyautogui.click(point[0], point[1])

    print("Finito.")

def main():
    click_revealed_numbers()

if __name__ == "__main__":
    main()
