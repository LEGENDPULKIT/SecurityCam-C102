import cv2

def Take_SnapShot():
    videoCaptureQbject=cv2.VideoCapture(0)
    result=True

    while (result):
        ret,frame=videoCaptureQbject.read()
        cv2.imwrite("newPicture1.jpg",frame)
        result=False

    videoCaptureQbject.release()

    cv2.destroyAllWindows()


Take_SnapShot()
