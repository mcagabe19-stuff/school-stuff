#author:mcagabe19

import time
import logging

try:
    # your code
    print('This Code Will Close After 3 Seconds...')
    time.sleep(3)

except:
    logging.exception("An exception was thrown!")
    print('This Code Will Close After 3 Seconds...')
    time.sleep(3)
