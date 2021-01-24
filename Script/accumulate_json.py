import os
import sys
import json
import getopt

def main(argv):
    root = ''
    # print(argv)
    try:
        opts, args = getopt.getopt(argv,"hr:",["root="])
    except getopt.GetoptError:
        print('accumulate_json.py -r <rootdir>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('usage: accumulate_json.py -r <rootdir>')
            sys.exit()
        elif opt in ("-r", "--root"):
            root = arg
    
    savedir = os.path.join(root,'gt')
    if not os.path.exists(savedir): os.makedirs(savedir)

    def two2one(l):
        return [i for item in l for i in item]
    
    for scene in os.listdir(root):
        if scene == 'gt':   continue
        s_d = os.path.join(root,scene)
        sa_d = os.path.join(savedir,scene)
        if not os.path.exists(sa_d): os.makedirs(sa_d)

        for vid in os.listdir(s_d):
            if vid=='instances':   continue
            sv_d = os.path.join(s_d,vid)
            t = list()
            for i,f in enumerate(os.listdir(sv_d)):
                if os.path.splitext(f)[-1]!='.json':    continue
                jfile = open(os.path.join(sv_d,f), 'r', encoding='utf-8')
                content = jfile.read()
                a = json.loads(content)
                for x in a['shapes']:
                    x['frame_id']=int(os.path.splitext(f)[0][5:10])
                    t.append(x)

                jfile.close()
            num_id = list()
            for x in t:
                if x['group_id'] not in num_id:
                    num_id.append(x['group_id'])
            with open(os.path.join(sa_d,vid+'.txt'),'w')as txt:
                for i in num_id:
                    # print('instance:',i)
                    instance = []
                    for idx,x in enumerate(t):

                            
                        if x['group_id'] == i:
                            # print(x)
                            instance.append([x['frame_id'], x['group_id'], x['label']]+two2one(x['points']))
                    # print(instance)
                    for i in range(len(instance)):
                        for j in range(len(instance[i])):
                            txt.write(str(instance[i][j]))
                            txt.write(',')
                        txt.write('\n')

if __name__ == '__main__':    
    main(sys.argv[1:])
    