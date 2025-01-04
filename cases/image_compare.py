from skimage.metrics import structural_similarity as ssim

import cv2


def calculate_ssim(imageA, imageB):


    # 将图片转换为灰度图


    grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)


    grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)


    # 计算SSIM


    score, diff = ssim(grayA, grayB, full=True)


    return score



imageA = cv2.imread('x.jpg')


imageB = cv2.imread('x1.jpg')



ssim_score = calculate_ssim(imageA, imageB)


print(f"SSIM: {ssim_score}")
