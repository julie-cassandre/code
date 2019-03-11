import argparse,sys
sys.path.append('D:\\bysj\\DataSet\\deepBaseV2.0')
import random
import numpy as np
f2=open('D:\\bysj\\DataSet\\hg19_allLncRNA.rnaFam.fa','w')
with open('D:\\bysj\\DataSet\\deepBaseV2.0\\hg19_allLncRNA.rnaFam.bed','r') as f1:
        for line in f1.readlines():
            linestr = line.strip()
            #print(linestr[0])
            linestrlist = linestr.split("\t")
            #linestrlist = linestr.split("|")
            #print(linestrlist[1])
            f2.write(str(linestrlist[0])+'\t')
            f2.write(str(linestrlist[1])+'\t') 
            f2.write(str(linestrlist[2])+'\t')
            f2.write(str(linestrlist[3])+'\n')
f2.close() 
