# ClashOfClans-AutoAttackingBot
> ⚠️ **Disclaimer**  
> Using bots in Clash of Clans may violate the game's Terms of Service and can result in account bans.  
> Use this project **at your own risk**.  
> This software is intended **only for proof-of-concept and educational purposes**.

---

## 📖 Description
This project implements a simple bot that automates attacks in *Clash of Clans* using the **pyautogui** library to simulate keyboard and mouse input.  
It is **not guaranteed** to bypass anti-bot checks or work with all game versions.

---

## ⚙️ Requirements
- **Python 3.8+**
- **pyautogui**

---

## 🚀 Installation and Running

1. **Create and activate a virtual environment**
   ```bash
   # Create the virtual environment
   python -m venv cocvenv

   #activate it:
   # Windows (PowerShell)
   .\cocvenv\Scripts\Activate.ps1
   # Windows (cmd)
   .\cocvenv\Scripts\activate.bat
   # Linux / macOS
   source cocvenv/bin/activate

   #and then
   pip install pyautogui

2. Edit the main bot file to adjust settings:
   ```bash
   INFINITE_ATTACKS = False   # True for infinite attacks
   NUM_ATTACKS = 20           # Number of attacks if INFINITE_ATTACKS = False
   ```
3. ###Running the Bot:
   ```bash
   python bot.py
   ```
