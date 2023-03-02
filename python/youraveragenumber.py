#author:mcagabe19

import time
import logging

try:
    number1 = int(input("Number 1 : "))
    number2 = int(input("Number 2 : "))
    number3 = int(input("Number 3 : "))
    number4 = int(input("Number 4 : "))
    total = number1 + number2 + number3 + number4 / 4
    print('Your Number Is : ', total)
    print('This Code Will Close After 3 Seconds...')
    time.sleep(3)

except:
    logging.exception("An exception was thrown!")
    print('This Code Will Close After 3 Seconds...')
    time.sleep(3)
