# coding=gbk  
'''
Created on 2017��8��14��

@author: ������
'''

# �����û������룺 input()
# �����ʽ��str(), str.format() 

# ��д�ļ�
    # f.read()
    # f.readline()

# str_1 = input("Enter a string:")
# str_2 = input("Enter another a string:")


## Output
# print("str_1 is :" + str_1 + ", str_2 is :" + str_2)
# print("str_1 is {} +  str_2 is {}".format(str_1, str_2))


## ��д�ļ�
# ��һ���ļ�
# f = open("File-test.txt", "w")
f = open("File-test.txt", "r")

# f.write( "Python ��һ���ǳ��õ����ԡ�\n�ǵģ���ȷ�ǳ���!!\n" )
str0 = f.read()
print(str0)
str1 = f.tell()
print("�ֽ�����", str1)

# �رմ򿪵��ļ�
f.close()


# python�ļ�д��Ҳ���Խ�����վ����,�ҵ�python�汾��3.6�����´����Ǵ�project.txt�ļ���
# ��������д��http://www.baidu.com��վ���롣
from urllib import request

response1 = request.urlopen("http://www.baidu.com/")  # ����վ
fi = open("project.txt", 'w')                        # openһ��txt�ļ�
page = fi.write(str(response1.read()))                # ��վ����д��
fi.close()                                           # �ر�txt�ļ�

