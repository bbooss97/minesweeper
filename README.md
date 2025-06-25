# Minesweeper Auto-Clicker

Un sistema automatico per giocare a Minesweeper Online che rileva e clicca automaticamente sui numeri rivelati nel gioco.

## 📋 Descrizione

Questo progetto consiste in tre script Python che lavorano insieme per automatizzare parte del gameplay di Minesweeper Online:

- **Color Picker**: Tool per identificare i colori dei numeri nel gioco
- **Minesweeper Clicker**: Script principale che rileva e clicca sui numeri
- **Hotkey Listener**: Sistema di tasti rapidi per controllare l'automazione

## 🚀 Caratteristiche

- ✅ Rilevamento automatico della finestra di Minesweeper Online
- ✅ Identificazione dei numeri tramite riconoscimento colori
- ✅ Click automatico sui numeri rilevati
- ✅ Sistema di tasti rapidi per controllo rapido
- ✅ Configurazione personalizzabile dei colori
- ✅ Debug visivo con screenshot

## 📦 Requisiti

### Dipendenze Python
```
pyautogui
pygetwindow
opencv-python (cv2)
numpy
keyboard
```

### Installazione delle dipendenze
```bash
pip install pyautogui pygetwindow opencv-python numpy keyboard
```

## 🎮 Come utilizzare

### 1. Configurazione iniziale

Prima di utilizzare il clicker, è necessario configurare i colori dei numeri:

1. Apri Minesweeper Online nel tuo browser
2. Esegui il color picker:
   ```bash
   python color_picker.py
   ```
3. Segui le istruzioni per catturare i colori dei numeri
4. I valori BGR verranno mostrati nel terminale mentre muovi il mouse
5. Aggiorna il file `colors.json` con i nuovi valori se necessario

### 2. Utilizzo del clicker manuale

Esegui lo script principale:
```bash
python minesweeper_clicker.py
```

Lo script:
- Troverà automaticamente la finestra di Minesweeper Online
- Catturerà uno screenshot del gioco
- Rileverà i numeri basandosi sui colori configurati
- Cliccherà automaticamente su tutti i numeri trovati

### 3. Utilizzo con tasti rapidi

**⚠️ Richiede privilegi di amministratore**

Esegui il listener come amministratore:
```bash
python hotkey_listener.py
```

Tasti rapidi disponibili:
- **Q**: Avvia il clicker automatico
- **W**: Chiude il listener

## 📁 Struttura del progetto

```
minesweeper/
├── color_picker.py          # Tool per identificare i colori
├── minesweeper_clicker.py   # Script principale del clicker
├── hotkey_listener.py       # Sistema di tasti rapidi
├── colors.json              # Configurazione colori dei numeri
├── debug_screenshot.png     # Screenshot di debug (generato automaticamente)
└── README.md               # Questo file
```

## ⚙️ Configurazione

### colors.json

Il file `colors.json` contiene i valori BGR per ogni numero:

```json
{
  "1_blue": [221, 164, 102],
  "2_green": [80, 160, 80],
  "3_red": [119, 102, 204],
  "4_dark_blue": [221, 119, 187],
  "5_maroon": [0, 153, 170],
  "6_cyan": [128, 128, 0]
}
```

### Parametri modificabili

Nel file `minesweeper_clicker.py`:
- `color_tolerance = 10`: Tolleranza per il riconoscimento colori
- `y_offset = 110`: Offset per la barra del titolo del browser

## 🔧 Troubleshooting

### Problemi comuni

1. **Finestra non trovata**
   - Assicurati che Minesweeper Online sia aperto nel browser
   - Il titolo della finestra deve contenere "Minesweeper Online"

2. **Numeri non rilevati**
   - Usa `color_picker.py` per aggiornare i colori in `colors.json`
   - Verifica che la tolleranza colore sia appropriata
   - Controlla il file `debug_screenshot.png` per verificare la cattura

3. **Tasti rapidi non funzionano**
   - Esegui `hotkey_listener.py` come amministratore
   - Su Windows: tasto destro → "Esegui come amministratore"

4. **Click imprecisi**
   - Verifica che l'offset Y sia corretto per il tuo browser
   - Assicurati che la finestra del gioco sia completamente visibile

## 🎯 Utilizzo consigliato

1. Apri Minesweeper Online
2. Inizia una partita e rivela alcuni numeri manualmente
3. Esegui il clicker per automatizzare i click sui numeri visibili
4. Continua alternando azioni manuali e automatiche

## ⚠️ Note importanti

- Questo tool è pensato per scopo educativo e di automazione personale
- L'utilizzo su siti web potrebbe violare i termini di servizio
- Usa responsabilmente e rispetta le policy del sito
- Testato su Windows con browser standard

## 🤝 Contribuire

Per contribuire al progetto:
1. Fai un fork del repository
2. Crea un branch per le tue modifiche
3. Testa le modifiche
4. Invia una pull request

## 📄 Licenza

Questo progetto è distribuito sotto licenza MIT. Vedi il file LICENSE per i dettagli.

---

**Buon divertimento con Minesweeper! 💣🎮**
