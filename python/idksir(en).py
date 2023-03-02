#author:mcagabe19

import time
import logging

try:
    name = input("Please Type Your Name : ")
    print('Welcome', name)
    print('This Code Will Close After 3 Seconds...')
    time.sleep(3)

except:
    logging.exception("An exception was thrown!")
    print('This Code Will Close After 3 Seconds...')
    time.sleep(3)
