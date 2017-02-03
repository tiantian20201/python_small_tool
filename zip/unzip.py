# coding=gbk

import ConfigParser
import os
import zlib
import zipfile

#�����ļ�
def walkFiles(filePath):

    #��ѹ��д��Ŀ¼
    #destDir = os.path.join(os.getcwd(), 'test_unzip')
    destDir = targetDir

    #ѹ���ļ�ԴĿ¼
    pathDir = os.listdir(filePath)

    pathArr = [];
    for alldir in pathDir:
        
        #Դ�ļ�����·��
        child = os.path.join(filePath, alldir)
        
        #��Ŀ¼
        if os.path.isdir(child):
            #print child
            walkFiles(child)
            
        else:
            if(len(pathArr) == 0):
                pathArr = filePath.split(os.sep)
                print pathArr[-1]
            
            childDir = os.path.join(destDir, pathArr[-1])
                
            if not os.path.isdir(childDir):
                os.makedirs(childDir)

            destfile = os.path.join(childDir, alldir)
            
            #print destfile

            #����ѹ���ļ�д�뵽��Ŀ¼
            decompress(child, destfile)        
        

def compress(infile, dest, level=-1):
    infile = open(infile, 'rb')
    dest = open(dest, 'wb')
    com = zlib.compressobj(level)
    data = infile.read(1024)
    while data:
        dest.write(com.compress(data))
        data = infile.read(1024)
    dest.write(com.flush())
                               
def decompress(infile, dest):
    infile = open(infile, 'rb')
    dest = open(dest, 'wb')
    decom = zlib.decompressobj()
    data = infile.read(1024)
    while data:
        dest.write(decom.decompress(data))
        data = infile.read(1014)
    dest.write(decom.flush())
            

if __name__ == '__main__':

    #ѹ���ļ�Դ·��
    sourceDir = "srcPath"
    #��ѹ����·��
    targetDir = "tarPath"
    
    #�����ļ�
    cfFile = "config.ini"

    #��ȡ�����ļ�
    if(os.path.exists(cfFile)):
        cf = ConfigParser.ConfigParser()
        cf.read(cfFile)
        sourceDir = cf.get("main", "sourceDir")
        targetDir = cf.get("main", "targetDir")
    else:
        print "�����ļ������ڣ�"
        raw_input("\n�� �س��� �˳�\n")
        exit()


    print "��ʼ��ѹ"
    sourceDir = os.path.normpath(sourceDir)
    walkFiles(sourceDir)
        

    raw_input("��ѹ��� �� �س��� �˳�")
    exit()
