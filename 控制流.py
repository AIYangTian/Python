# coding=gbk  
'''
Created on 2017��8��14��

@author: ������
'''
# if&for
# while && range
# break && contine && pass

# if���
    # Python ���� elif ������ else if
    # ��Python��û��switch �C case���

    # ����ʵ�� x Ϊ 0-99 ȡһ����,y Ϊ 0-199 ȡһ����,��� x>y ����� x�� ��� x ���� y ����� x+y���������y��
import random

x = random.choice(range(100))
y = random.choice(range(100))

if x>y:
    print("x:",x)
elif x==y:
    print("x+y:",x+y)
else:
    print("y:",y)

#  forѭ��
    # for���Ա����κ����е���Ŀ����һ���б����һ���ַ���
print("forѭ��----------------------------------")
sites = ["Baidu", "Google","Runoob","Taobao"]
for site in sites:
    if site == "Runoob":
        print("����̳�!")
        break
    print("ѭ������ " + site)
else:
    print("û��ѭ������!")
print("���ѭ��!")




# while���

    # ��Python��û��do..whileѭ����
    # ����ʹ�� CTRL+C ���˳���ǰ������ѭ����
    
    # while ѭ��ʹ�� else ���
count = 0
while count < 5:
    print (count, " С�� 5")
    count = count + 1
else:
    print (count, " ���ڻ���� 5")


## range()
    #��Ҫ�����������У�����ʹ������range()������������������
print("range()-----------------------------------")    
for i in range(5):
    print(i)

    # Ҳ����ʹrange��ָ�����ֿ�ʼ��ָ����ͬ������
for i in range(0, 10, 3) :
    print(i)
    
    # ���Խ��range()��len()�����Ա���һ�����е�����
    
a = ['Google', 'Baidu', 'Runoob', 'Taobao', 'QQ']
for i in range(len(a)):
     print(i, a[i])

    # ʹ��range()����������һ���б�
    
m=list(range(5))
print(m)

    # ���
sum = sum(range(101))
print("���1-100��",sum)

# break��continue��估ѭ���е�else�Ӿ�


# pass ���
    # Python pass�ǿ���䣬��Ϊ�˱��ֳ���ṹ�������ԡ�
    # pass �����κ����飬һ������ռλ���




