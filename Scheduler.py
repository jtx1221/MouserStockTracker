from time import time
import schedule
import time
from Script import testscript

schedule.every(1).minute.do(testscript)

while 1:
    schedule.run_pending()
    time.sleep(1)