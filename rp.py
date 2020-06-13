import time
from pywinauto.application import Application
from discoIPC import ipc
import psutil
import configparser
import win32gui
import win32process

config = configparser.ConfigParser()
config.read('config.ini')

client = ipc.DiscordIPC(config['CLIENT']['client_id'])


def check_open():
    activity = {
        'timestamps': {},
        'assets': {
            'large_image': 'book',
            'large_text': 'Epub Reader'  # change as you like
        }
    }

    client.connect()
    print('Starting Discord ICP')

    time_elapsed = int(time.time())

    def set_activity(state, details):
        activity['state'] = state
        activity['details'] = details
        activity['timestamps']['start'] = time_elapsed
        return activity

    while True:
        app = None
        try:
            app = Application().connect(path='epubfilereader.exe')
        except Exception as e:
            client.disconnect()
            print("Disconnecting Discord IPC")
            return False
        pid_of_epubfilereader = psutil.Process(app.process).pid
        foreground_win = win32gui.GetForegroundWindow()
        pid_of_another_app = None
        try:
            pid_of_another_app = win32process.GetWindowThreadProcessId(foreground_win)[1]
        except Exception as e:
            print(e)
            pass  # here you can add another event that can trigger if array of pid's is out of bounds.
        if pid_of_epubfilereader != pid_of_another_app:
            pass  # here you can add
                  # something that will trigger if the user is NOT focused on the EPUB File Reader.
        else:
            gui_title = win32gui.GetWindowText(foreground_win)
            if gui_title == "EPUB File Reader (www.epubfilereader.com)":
                set_activity("Not reading anything :(", "User is Idling.")
            else:
                set_activity(gui_title, "User is reading:")
            client.update_activity(activity)
            time.sleep(5)  # change as you like


while True:
    check_open()
    time.sleep(5)  # change as you like
