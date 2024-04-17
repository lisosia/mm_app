"""
Move the mouse cursor periodically
"""
import time
import pyautogui
import tendo
from tendo import singleton


# 二重起動防止
me = singleton.SingleInstance()

# 動かす頻度
INTERVAL_SEC = 3 * 60 - 1

# アプリが終了する時間
FINISH_SEC = 9 * 60 * 60

#スクリーンの隅にマウスが来たときに緊急停止する動作をOFF
pyautogui.FAILSAFE = False

next_move = 1
remain = FINISH_SEC
while remain > 0: 
    x, y = pyautogui.position()
    pyautogui.moveTo(x + next_move, y)

    next_move = - next_move
    remain -= INTERVAL_SEC

    time.sleep(INTERVAL_SEC)
