import cv2
import os
def seq2vid(seq_root):
    img_root = os.path.join(seq_root,'frame')
    fps = 6
    # length = len(os.listdir(seq_root))
    seq = os.listdir(seq_root)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    
    s_d = os.path.join(seq_root,os.path.pardir,'video')
    if not os.path.isdir(s_d):  os.makedirs(s_d)

    videoWriter = cv2.VideoWriter(os.path.join(s_d,seq_root.split(os.sep)[-1]+'.avi'),fourcc,fps,(3840,2160),True)
    l = [int(x[5:10]) for x in os.listdir(seq_root)]
    for i in l:
        img = cv2.imread(img_root+str(i).zfill(5)+'.jpg')
        
        cropped = img[1080:3240,1920:5760,:]
        videoWriter.write(cropped)
        
    videoWriter.release()
if __name__ == "__main__":
    seq2vid('I:\\dataset\\Ours\\anno\zzc\\buildings4\\1')