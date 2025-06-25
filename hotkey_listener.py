

import keyboard
import time
import os
import sys
from minesweeper_clicker import click_revealed_numbers # Importa la funzione che abbiamo già creato

# --- Funzioni per i tasti rapidi ---

def run_clicker():
    print(f"[{time.strftime('%H:%M:%S')}] Tasto 'q' premuto. Avvio dello script di click...")
    try:
        click_revealed_numbers()
        print(f"[{time.strftime('%H:%M:%S')}] Script completato. In attesa di nuovi input...")
    except Exception as e:
        print(f"Si è verificato un errore durante l'esecuzione dello script: {e}")

def quit_listener():
    print("Tasto 'w' premuto. Chiusura del listener in corso...")
    # Uscita forzata dallo script. È il modo più affidabile per terminare.
    sys.exit(0)

# --- Programma Principale ---

def main():
    # Nasconde la finestra del terminale se eseguito come processo in background
    # Nota: questo potrebbe non funzionare su tutti i sistemi
    # import ctypes
    # ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

    print("--- Listener di Tasti Rapidi per Minesweeper Attivo ---")
    print("   - Premi 'q' per avviare il clicker.")
    print("   - Premi 'w' per chiudere questo listener.")
    print("------------------------------------------------------")

    # Associa le funzioni ai tasti
    keyboard.add_hotkey('q', run_clicker, suppress=True)
    keyboard.add_hotkey('w', quit_listener, suppress=True)

    # Mantiene lo script in esecuzione fino a quando non viene chiamato quit_listener
    keyboard.wait()

    print("Listener terminato.")

if __name__ == "__main__":
    # Controlla se lo script è eseguito con privilegi di amministratore
    # La libreria 'keyboard' ne ha bisogno per funzionare correttamente
    try:
        is_admin = os.getuid() == 0
    except AttributeError:
        is_admin = os.path.exists('C:\\Windows\\System32\\config\\system') # Un modo per verificarlo su Windows

    if not is_admin:
        print("\nAttenzione: Questo script richiede privilegi di amministratore per intercettare i tasti.")
        print("Per favore, esegui questo script da un terminale (CMD o PowerShell) aperto come Amministratore.")
        time.sleep(5)
        sys.exit(1)

    main()

