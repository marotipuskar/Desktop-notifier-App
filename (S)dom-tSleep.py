# import os
# import time

# def sleep_mode(duration):
#     print(f"Putting computer to sleep for {duration} seconds...")
#     time.sleep(duration)
#     # Put computer to sleep
#     if os.name == 'posix':  # for Unix/Linux/MacOS
#         os.system("sudo pmset sleepnow")
#     elif os.name == 'nt':  # for Windows
#         os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
#     else:
#         print("Unsupported OS")

# # def wake_up():
    
#     # Implement waking up the computer here (platform-specific)
#     # This might require third-party libraries or system-level commands

# def main():
#     try:
#         duration = int(input("Enter sleep duration in seconds: "))
#         sleep_mode(duration)
#         # After sleep duration, wake up the computer
#         # wake_up()
#     except ValueError:
#         print("Please enter a valid number for duration.")

# if __name__ == "__main__":
#     main()


import subprocess
import time

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
