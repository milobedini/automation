import time

import pyautogui
import pywhatkit
from config import config
from pynput.keyboard import Controller, Key

keyboard = Controller()

# Below is a workaround due to library bug. Requires browser not on external screen.


def send_message(msg: str):
    try:

        pywhatkit.sendwhatmsg_instantly(
            phone_no=config["number"],
            message=msg,
            tab_close=True,
        )
        time.sleep(10)
        pyautogui.click()
        time.sleep(2)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        print("Message sent!")

    except Exception as e:
        print(str(e))


send_message("Finally yes?")

# Groups. Press invite to group via link and copy group ID.


def send_group_message(msg: str):
    pywhatkit.sendwhatmsg_to_group_instantly(
        group_id=config["groupId"],
        message=msg,
        tab_close=True,
    )


send_group_message("yuck indeed")
