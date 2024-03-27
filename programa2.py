#mensaje de whats
import pywhatkit
import pyautogui

try:
    #pywhatkit.sendwhatsmsg("+524446390477", "ola bola", 18,12)
    pywhatkit.sendwhatmsg_to_group("HMSd7sLfFPy4ivP0YtAqvE", "a", 19,8)
    pyautogui.press('enter')
    print("Mensaje enviado")
except:
    print("Error")