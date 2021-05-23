import time
import random
import cv2
import dropbox
start_time=time.time()

def Take_SnapShot():
    number=random.randint(0,100)
    VideoCaptureObject=cv2.VideoCapture(0)
    result=True

    while (result):
        ret,frame=VideoCaptureObject.read()
        img_name="img"+str(number)+".png"
        cv2.imwrite(img_name,frame)
        start_time=time.time()
        result=False
    
    VideoCaptureObject.release()
    cv2.destroyWindows() 

    return img_name


def upload_file(img_name):
    access_token='h-9vf199QgsAAAAAAAAAAX6E0ZEyFby6z1jgp1Z28q6nNFdfTZ1rl_DePFWFujoM'

    file=img_name
    file_from=file
    file_to="/newfolder1/"+(img_name)
    dbx=dropbox.Dropbox(access_token)
    with open(file_from,'rb') as f:
        dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
        print("File Uploaded")

def main():
    while (True):
        if((time.time()-start_time)>=100):
            name=Take_SnapShot()
            upload_file(name)

main()
    

      