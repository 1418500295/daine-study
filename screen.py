import datetime
import time

from PIL import ImageGrab
import numpy as np
import cv2
import keyboard

def ac():
    screen = ImageGrab.grab()  # 获得当前屏幕

    length, width = screen.size  # 获得当前屏幕的大小
    video_decode_style = cv2.VideoWriter_fourcc(*'XVID')  # 编码格式
    video = cv2.VideoWriter(f'{time.strftime("%Y-%m-%d %H-%M-%S", time.localtime())}.avi', video_decode_style, 12,
                            (length, width))  # 输出文件命名为a.mp4,帧率为32，可以调节
    # print("screen record is doing, press <esc> to stop........")
    while True:
        im = ImageGrab.grab()
        imm = cv2.cvtColor(np.array(im), cv2.COLOR_RGB2BGR)  # 转为opencv的BGR格式
        video.write(imm)
        if keyboard.is_pressed("esc"):
            break
    video.release()
    cv2.destroyAllWindows()
if __name__ == '__main__':
    ac()
