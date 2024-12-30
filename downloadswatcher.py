from downloadsmover import *
import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Define the Downloads directory
downloads_dir = os.path.join(os.path.expanduser('~'), 'Downloads')

class DownloadHandler(FileSystemEventHandler):
    def on_created(self, event):
        # Check if the event is for a file (not a directory)
        if not event.is_directory:
            print(f"New file detected: {event.src_path}")
            notification.notify(
                title="New file in Downloads",
                message=f"File {event.src_path} has been detected",
                app_name = "Downloads Monitor",
                timeout=10, 
            )
            t.sleep(10)
            move_files()

def monitor_downloads():
    event_handler = DownloadHandler()
    observer = Observer()
    observer.schedule(event_handler, downloads_dir, recursive=False)
    observer.start()
    notification.notify(
        title='Downloads Monitor',
        message=f"Monitoring {downloads_dir} for new files.",
        app_name='Downloads Monitor',
        timeout=10
    )
    print(f"Monitoring {downloads_dir} for new files...")

    try:
        while True:
            time.sleep(1)  # Keep the script running
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    monitor_downloads()