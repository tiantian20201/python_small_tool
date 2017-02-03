# coding=gbk

import os
import re
import urllib
import urllib2

def walkFiles(filePath):

    dirList = os.listdir(filePath)

    pathArr = []

    for childDir in dirList:

        #full name
        fullPath = os.path.join(filePath, childDir)

        if os.path.isdir(fullPath):
            walkFiles(fullPath)
        else:
            if(len(pathArr) == 0):
                pathArr = filePath.split(os.sep)
                #print pathArr[-1]

            #destDir = os.path.join(targetDir, pathArr[-1])

            #if not os.path.isdir(destDir):
                #os.makedirs(destDir)

            #����д���ļ���
            #destfile = os.path.join(destDir, childDir)

            #ȫ�ļ�·��
            #fullFilePathList.append(destfile);

            #����Ŀ¼���ļ� event/new/*.bin �ȵȵ�
            tempPathArr = fullPath.split('commons')

            usePath = tempPathArr[1]

            tempPathArr = usePath.split(os.sep)

            usePath = '/'.join(tempPathArr)
            
                
            #���ļ���
            fileUrls.append(usePath)
                
    

'''
��ȡ�����ļ� urlretrieve
'''
def getUrlFile(urls):
    
    for url in urls:
        try:
            urls = url.split('/bin')

            endFilePath = urls[1]

            endFilePathList = endFilePath.split('/')

            endFilePath = '\\'.join(endFilePathList)

            fullFileName = targetDir + endFilePath
            
            (topPath, endFile) = os.path.split(fullFileName)
                   
            mkdir(topPath)

            if not os.path.exists(fullFileName):
                print '�ļ�', fullFileName, '������...'

                request = urllib2.Request(url, headers = headers)
                response = urllib2.urlopen(request)
                content = response.read()

                if len(content) > 0:
                    urllib.urlretrieve(url, fullFileName, schedule)
                
        except urllib2.URLError, e:
                           
            if hasattr(e, 'code'):
                print e.code
                print '����ʧ��'
            
            #if hasattr(e, 'reason'):
                #print e.reason


'''
��ȡ�����ļ� urllib2
'''
def getAllFile(urls):

    
    for url in urls:

        if url.find('images') != -1:
            
            try:
                request = urllib2.Request(url, headers = headers)
                response = urllib2.urlopen(request)
                content = response.read()

                if content:
                    urls = url.split('/bin')

                    endFilePath = urls[1]

                    endFilePathList = endFilePath.split('/')

                    endFilePath = '\\'.join(endFilePathList)

                    fullFileName = targetDir + endFilePath

                    (topPath, endFile) = os.path.split(fullFileName)
                    
                    mkdir(topPath)

                    if not os.path.exists(fullFileName):
                        saveFileLocal(content, fullFileName)
                
            except urllib2.URLError, e:
            
                if hasattr(e, 'code'):
                    print e.code
            
                if hasattr(e, 'reason'):
                    print e.reason
                continue


'''
�����ļ�
'''
def saveFileLocal(data, fileName):

    f = open(fileName, 'wb')
    f.write(data)
    print u"���ڱ����ļ�", fileName
    f.close()



'''
urlretrieve �����ļ� 
'''
def schedule(a, b, c):
    '''
    a:�Ѿ����ص����ݿ�
    b:���ݿ��С
    c:Զ���ļ��Ĵ�С
    '''
    #print 'file c: ', c
    if c != 0:
        
        per = 100.0 * a * b / c
        if per > 100:
            per = 100

        print '%.2f%%' % per


'''
�������ļ�
'''
def saveFiles(files, name):

    for fileUrl in files:
        #splitPath = fileUrl.split('.')
        #fTail = splitPath.pop()

        saveFile(fileUrl, name)
    

'''
�����ļ�
'''
def saveFile(fileUrl, fileName):

    u = urllib.urlopen(fileUrl)
    data = u.read()
    f = open(fileName, 'wb')
    f.write(data)
    print u"���ڱ����ļ�", fileName
    f.close()


'''
����Ŀ¼
'''
def mkdir(path):
    path = path.strip()

    isExists = os.path.exists(path)

    if not isExists:

        print '����������Ϊ', path, '���ļ���'

        os.makedirs(path)
        return True
    else:
        #print '��Ϊ',path,'���ļ����Ѿ������ɹ�'
        return False
    

if __name__ == '__main__':

    targetDir = os.getcwd()

    print targetDir

    baseUrl = 'http://web-1699033708.ap-northeast-1.elb.amazonaws.com/bin/commons'

    childUrl = ['event/hscene/', 'event/new/', 'event/story/', 'event/tutorial/']

    fileUrl = baseUrl + childUrl[0]
    
    #getAllFile(fileUrl)

    fullFilePathList = []

    fileUrls = []

    fullUrls = []

    sourcePath = 'E:/FlowerClient/trunk/MainProject/bin/commons'
    walkFiles(sourcePath)

    for fileurl in fileUrls:

        fullUrl = baseUrl + fileurl

        fullUrls.append(fullUrl)


    user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
    headers = {'User-Agent':user_agent}


    #getAllFile(fullUrls)
    getUrlFile(fullUrls)
    

        
