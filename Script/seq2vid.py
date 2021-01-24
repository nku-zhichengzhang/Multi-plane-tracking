#%%
import os
import cv2
import numpy as np
colorlist=[(0,0,0),(220,20,60),(0,0,205),(46,139,87),(255,215,0)]

def seq2vid(seq_root, anno_txt):
    img_root = os.path.join(seq_root,'frame')
    fps = 6
    seq = os.listdir(seq_root)
    txt = open(anno_txt, 'r')
    lines = txt.readlines()
    
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    
    s_d = os.path.join(seq_root,os.path.pardir,os.path.pardir,'gt','video')
    if not os.path.isdir(s_d):  os.makedirs(s_d)

    videoWriter = cv2.VideoWriter(os.path.join(s_d,seq_root.split(os.sep)[-1]+'.avi'),fourcc,fps,(3840,2160),True)
    l = list(set([int(x[5:10]) for x in os.listdir(seq_root)]))
    for i in l:
        print(i)
        img = cv2.imread(img_root+str(i).zfill(5)+'.jpg')
        point = []
        for line in lines:
            info = line.split(',')
            if int(info[0])==i:
                point.append(info[3:11])
        point = np.array(point).reshape((-1,1,2)).astype(float).astype(int)
        # print(point)
        for j in range(int((point.shape[0]+3)/4)):
            img = cv2.polylines(img, [point[j*4:4*j+4]], True, color=colorlist[j%5][0:3], thickness=5)
        cropped = img[1080:3240,1920:5760,:]
        cv2.putText(cropped, '#'+str(i),(200, 200), cv2.FONT_HERSHEY_COMPLEX, 5.0, (255, 255, 255), 25) 
        videoWriter.write(cropped)
        
    videoWriter.release()
    txt.close()
if __name__ == "__main__":
    seq2vid('I:\\dataset\\Ours\\anno\\zzc\\buildings4\\1','I:\\dataset\\Ours\\anno\\zzc\\gt\\buildings4\\1.txt')
# %%
