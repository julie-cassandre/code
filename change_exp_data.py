import argparse,sys
sys.path.append('D:\\bysj\\DataSet\\NONCODE V5\\NONCODEv5_human.lncRNA')
import random
import numpy as np
import math
from math import log
f2=open('D:\\bysj\\DataSet\\NONCODE V5\\NONCODEv5_human.lncRNA\\NONCODEv5_human.lncRNA2.exp','w')
with open('D:\\bysj\\DataSet\\NONCODE V5\\NONCODEv5_human.lncRNA\\NONCODEv5_human.lncRNA1.exp','r') as f1:
        for line in f1.readlines():
            linestr = line.strip()
            #print(linestr[0])
            linestrlist = linestr.split("\t")
            #linestrlist = linestr.split("|")
            #print(linestrlist)
            f2.write(str(linestrlist[0])+'\t')
            del(linestrlist[0])
            #print(linestrlist)
            def safe_float(number):
                try:
                    return float(number)
                except:
                    return 0.0
            a_float_list = list(map(safe_float,linestrlist))
            a_float_list = list(a_float_list)
            mean=(np.sum(a_float_list))/24
            print(mean) 
            #print(a_float_list)
            for i in range(len(a_float_list)):
                if(a_float_list[i]==0.0):
                    f2.write(str('0')+'\t')
                else:
                    a1=math.log(a_float_list[i],2)-mean
                    f2.write(str(a1)+'\t')
                    #print(a_float_list[i])
            f2.write('\n')
f2.close()        
