import os
import sys
import json
import getopt

def set_id(vid_root,ori_class,ori_id,new_class,new_id,frame_range):

    for i,f in enumerate(os.listdir(vid_root)):
        if os.path.splitext(f)[-1]!='.json':    continue
        jfile = open(os.path.join(vid_root,f), 'r', encoding='utf-8')
        content = jfile.read()
        a = json.loads(content)
        jfile.close()
        flag=0
        for i in range(len(a['shapes'])):
            if a['shapes'][i]['label']==ori_class and a['shapes'][i]['group_id']==ori_id:
                print(int(os.path.splitext(f)[0][5:10]))
                if  int(os.path.splitext(f)[0][5:10]) < frame_range[0] or int(os.path.splitext(f)[0][5:10]) >= frame_range[1]:
                    continue
                a['shapes'][i]['group_id']=new_id
                a['shapes'][i]['label']=new_class
                flag=1
        if flag:
            wfile = open(os.path.join(vid_root,f), 'w', encoding='utf-8')
            json.dump(a,wfile)
            wfile.close()
        
set_id('I:\\dataset\\Ours\\anno\\zzc\\village5\\9','纸箱',2,'纸箱',6,[0,700])