#author:mcagabe19

import time
import logging

try:
    kenar = int(input("Karenin Kenarı : "))
    cevre = kenar * 4
    alan = kenar * kenar
    print("Karenin Çevresi :", cevre, "\nKarenin Alanı :", alan);
    print('This Code Will Close After 3 Seconds...')
    time.sleep(3)

except:
    logging.exception("An exception was thrown!")
    print('This Code Will Close After 3 Seconds...')
    time.sleep(3)
