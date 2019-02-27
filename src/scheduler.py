import schedule
import time
import job

INTERVAL_IN_SECONDS = 30

def run_for_n_seconds(n):
    schedule.every(n).seconds.do(job.run)
    t = 0
    while t < n:
        schedule.run_pending()
        time.sleep(1)
        t += 1
    return t


# This is the default if run from command line
# like: python scheduler.py
# this will run whatever code is placed 
# in job.run() once every second
schedule.every(INTERVAL_IN_SECONDS).seconds.do(job.run)
print('running job every %s seconds...' % (INTERVAL_IN_SECONDS))
# schedule.every().hour.do(job.run)
# schedule.every().day.at("22:17").do(job.run)


if __name__ == "__main__":
    while 1:
        schedule.run_pending()
        time.sleep(1)





# To clear all functions
# schedule.clear()
