import os
import time 
from plyer import notification

while True:
    print("1. Switch off the computer \n 2. Sleep Mode \n 3. Water Reminder \n 4. Tablet Reminder ")
    user_input=int(input("Enter which operation want to perform :-  "))
    print(user_input)
    if user_input==1:
        print("Switch off the computer")
        def shutDown():
            if os.name=='nt':
                os.system('shutdown /s /t 2')
        shutDown()
        
    elif user_input==2:
        print("Sleep Mode")
        print("Going to sleep for 20 seconds...")
        

        def sleep_laptop(duration):
            print(f"Laptop will sleep for {duration} seconds.")
            time.sleep(duration)
            print("Laptop waking up now...")
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

        def main():
            try:
                input_time = int(input("Enter the time in seconds for laptop to sleep: "))
                sleep_laptop(input_time)
            except ValueError:
                print("Please enter a valid integer for time.")

        if __name__ == "__main__":
            main()


            
    elif user_input==3:
        print("Water Reminder")
        notification.notify(
            title="drink water ",
            message="Experts recommend that males consume 15.5 cups (3.7 liters) of water daily and females 11.5 cups (2.7 liters). But environmental factors such as temperature and other health conditions may affect your water needs.",
            app_icon="C:\\Users\\marot\\Desktop\\Desktop notifier App\\waterGlassIcon.ico",
            timeout=10,
            
        )
        time.sleep(60 * 240)
        

    elif user_input==4:
        print("Tablet Reminder")
        notification.notify(
            title="Take Your Tablet now",
            message="Firstly Eat Food then take tablet. For your illness this is best to take the tablet at suitable time. If you dont take the tablet then your illness may be increase or it affect on your health Totally.",
            app_icon="C:\\Users\\marot\\Desktop\\Desktop notifier App\\tablet.ico",
            timeout=14,
        )
        time.sleep(60 * 360)
    else:
        print("invalid entered1")
