import schedule
import time
from IndusDC import clean_data
    
schedule.every(6).hours.do(clean_data) #runs every 6 hours

while(1):
    schedule.run_pending()
    time.sleep(1)