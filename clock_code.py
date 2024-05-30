import datetime

def show_time():
    now = datetime.datetime.now()
    time_str = now.strftime("%H:%M:%S")
    print("Current time:",time_str)

show_time()