import time
import os

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
