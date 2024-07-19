import os
import time
from plyer import notification
from tkinter import *
from tkinter import ttk,Text
win=Tk()
win.title("Desktop Notifier App window")
# Setting window background color
win.configure(bg="yellow")
# win.geometry("1750*250")
label=Label(text="Welcome To Desktop Notifier App", font=('Helvetica 17 bold underline'), fg="blue")
label.pack()
print("hi ")
# while True:
def print_data():
    # for i in range(20):
    #     print(i)
    print("1. Switch off the computer \n 2. Sleep Mode \n 3 Restart Computer \n 4. Water Reminder \n 5. Tablet Reminder \n 6. ALl Bills Reminder")
    user_input=int(input("Enter which operation want to perform :-  "))
    print(user_input)
    if user_input==1:
        print("Your computer is hanged thats why you choose this ")
        print("THanks for choosig this your window's trafic will clear in some minutes  ")
        print("Switch off the computer")
        def shutDown():
            if os.name=='nt':
                os.system('shutdown /s /t 2')
        shutDown()
        # SLEEP MODE
    elif user_input==2:
            print("Sleep Mode")
            print("Going to sleep for 20 seconds...")

    
    elif user_input==3:
            print("Water Reminder")
            def restart_window(delay):
                print("Restarting window in", delay, "seconds...")
                time.sleep(delay)
                print("Restarting window now!")
                os.system("shutdown /r /t 1")  # This restarts the system after 1 second

            if __name__ == "__main__":
                try:
                    user_input = int(input("Enter the time in seconds after which you want to restart the window: "))
                    restart_window(user_input)
                except ValueError:
                    print("Please enter a valid number of seconds.")

                        
                        
            time.sleep(10)
    
    elif user_input==4:
            print("Water Reminder")
            notification.notify(
                title="drink water ",
                message="Experts recommend that males consume 15.5 cups (3.7 liters) of water daily and females 11.5 cups (2.7 liters). But environmental factors such as temperature and other health conditions may affect your water needs.",
                app_icon="C:\\Users\\marot\\Desktop\\Desktop notifier App\\waterGlassIcon.ico",
                timeout=10,
                
            )
            # 60 * 240 
            time.sleep(10)
            

    elif user_input==5:
        print("Tablet Reminder")
        notification.notify(
            title="Take Your Tablet now",
            message="Firstly Eat Food then take tablet. For your illness this is best to take the tablet at suitable time. If you dont take the tablet then your illness may be increase or it affect on your health Totally.",
            app_icon="C:\\Users\\marot\\Desktop\\Desktop notifier App\\tablet.ico",
            timeout=14,
            )
            # 60 * 360
        time.sleep(12)
        
    elif user_input==6:
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

text=Text(win, height=28, width=105, font=('Times 17 ') , fg="red")
text.insert(END,"\n Welcome to My Desktop Notification app \n \n ")
# text.insert(END,"\n Welcome to My Desktop Notification app \n \n ")
text.insert(END, " Desktop notifier is a simple application which produces a notification message in form of a pop-up message on desktop \n desktop-notifier is a Python library for cross-platform desktop notifications. Currently supported platforms are: Linux via the dbus service org.freedesktop.Notifications macOS and iOS via the Notification Center framework [ experimental] Windows via the WinRT / Python bridge. \n \n  ")

text.insert(END, "\n A Desktop Notifier is a straightforward application that generates a notification message in the form of a pop-up message on the desktop. The main objective of the desktop notification application that we will learn to develop today is to constantly remind us of the different things that we require to accomplish throughout the day.\n \n ")
text.insert(END, "The main objective of the desktop notification application that we will learn to develop today is to constantly remind us of the different things that we require to accomplish throughout the day.\n \n \n ")

text.insert(END, "This is bet application for which a person which cant remind the everything,\n ")
text.insert(END, "\n This will Helps to remind the things like wise the tablet, phone bills pay and soon. \n \n")
text.insert(END, "\n But before we get started, let us briefly understand a desktop notifier and its working. A Desktop Notifier is a straightforward application that generates a notification message in the form of a pop-up message on the desktop. \n \n \n")

text.pack()


print_button=Button(win,text="START REMINDER" , command=print_data ,fg="orange")
print_button.pack()


output_label = Label(win, text="")
output_label.pack()
win.mainloop()




# print("hi ")
# def print_data():
#     for i in range(20):
#         print(i)


# print_button=Button(win,text="print_data" , command=print_data)
# print_button.pack()
# output_label = Label(win, text="")
# output_label.pack()