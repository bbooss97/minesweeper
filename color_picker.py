import pyautogui
import pygetwindow as gw
import cv2
import numpy as np
import time
import os

# Funzione per trovare la finestra del gioco
def find_game_window():
    try:
        game_windows = [w for w in gw.getAllWindows() if 'Minesweeper Online' in w.title]
        if not game_windows:
            return None
        return game_windows[0]
    except Exception:
        return None

# Funzione per catturare la schermata del gioco
def capture_game_screen(window):
    if window:
        try:
            window.activate()
            time.sleep(0.2)
        except Exception:
            window.maximize()
            time.sleep(0.5)
            window.activate()

        x, y, width, height = window.left, window.top, window.width, window.height
        y_offset = 110  # Approssimazione per barra del titolo e indirizzi
        
        screenshot = pyautogui.screenshot(region=(x, y + y_offset, width, height - y_offset))
        return cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    return None

if __name__ == "__main__":
    print("Avvio del Color Picker...")
    game_window = find_game_window()

    if not game_window:
        print("Finestra di Minesweeper non trovata. Esecuzione interrotta.")
    else:
        print("Finestra trovata. Cattura dello schermo in corso...")
        screen = capture_game_screen(game_window)

        if screen is not None:
            print("\n*** Istruzioni ***")
            print("1. Apri la finestra del terminale e quella del gioco fianco a fianco.")
            print("2. Muovi il mouse sopra i numeri nel gioco.")
            print("3. Annota i valori BGR (Blu, Verde, Rosso) che appaiono nel terminale.")
            print("4. Premi CTRL+C nel terminale per uscire.")
            print("-" * 20)

            y_offset = 110 # Deve corrispondere a quello in capture_game_screen

            try:
                while True:
                    # Ottieni la posizione attuale del mouse
                    mx, my = pyautogui.position()

                    # Converte le coordinate dello schermo in coordinate della finestra di gioco
                    win_x = mx - game_window.left
                    win_y = my - game_window.top - y_offset

                    # Controlla se il cursore è all'interno dell'area catturata
                    if 0 <= win_x < screen.shape[1] and 0 <= win_y < screen.shape[0]:
                        # Ottieni il colore BGR del pixel
                        color = screen[win_y, win_x]
                        # Stampa il valore in modo che si aggiorni sulla stessa linea
                        print(f"Pos: ({win_x}, {win_y}) -> Colore BGR: {color}      ", end='\r')
                    else:
                        print("Mouse fuori dall'area di gioco...      ", end='\r')

                    time.sleep(0.1)
            except KeyboardInterrupt:
                print("\n\nUscita dal programma.")
