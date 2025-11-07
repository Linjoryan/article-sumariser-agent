from apscheduler.schedulers.blocking import BlockingScheduler
from main import run_daily
from config.settings import os

sched = BlockingScheduler()
DELIVERY_TIME = os.getenv('DELIVERY_TIME', '07:00')
hour, minute = map(int, DELIVERY_TIME.split(':'))

@sched.scheduled_job('cron', hour=hour, minute=minute)
def scheduled_run():
    print('Scheduled run triggered')
    run_daily()

if __name__ == '__main__':
    print('Starting scheduler...')
    sched.start()
