import pyautogui
import pytesseract
import time
import random

INFINITE_ATTACKS = False
NUM_ATTACKS = 20
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\feder\Desktop\venvClash\Tesseract-OCR\tesseract.exe'


def check_and_skip():

    while True:    
        text = __ocr_from_screen(178,140,290,220)
        print(text)

        lines = []
        for riga in text.splitlines():
            lines.append(riga)
        try:
            if len(lines[0])>7 or len(lines[1])>7:
                break
        except (ValueError, IndexError):
            pass
        try:
            if int(lines[0][0])>7 or int(lines[1][0])>7:
                break
        except (ValueError, IndexError):
            pass
        pyautogui.click(1700,800)
        time.sleep(5)

    return 0

def __ocr_from_screen(x1,y1,x2,y2):
    # 1. Cattura lo screenshot dell'intera schermata (o una regione specifica)
    # Per una regione specifica: pyautogui.screenshot(region=(x, y, larghezza, altezza))
    screenshot = pyautogui.screenshot(region=(x1, y1, x2-x1, y2-y1))
    
    # 2. Esegui l'OCR sull'immagine dello screenshot
    text = pytesseract.image_to_string(screenshot)
    
    return text

def start_atk():
    pyautogui.click(200, 900)
    time.sleep(1)
    pyautogui.click(300, 700)
    return 0

def atk():
    #zoom-out
    for _ in range (5):
        pyautogui.scroll(-100)

    #piazza i golin intorno al villaggio attaccato
    pyautogui.click(400, 900)

    pyautogui.click(500,500)#clack al centro per i villaggi con l'animazione

    for i in range (20):
        pyautogui.click(270+i*20 +random.randint(-4, 4) , 500+i*16+random.randint(-4, 4))
        time.sleep(random.uniform(0, 0.2))
    
    for i in range (25):
        pyautogui.click(300+i*22+random.randint(-4, 4), 470-i*16+random.randint(-4, 4))
        time.sleep(random.uniform(0, 0.2))

    for i in range (20):
        pyautogui.click(1700-i*20+random.randint(-4, 4), 470+i*20+random.randint(-4, 4))
        time.sleep(random.uniform(0, 0.2))
    
    for i in range (25):
        pyautogui.click(1700-i*22+random.randint(-4, 4), 370-i*14+random.randint(-4, 4))
        time.sleep(random.uniform(0, 0.2))
    
    for i in range (25):
        pyautogui.click(1650-i*22+random.randint(-4, 4), 380-i*14+random.randint(-4, 4))
        time.sleep(random.uniform(0, 0.2))

    return 0

def end_atk():
    pyautogui.click(200, 820)
    time.sleep(0.5)
    pyautogui.click(1100, 650)
    time.sleep(0.5)
    pyautogui.click(1000, 900)
    return 0

if __name__ == "__main__":
    #time.sleep(4)
    count = 0
    while INFINITE_ATTACKS or count < NUM_ATTACKS:

        time.sleep(4)
        start_atk()
        time.sleep(5)
        check_and_skip()
        atk()
        time.sleep(10)
        end_atk()

        cont+=1


