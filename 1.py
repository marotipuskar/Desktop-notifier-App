# import time
# from plyer import notification
# notification.notify(
#         title="Drink water Now ",
#         message="Experts recommend that males consume 15.5 cups (3.7 liters) of water daily and females 11.5 cups (2.7 liters). But environmental factors such as temperature and other health conditions may affect your water needs.",
#         # app_icon="C:\Users\marot\Desktop\Desktop notifier App\waterGlassIcon.png",
#         timeout="10"
# )
# time.sleep(60*240)


import time
from plyer import notification

notification.notify(
    title="Drink water Now",
    message="Experts recommend that males consume 15.5 cups (3.7 liters) of water daily and females 11.5 cups (2.7 liters). But environmental factors such as temperature and other health conditions may affect your water needs.",
    app_icon="C:\\Users\\marot\\Desktop\\Desktop notifier App\\waterGlassIcon.ico",
    timeout=10  # Timeout in seconds
)

time.sleep(60 * 240)  # Wait for 4 hours (60 seconds * 60 minutes * 4 hours)
