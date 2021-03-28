from EventHandler import EventHandler
from time import sleep
from watchdog.observers import Observer

observed_folder = 'C:/Users/chrif/Downloads/Downloaded'
destination_folder = 'C:/Users/chrif/Downloads'

handler = EventHandler(observed_folder, destination_folder)

observer = Observer()
observer.schedule(handler, observed_folder, recursive=False)
observer.start()

try:
    while True:
        sleep(60)
except KeyboardInterrupt:
    print('Interrupted')
    observer.stop()
observer.join()
