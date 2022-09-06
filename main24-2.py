import numpy as np
import cv2

ff = np.fromfile(r'24. 사진을 그림으로 변환하기 (OpenCV)\여행사진.jpg', np.uint8)
img = cv2.imdecode(ff, cv2.IMREAD_UNCHANGED)
img = cv2.resize(img, dsize=(0, 0), fx=1.0, fy=1.0, interpolation=cv2.INTER_LINEAR)

def onChange(pos):
    pass

cv2.namedWindow("Trackbar Windows")  # 트랙 윈도우를 생성합니다.

cv2.createTrackbar("sigma_s", "Trackbar Windows", 0, 200, onChange) # 트랙의 최소 최대 값을 지정합니다. 트랙이 움직일때마다 동작하는 함수를 지정합니다.
cv2.createTrackbar("sigma_r", "Trackbar Windows", 0, 100, onChange)  # 트랙의 최소 최대 값을 지정합니다. 트랙이 움직일때마다 동작하는 함수를 지정합니다.

cv2.setTrackbarPos("sigma_s", "Trackbar Windows", 100)  # 트랙의 기본 위치 지정
cv2.setTrackbarPos("sigma_r", "Trackbar Windows", 10)   # 트랙의 기본 위치 지정

while True:
    
    if cv2.waitKey(100) == ord('q'):  # opencv에서 킷값을 입력받습니다. 100ms동안 킷값을 기다리다가 값이 없으면 21줄의 코드 종료 후, 다음 코드 실행. q 값이 입력되면 반복문 종료
        break
    
    sigma_s_value = cv2.getTrackbarPos("sigma_s", "Trackbar Windows")  # 트랙의 포지션으로 값을 받습니다.
    sigma_r_value = cv2.getTrackbarPos("sigma_r", "Trackbar Windows") / 100.0  # 트랙의 포지션으로 값을 받습니다. 100을 나눠줍니다.

    print("sigma_s_value:",sigma_s_value)
    print("sigma_r_value:",sigma_r_value)

    cartoon_img = cv2.stylization(img, sigma_s=sigma_s_value, sigma_r=sigma_r_value)  # 트랙의 포지션에 따라서 이미지를 그림화합니다.

    cv2.imshow("Trackbar Windows", cartoon_img)

cv2.destroyAllWindows() # 모든 창이 닫히고 종료됩니다.
