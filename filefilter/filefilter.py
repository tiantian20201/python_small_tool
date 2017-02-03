# -*- coding: cp936 -*-

import os
import re

def walkfiles(filepath):

    listdir = os.listdir(filepath)

    pathArr = []

    dirname = ''

    fileList = []
    
    for childdir in listdir:

        childfile = os.path.join(filepath, childdir)

        if os.path.isdir(childfile):
            
            walkfiles(childfile)
        else:

            if(len(pathArr) == 0):
                pathArr = filepath.split(os.sep)
                #print filepath
                #print pathArr[-1]

                dirname = pathArr[-1]
                
                dirList.append(dirname)
            
            filename = os.path.basename(childfile)

            if 'Dto' not in filename:

                #print filename

                fileList.append(filename)

                #�ļ�ȫ·��
                fullFileNameList.append(childfile)

        if len(fileList) > 0 and dirname != '':
            
            apiDic[dirname] = fileList
                

def readFromFile(filelist):

     #ֵ�ֵ� ��������Ͷ�Ӧ��ֵ�б�
     valueDic = dict()
         
     for childfile in filelist:

         #�����ļ�·�������ļ���������չ��
         (filepath, tempfilename) = os.path.split(childfile)
         
         #�����ļ�������չ��
         #(shotname, extension) = os.path.splitext(tempfilename)

         #ֵ�б� ��ŵ�������ƥ����� endurl parameters
         singleValueList = []
         
         f = open(childfile, 'rb')
         
         lines = f.readlines()

         for line in lines:
             tripline = line.strip()

             #ƥ�� endurl ��
             urlMatchObj = re.match(r'(.+)=(.+\/\w+\/\w+.*)', tripline, re.M|re.I)

             if urlMatchObj:
                 #print 'endUrl    --> : ', urlMatchObj.group(2)

                 singleValueList.append(urlMatchObj.group(2))

             #else:
                 #print "No match!"

             #ƥ�� ���� 
             paraMatchObj = re.match(r'.+apiRequest\((.+)\).+', tripline, re.M|re.I)

             if paraMatchObj:
                 #print 'parameters --> : ', paraMatchObj.group(1)

                 singleValueList.append(paraMatchObj.group(1))
             #else:
                 #singleValueList.append('') #�еķ���û�в���
             
         #��������Ͷ�Ӧ��ֵ�б�
         valueDic[tempfilename] = singleValueList

     return valueDic



def writeToFile(dic, path):

    f = open(path, 'wb')

    dirCount = 0
    fileCount = 0

    #�ֵ����� ���ص���Ԫ���б�
    sortedTuple = sorted(apiDic.items(), key=lambda d:d[0])

    #childtuple[0] ����ǰ�ֵ���� key childtuple[1]����ǰ�ֵ����ֵ
    for childtuple in sortedTuple:
        dirCount += 1
        
        dirname = childtuple[0] #Ŀ¼��
        filelist = childtuple[1]#Ŀ¼�µ�����


        classInDirCount = len(filelist) #��Ŀ¼�µ�������

        linename = '-----------%s---------- Count: %s ' % (dirname, classInDirCount)

        #apinames = "\r\n".join(filelist)

        fileCount += len(filelist)

        f.write(linename)
        
        f.write('\r\n')
        
        for apiclass in filelist:
            
            paralist = paramDic[apiclass] #������Ӧ�Ĳ����б�

            f.write(apiclass) #д������
            f.write('  --  ')
            
            if len(paralist) is 2:
                f.write("EndURL:" + paralist[0] + '\n')
                f.write("FuncPara:" + paralist[1])
            else:
                f.write("EndURL:" + paralist[0] + '\n')
                f.write("FuncPara:�޲���")

            f.write('\r\n')
            
        f.write('\r\n')
        f.write('\r\n')

        print "Writing %s" % dirname
    

    lastStr = "Total Dir %s --- Total Files %s" % (dirCount, fileCount)
    f.write(lastStr)
    
    f.close()


def sortedDictValues(dic):
    items = dic.items()
    items.sort()

    return [value for key, value in items]

if __name__ == '__main__':

    #Ŀ¼�� API cateory
    dirList = []

    #Ŀ¼�µ��ļ��� api name
    apiList = []

    #Ŀ¼��Ӧ�ļ���  api cateory -- api names
    apiDic = dict()

    #�������ֵ�
    sortedDic = dict()

    #�ļ�ȫ·��
    fullFileNameList = []

    #�����Ͷ�Ӧ��endurl para ����
    paramDic = dict()

    #-----�����ļ����µ��������ļ� �ҳ� api ��
    filepath = 'D:/PythonTestCode/filefilter/api/'
    filepath = os.path.normpath(filepath)
    walkfiles(filepath)
    

    #------������ȡ��һ����ȡ�� api �࣬��ȡ endurl parameters
    paramDic = readFromFile(fullFileNameList)

    #for key in paramDic:
        #print "%s" %key, fileDic[key]


    
    #------�������ڵ�Ŀ¼�� ���� ��ӵ�е� endul paramters ����д��
    writefile = 'D:/PythonTestCode/filefilter/api.txt'
    writeToFile(apiDic, writefile)

    #print '\n'.join(fullFileNameList)

    
