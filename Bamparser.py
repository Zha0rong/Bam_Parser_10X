#!/usr/bin/python
import os
import csv
import subprocess
import sys
from collections import defaultdict, OrderedDict
from itertools import product, combinations
import gzip
import re
import random

def ParseFastq(pathtobam):
    processes=subprocess.Popen(['samtools', 'view',pathtobam],stdout=subprocess.PIPE)
    totalreads = processes.stdout
    while True:
        read=next(totalreads).decode()
        if read:
            yield read
        else:
            break
    for read in totalreads:
        read.close()

def write_fastq(file,ID,seq,quality_score):
    file.write('%s\n'%ID)
    file.write('%s\n' % seq)
    file.write('+\n')
    file.write('%s\n' % quality_score)

class BamParser:
    pathtobam=''
    outputname=''
    def __init__(self,pathtobam,outputname):
        self.pathtobam=pathtobam
        self.outputname=outputname

    def Parse(self):
        CB_UMI=gzip.open('%s_Read1.fastq.gz'%(self.outputname),'wt')
        RNA=gzip.open('%s_Read2.fastq.gz'%(self.outputname),'wt')
        for read in ParseFastq(self.pathtobam):
            parsed_read=read.split('\t')
            # Use the first column as read ID
            readname=parsed_read[0]
            CB=[x.replace('CR:Z:','') for x in parsed_read if 'CR:Z:' in x][0]
            CB_Qual=[x.replace('CY:Z:','') for x in parsed_read if 'CY:Z:' in x][0]
            UMI=[x.replace('UR:Z:','') for x in parsed_read if 'UR:Z:' in x][0]
            UMI_Qual=[x.replace('UY:Z:','') for x in parsed_read if 'UY:Z:' in x][0]
            RNA_seq=parsed_read[9]
            RNA_qual=parsed_read[10]
            CB_UMI_seq=(CB+UMI)
            CB_UMI_qual=(CB_Qual+UMI_Qual)
            write_fastq(CB_UMI,readname,CB_UMI_seq,CB_UMI_qual)
            write_fastq(RNA,readname,RNA_seq,RNA_qual)
        CB_UMI.close()
        RNA.close()

if __name__=="__main__":
    Process=BamParser(pathtobam='test_input/Donor1OC_subset.bam',outputname='test_output/Donor1OC_subset')
    Process.Parse()
