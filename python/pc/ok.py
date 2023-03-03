#author:mcagabe19

import time
import logging

try:
    vize = int(input("Vize Puanı : ")) * 0.30
    final = int(input("Final Puanı : ")) * 0.70
    toplam = vize + final
    print("Toplam Notunuz :", toplam)
    print('This Code Will Close After 3 Seconds...')
    time.sleep(3)

except:
    logging.exception("An exception was thrown!")
    print('This Code Will Close After 3 Seconds...')
    time.sleep(3)
