# coding=gbk

import ConfigParser
import os
import Tkinter
import tkFileDialog
import zlib
import zipfile

#�����ļ�
def walkFiles(filePath):

    #Ŀ���ļ�·��
    #destDir = os.path.join(os.getcwd(), 'zip')
    destDir = targetDir

    #Դ�ļ�Ŀ¼
    pathDir = os.listdir(filePath)
    
    pathArr = []
    
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

            #��ѹ�����ļ�д�뵽��Ŀ¼
            compress(child, destfile)

'''
����ѡȡ���ļ�����ѹ��
'''     
def zipFiles(filelist):

    destDir = targetDir

    pathArr = []
    for childfile in filelist:
        
        childfile = os.path.normpath(childfile)

        filename = os.path.basename(childfile)
        
        if(len(pathArr) == 0):
            pathArr = childfile.split(os.sep)
            print pathArr[-2]

        childDir = os.path.join(destDir, pathArr[-2])

        if not os.path.isdir(childDir):
            os.makedirs(childDir)

        destfile = os.path.join(childDir, filename)

        #��ѹ�����ļ�д�뵽��Ŀ¼
        compress(childfile, destfile)
        

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

    #Դ�ļ�·��
    sourceDir = "srcPath"
    #ѹ������·��
    targetDir = "tarPath"
    
    #�����ļ�
    cfFile = "config_unzip.ini"

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

    inpu = raw_input("\nѡ��ȫ��ѹ�� ����1�������ļ�ѹ������ 2: ")
    if(inpu == '1'):
        
        sourceDir = os.path.normpath(sourceDir)
        walkFiles(sourceDir)
        
    elif(inpu == '2'):
        print "ѡ�е��ļ�: "
        master = Tkinter.Tk()
        #master.withdraw() #����ʾ����������
        #master.mainloop()
        '''
        options = {}  
        options['defaultextension'] = '.bin'  
        options['filetypes'] = [('all files', '.*'), ('text files', '.txt')]  
        options['initialdir'] = 'C:\\'  
        options['initialfile'] = 'myfile.txt'  
        options['parent'] = master
        options['title'] = 'ѡȡҪѹ�����ļ�'
        '''
        
        filenames = tkFileDialog.askopenfilenames()
        print '\n'.join(list(filenames))
        print "��ʼѹ��"
        zipFiles(filenames)

        master.destroy()

    else:
        print "�˳�"
    
    raw_input("ѹ����� �� �س��� �˳�")
    exit()
