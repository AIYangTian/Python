# coding=gbk  
'''
Created on 2017��8��14��

@author: hasee
'''
# �﷨����  syntax errors&& �쳣Exceptions

# while True  print("�﷨����")
# print(8/0)



    
    # while True:
    #         try:
    #             x = int(input("Please enter a number: "))
    #             break
    #         except ValueError:
    #             print("Oops!  That was no valid number.  Try again   ")
        
            
    # һ��except�Ӿ����ͬʱ�������쳣����Щ�쳣��������һ���������Ϊһ��Ԫ��
#     except (RuntimeError, TypeError, NameError):
#         pass


    # import sys
    # 
    # try:
    #     f = open('myfile.txt')
    #     s = f.readline()
    #     i = int(s.strip())
    # except OSError as err:
    #     print("OS error: {0}".format(err))
    # except ValueError:
    #     print("Could not convert data to an integer.")
    # except:
    #     print("Unexpected error:", sys.exc_info()[0])
    #     raise
            
# �׳�ָ���쳣
    # Python ʹ�� raise ����׳�һ��ָ�����쳣��
    
# raise NameError('HiThere')
    
    
#������������Ϊ
    # try ��仹������һ����ѡ���Ӿ䣬���������������κ�����¶���ִ�е�������Ϊ
# try:
#     raise KeyboardInterrupt
# finally:
#     print('Goodbye, world!')
#      
     
# Ԥ�����������Ϊ

for line in open("File-test.txt"):
    print(line, end="")
    
    # �ؼ��� with ���Ϳ��Ա�֤�����ļ�֮��Ķ�����ʹ����֮��һ������ȷ��ִ������������: 
with open("File-test.txt") as f:
    for line in f:
        print(line, end="")



    
    
    
    
    
    
    
    
    