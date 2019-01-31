from django_cron import CronJobBase, Schedule
import requests


class ParseNews(CronJobBase):
    RUN_EVERY_MINS = 3

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'meowapi.parse_news'

    def do(self):
        print('scheduled')