#!/usr/bin/env python
# -*- coding: utf-8 -*-
import schedule
import time
from datetime import datetime

def job():
    print(time.time())


# schedule.every().minutes.do(job)
# schedule.every().hour.do(job)
# schedule.every().day.at("22:17").do(job)
schedule.every(3).seconds.do(job)


while 1:
    schedule.run_pending()
    time.sleep(1)
    

# To clear all functions   
# schedule.clear()