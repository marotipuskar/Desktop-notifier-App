# from tkinter import *
# from tkinter import ttk

# # Function definition
# def my_function():
#     print("Hello from a function")
#     user_input = int(input("Enter which operation want to perform :-  "))
#     if user_input == 1:
#         print("Switch off the computer")
#     elif user_input == 2:
#         print("Sleep Mode")
#     elif user_input == 3:
#         print("Water Reminder")
#     elif user_input == 4:
#         print("Tablet Reminder")
#     else:
#         print("Invalid entry")

# win = Tk()
# win.title("Desktop Notifier App window")
# label = Label(win, text="Welcome To Desktop Notifier App ", font=('Helvetica 17 bold'))
# label.pack()

# # Button to trigger the function
# button = Button(win, text="Perform Operation", command=my_function)
# button.pack()

# win.mainloop()
import os
import time 
import subprocess
from plyer import notification

def my_function():


    while True:
        print("1. Switch off the computer \n 2. Sleep Mode \n 3. Water Reminder \n 4. Tablet Reminder \n 5. ALl Bills Reminder")
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


            def sleep_mode(duration):
                print(f"Putting computer to sleep for {duration} seconds...")
                time.sleep(duration)
                # Put computer to sleep
                subprocess.run("shutdown /h /f")

            def main():
                try:
                    duration = int(input("Enter sleep duration in seconds: "))
                    sleep_mode(duration)
                except ValueError:
                    print("Please enter a valid number for duration.")

            if __name__ == "__main__":
                main()
            
            

            # def sleep_laptop(duration):
            #     print(f"Laptop will sleep for {duration} seconds.")
            #     time.sleep(duration)
            #     print("Laptop waking up now...")
            #     os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

            # def main():
            #     try:
            #         input_time = int(input("Enter the time in seconds for laptop to sleep: "))
            #         sleep_laptop(input_time)
            #     except ValueError:
            #         print("Please enter a valid integer for time.")

            # if __name__ == "__main__":
            #     main()


                
        elif user_input==3:
            print("Water Reminder")
            notification.notify(
                title="drink water ",
                message="Experts recommend that males consume 15.5 cups (3.7 liters) of water daily and females 11.5 cups (2.7 liters). But environmental factors such as temperature and other health conditions may affect your water needs.",
                app_icon="C:\\Users\\marot\\Desktop\\Desktop notifier App\\waterGlassIcon.ico",
                timeout=10,
                
            )
            # 60 * 240
            time.sleep(10)

        
            

        elif user_input==4:
            print("Tablet Reminder")
            notification.notify(
                title="Take Your Tablet now",
                message="Firstly Eat Food then take tablet. For your illness this is best to take the tablet at suitable time. If you dont take the tablet then your illness may be increase or it affect on your health Totally.",
                app_icon="C:\\Users\\marot\\Desktop\\Desktop notifier App\\tablet.ico",
                timeout=14,
            )
            # 60 * 360
            time.sleep(12)
        
        elif user_input==5:
            print("LightBill, Phone Bill")
            notification.notify(
                title="PAY YOUR LightBill, Phone Bill ... NOW   ",
                message="Electricity is essential for our daily lives, providing power for lighting, heating, cooking, communication, industry, and transportation \n Paying bills on time leads to an improved credit score, and an improved credit score leads to lower monthly payments when it's time to take out a loan. Whether you're buying a car or getting a mortgage for a house, you can get better interest rates with a higher credit score. \n it will be easier for the drawer to recover the amount legally.",
                app_icon="C:\\Users\\marot\\Desktop\\Desktop notifier App\\bill.ico",
                timeout=10,
                
            )
            print("THis Will remind You after every 1 month.")

            time.sleep(60 * 43,200)
        else:
            print("invalid entered1")









    print("Hello from a function")
    user_input = int(input("Enter which operation want to perform :-  "))
    if user_input == 1:
        print("Switch off the computer")

from tkinter import *
from tkinter import ttk

win = Tk()
win.title("Desktop Notifier App window")

# Setting window background color
win.configure(bg="yellow")

# Label with text color
label = Label(win, text="Welcome To Desktop Notifier App  ", font=('Helvetica 37 bold underline'), fg="blue")
label.pack()

# Text widget with background color
text = Text(win, height=80, width=180, bg="pink", font=('Times 17 ') , fg="orange")
text.pack()

# Inserting text and paragraphs
text.insert(END,"\n Welcome to My Desktop Notification app \n \n ")
text.insert(END, "desktop notifier is a simple application which produces a notification message in form of a pop-up message on desktop \n desktop-notifier is a Python library for cross-platform desktop notifications. Currently supported platforms are: Linux via the dbus service org.freedesktop.Notifications macOS and iOS via the Notification Center framework [ experimental] Windows via the WinRT / Python bridge. \n \n  ")
text.insert(END, "A Desktop Notifier is a straightforward application that generates a notification message in the form of a pop-up message on the desktop. The main objective of the desktop notification application that we will learn to develop today is to constantly remind us of the different things that we require to accomplish throughout the day.\n \n ")
text.insert(END, "The main objective of the desktop notification application that we will learn to develop today is to constantly remind us of the different things that we require to accomplish throughout the day.\n \n \n ")

text.insert(END, "This is bet application for which a person which cant remind the everything,\n ")
text.insert(END, "This will Helps to remind the things like wise the tablet, phone bills pay and soon. \n \n")



text.insert(END, "But before we get started, let us briefly understand a desktop notifier and its working. A Desktop Notifier is a straightforward application that generates a notification message in the form of a pop-up message on the desktop. \n \n \n")
text.insert(END, "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed et hendrerit lorem. Fusce non justo vel libero suscipit feugiat. Vivamus euismod sapien a lacinia congue.\n \n ")



# Button to trigger the function
button = Button(win, text="Run O/P",fg="red" ,font=('Helvetica 37 bold ') , command=my_function)
button.pack()
text.insert(END, "RUN ABOVE  ipsum dolor sit amet, consectetur adipiscing elit. Sed et hendrerit lorem. Fusce non justo vel libero suscipit feugiat. Vivamus euismod sapien a lacinia congue.\n")


win.mainloop()