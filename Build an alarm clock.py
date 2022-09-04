'''
task :
Build an alarm clock. build an alarm clock for yourself , you can set multiple
alarms , the alarm should show desktop notification
'''
from win10toast import ToastNotifier
import time
import schedule



toaster = ToastNotifier()
def wake_up():
    toaster.show_toast(
        "it's 20:37 O'Clock",
        'wake up',
        icon_path=None,
        duration=10,
        threaded=False)
def study():
    toaster.show_toast(
         "it's 20:40 O'Clock",
        'study',
        icon_path=None,
        duration=10,
        threaded=False)
def playing_football():
    toaster.show_toast(
         "it's 20:42 O'Clock",
        'playing football',
        icon_path=None,
        duration=10,
        threaded=False)
def running():
    toaster.show_toast(
         "it's 20:45 O'Clock",
        'running',
        icon_path=None,
        duration=10,
        threaded=False)
def social_meeting():
    toaster.show_toast(
         "it's 20:46 O'Clock",
        'social meeting',
        icon_path=None,
        duration=10,
        threaded=False)
def Nile_Trip():
    toaster.show_toast(
         "it's 20:48 O'Clock",
        'Nile trip',
        icon_path=None,
        duration=10,
        threaded=False)
def sun_view():
    toaster.show_toast(
         "it's 20:50 O'Clock",
        'sun view',
        icon_path=None,
        duration=10,
        threaded=False)

schedule.every().day.at("20:37").do(wake_up)
schedule.every().day.at("20:40").do(study)
schedule.every().day.at("20:42").do(playing_football)
schedule.every().day.at("20:45").do(running)
schedule.every().day.at("20:46").do(social_meeting)
schedule.every().day.at("20:48").do(Nile_Trip)
schedule.every().day.at("20:50").do(sun_view)
while True:
    schedule.run_pending()
    time.sleep(5)



