import time
import pandas as pd
from datetime import datetime
import subprocess
import pyautogui


def sign_in(meeting_id,pw):
    subprocess.call(["C:/Users/damit/AppData/Roaming/Zoom/bin/zoom.exe"])
    time.sleep(2)

    join_btn=pyautogui.locateCenterOnScreen('join_button.png')
    # print(join_btn)
    pyautogui.moveTo(join_btn)
    pyautogui.click()

    #Type the meeting ID
    meeting_id_btn=pyautogui.locateCenterOnScreen('meeting_id.png')
    pyautogui.moveTo(meeting_id_btn)
    pyautogui.click()
    pyautogui.write(meeting_id)

    meeting_name_btn=pyautogui.locateCenterOnScreen('your_name_field.png')
    pyautogui.moveTo(meeting_name_btn)
    pyautogui.click()
    pyautogui.write("Amit Dutta")

    check_box=pyautogui.locateCenterOnScreen('check_box.png')
    pyautogui.moveTo(check_box)
    pyautogui.click()

    check_box=pyautogui.locateCenterOnScreen('check_box.png')
    pyautogui.moveTo(check_box)
    pyautogui.click()

    join_btn=pyautogui.locateCenterOnScreen('join.png')
    pyautogui.moveTo(join_btn)
    pyautogui.click()

    time.sleep(5)


    return

# sign_in("6423492125","K83yxG")

df=pd.read_csv("timings.csv")
while True:

    now=datetime.now().strftime("%H:%M")

    if now in str(df['timings']):

        row=df.loc[df['timings'] == now]
        m_id=df.loc[df.iloc[0,1]]
        m_pwd=df.loc[df.iloc[0,2]]

        sign_in(m_id,m_pwd)
        time.sleep(40)
        print('sign in')

# Join Zoom Meeting
# https://us05web.zoom.us/j/85418685680?pwd=NFN0ckdmcWpKa1l2ZDc5NTdEMkl1Zz09

# Meeting ID: 854 1868 5680
# Passcode: Q7rcCG











