import time

for seconds in range(10):
    current_time = time.strftime('%H:%M:%S')
    print(current_time)
    time.sleep(1)