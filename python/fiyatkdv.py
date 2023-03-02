#author:mcagabe19

import time
import logging

try:
    fiyat = int(input("Fiyatı Giriniz : "))
    kdvlifiyat = fiyat * 0.18
    print("KDV'li Fiyat :", kdvlifiyat)
    print('This Code Will Close After 3 Seconds...')
    time.sleep(3)

except:
    logging.exception("An exception was thrown!")
    print('This Code Will Close After 3 Seconds...')
    time.sleep(3)
