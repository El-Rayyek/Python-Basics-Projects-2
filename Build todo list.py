'''
task :
Build todo list that reminds with with tasks in certain times , show the tasks as
desktop notification
'''

from win10toast import ToastNotifier
import schedule
import time
import datetime


toast = ToastNotifier()

def reading_time():
    toast.show_toast(
        "Reading Time",
        "Hello , It's Reading missoin",
        icon_path=None,
        duration=10,
        threaded=False
    )
def watching_time():
    toast.show_toast(
        "Watching Time",
        "Hello , It's watching missoin",
        icon_path=None,
        duration=10,
        threaded=False
    )   
def phone_time():
    toast.show_toast(
        "Phone Time",
        "Hello , It's phone missoin",
        icon_path=None,
        duration=10,
        threaded=False
    )
def praying_time():
    toast.show_toast(
        "Praying Time",
        "Hello , It's praying missoin",
        icon_path=None,
        duration=10,
        threaded=False
    )

schedule.every().day.at("22:03").do(reading_time)
schedule.every().day.at("22:04").do(watching_time)
schedule.every().day.at("22:06").do(phone_time)
schedule.every().day.at("22:07").do(praying_time)
while True:
    schedule.run_pending()
    time.sleep(2)







