#author:mcagabe19

import time
import logging

try:
    isim = input("Adınızı Giriniz : ")
    print('Hoşgeldiniz', isim)
    print('This Code Will Close After 3 Seconds...')
    time.sleep(3)

except:
    logging.exception("An exception was thrown!")
    print('This Code Will Close After 3 Seconds...')
    time.sleep(3)
