import argparse,sys
sys.path.append('D:\\bysj\\DataSet')
import random
import numpy as np
f2=open('D:\\bysj\\DataSet\\DeepbaseN.fa','w')
f3=open('D:\\bysj\\DataSet\\hg19_allLncRNA.rnaFam.fa','r')
with open('D:\\bysj\\DataSet\\DeepBase.fa','r') as f1:
        for line in f1.readlines():
            linestr1 = line.strip()
            if ">"in linestr1:
                linestrlist =linestr1.replace(":", "\t")
                linestrlist1 =linestrlist.replace("-", "\t")
                linestrlist11 =linestrlist1.replace(">", "")
                linestrlist111 = linestrlist11.split("\t")
                line2 = f3.readline()
                linestr2 = line2.strip()
                #print(linestr2)
                linestrlist2 = linestr2.split("|")
                linestr3 =linestrlist2[0]
                linestrlist3 = linestr3.split("\t")
                #print(linestrlist2)
                #print(linestrlist3)
                #print(linestrlist111)
                if (linestrlist111[0]==linestrlist3[0])&(linestrlist111[1]==linestrlist3[1])&(linestrlist111[2]==linestrlist3[2]):
                    f2.write(">")
                    f2.write(str(linestrlist3[3])+'\n')
                    print(linestrlist3[3])
                else:
                    print("数据不匹配")
            else:
                f2.write(str(linestr1)+'\n')
            #linestrlist = linestr.split("|")
            
          
f2.close()  
f3.close()
