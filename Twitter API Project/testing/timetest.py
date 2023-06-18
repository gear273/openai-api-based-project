import schedule
import time


def your_function():
    print("this function is working")
    return


# Schedule the function to run at 6 AM every day
schedule.every().day.at("17:48").do(your_function)

while True:
    schedule.run_pending()
    time.sleep(60)
