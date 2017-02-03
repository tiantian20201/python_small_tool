# coding=gbk
'''
copy from Internet
mod by xbma
'''
import os,ConfigParser

'''
�ݹ��г�ĳĿ¼�µ��ļ�������List��
'''
def listDir (fileList,path):
    files=os.listdir(path)
    for i in  files:
        file_path = path + os.sep + i
        file_path = os.path.normpath(file_path)
        if os.path.isfile(file_path):
            fileList.append(file_path)
            
    for i in files:
        file_path = path + os.sep + i
        file_path = os.path.normpath(file_path)
        if os.path.isdir(file_path):
            listDir(fileList,file_path)
            
    return fileList

'''
��List������д���ļ�
'''
def writeListToFile(filelist, path):
    strs="\n".join(filelist)
    f=open(path,'wb')
    f.write(strs)
    f.close()
    
'''
�����ļ����ݲ�����List��
'''
def readFileToList(path):
    lists=[]
    f=open(path,'rb')
    lines=f.readlines()
    for line in lines:
        lists.append(line.strip())
    f.close()
    return lists

'''
�Ƚ��ļ�--��Set��ʽ
'''
def compList(list1,list2):
    return list(set(list1)-set(list2))

'''
�Ƚ�Դ·���ļ���Ŀ��·���ļ�
���������޸ĵ��ļ���ӵ��б��з���
'''
def compAllFiles(src, dest):
    allSrcFiles = []
    allSrcFiles = listDir(allSrcFiles, src)

    allDestFiles = []
    allDestFiles = listDir(allDestFiles, dest)

    diffList = []

    for srcfile in allSrcFiles:
        srcfilename = os.path.basename(srcfile)
        for destfile in allDestFiles:
            destfilename = os.path.basename(destfile)

            if(srcfilename == destfilename):
                if os.path.getsize(srcfile) != os.path.getsize(destfile):

                    diffList.append(srcfile)
                    
                    print srcfilename
            else:
                diffList.append(srcfile)

    return diffList

'''
����List���ļ���ָ��λ��
'''
def copyFiles(fileList,targetDir):

    #�ָ�·��
    pathArr = []
    #�ļ��ĸ�Ŀ¼
    lastDir = ''
    
    for childfile in fileList:

        if(len(pathArr) == 0):
            pathArr = os.path.dirname(childfile).split(os.sep)
            lastDir = pathArr[-1]
            
        #Ŀ��·��
        targetPath=os.path.join(targetDir, lastDir)
        print targetPath
        #Ŀ���ļ��� - ȫ·��
        targetFile=os.path.join(targetPath, os.path.basename(childfile))
        print targetFile

        if not os.path.exists(targetPath):
            os.makedirs(targetPath)
        if not os.path.exists(targetFile) or (os.path.exists(targetFile) and os.path.getsize(targetFile)!=os.path.getsize(childfile)):
            print "���ڸ����ļ���" + childfile
            open(targetFile,'wb').write(open(childfile,'rb').read())
        else:
            print "�ļ��Ѵ��ڣ������ƣ�"
            
if __name__ == '__main__':
    path=".svn"
    #��ȡԴĿ¼
    txtFile="files.txt"
    #Ŀ¼�ṹ�����Ŀ���ļ�
    tdir="cpfile"
    #���Ƶ���Ŀ��Ŀ¼
    cfFile="config.ini";
    #�����ļ��ļ���
    fileList=[]
    #��ȡ�����ļ�
    if(os.path.exists(cfFile)):
        cf=ConfigParser.ConfigParser()
        cf.read(cfFile)
        path=cf.get("main", "sourceDir")
        txtFile=cf.get("main","txtFile")
        tdir=cf.get("main","targetDir")
    else:
        print "�����ļ������ڣ�"
        raw_input("\n�� �س��� �˳�\n")
        exit()

    print '��ʼ���ļ��Ա�'
    resultArr = compAllFiles(path, tdir)
    if len(resultArr) > 0:
        print "�иĶ���������ļ���: \n"
        print resultArr
        print "\n�����ļ�����" + str(len(resultArr)) + "\n"

        if raw_input('\n�Ƿ����ļ��� (y/n)') != 'n':
            copyFiles(resultArr, tdir)
    else:
        print "û�в���ͬ���ļ�"

    '''  
    if(os.path.exists(txtFile)):
        #����������ļ����ڣ��Ͷ�ȡ��Ƚ�
        list1=readFileToList(txtFile)
        print "���ڶ�ȡ�ļ��б���"
        fileList=listDir (fileList,path)
        print "���ڱȽ��ļ�����"
        list_res=compList(fileList,list1)
        if len(list_res)>0:
            print "������ԭĿ¼�в����ڵ��ļ���\n"
            print "\n".join(list_res)
            print "\n�����ļ�����"+str(len(list_res))+"\n"
            if raw_input("\n�Ƿ����ļ�����y/n��") != 'n':
                copyFiles(list_res,tdir)
        else:
            print "û�в���ͬ���ļ���"
    else:
        #����������ļ������ڣ��򵼳��ļ�
        print "���ڶ�ȡ�ļ��б���"
        fileList=listDir (fileList,path)
        writeListToFile(fileList,txtFile)
        print "�ѱ��浽�ļ���"+txtFile
    '''  
    raw_input("\n�� �س��� �˳�\n")
    exit()
