# coding=gbk  
'''
Created on 2017��8��12��

@author: Chongqing
'''
# Python3 ����������׼���������ͣ�
    # Number�����֣�
    # String���ַ����� ���ɸ���
    # List���б�          �ɸ���
    # Tuple��Ԫ�飩       ���ɸ���
    # Sets�����ϣ�
    # Dictionary���ֵ䣩�ɸ���

# ���������ֵ
a, b, c=1,2,"Chognqing"
print(a,b,c)

# 1,���� ---int float ����ֵ(False, True) ����J
d,e,f,g = 10, 1.5,True, 4+3j
print(d,e,f,g)

    ## type(),��ѯ������ָ�Ķ������ͣ�     isinstance
print(type(d),type(e),type(f),type(g))
print(isinstance(a, int))

    # del���ɾ��һЩ����
    # del var_a, var_b

    # ��ֵ����
print(2 / 4)  # �������õ�һ��������
print( 2 // 4) # �������õ�һ������
print(2 ** 5) # �˷�

# �ַ��� String�������ţ�˫���ţ���б��ת���ַ�
    # 0 Ϊ��ʼֵ��-1 Ϊ��ĩβ�Ŀ�ʼλ�á�
    # Python�е��ַ������ܸı䡣

str = "Huang"
print(str[0:-2]) # ���str[0]--str[-3],,,�����str[-2]
print(str*2)  # ����2��
print(str+" Chong")# �����ַ���

    # �����÷�б�ܷ���ת�壬�������ַ���ǰ�����һ�� r����ʾԭʼ�ַ���������б��(\)������Ϊ���з�    
print('Huang\Chong')      # ??????????????????????û��ת��
print(r'Huang\Chong')
    # Python�е��ַ������ܸı䡣

# �б�List ����[ͷ�±�:β�±�] ------------����--------------------------------------------------------
    # ython�ַ�����һ�����ǣ��б��е�Ԫ���ǿ��Ըı�ģ�
    #List�������кܶ෽��������append()��pop()��
list = ['Haung',12, 2.34]
print(list[1:])
list[1:] = [] # ������
print(list[1:])     


# Tuple��Ԫ�飩    
    # ��Ȼtuple��Ԫ�ز��ɸı䣬�������԰����ɱ�Ķ���
tup = (1,"HAung")
# tup[0]=1  #  �޸�Ԫ��Ԫ�صĲ����ǷǷ���

    # ������� 0 ���� 1 ��Ԫ�ص�Ԫ��Ƚ����⣬������һЩ������﷨����
tup1 = ()    # ��Ԫ��
tup2 = (20,) # һ��Ԫ�أ���Ҫ��Ԫ�غ���Ӷ���


# Set�����ϣ� ˳����ĺú�����
    # ���ϣ�set����һ�������ظ�Ԫ�ص�����
    # ��Ա��ϵ���Ժ�ɾ���ظ�Ԫ��
    # �ô����� { } ���� set() �����������ϣ�ע�⣺����һ���ռ��ϱ����� set() ������ { }����Ϊ { } ����������һ�����ֵ䡣
student = {'Tom', 'Jim2', 'Mary3', 'Tom', 'Jack5', 'Rose6'}
print(student)   # ������ϣ��ظ���Ԫ�ر��Զ�ȥ��
# ��Ա����
if('Rose6' in student) :
    print('Rose �ڼ�����')
else :
    print('Rose ���ڼ�����')

 
# set���Խ��м�������
a = set('abracadabra')
b = set('alacazam')
 
print(a)
print(b)
 
print(a - b)     # a��b�Ĳ
 
print(a | b)     # a��b�Ĳ���
 
print(a & b)     # a��b�Ľ���
 
print(a ^ b)     # a��b�в�ͬʱ���ڵ�Ԫ��


# Dictionary���ֵ䣩
    # �б�������Ķ����ϣ��ֵ�������Ķ��󼯺ϡ�
    # �ֵ���"{ }"��ʶ������һ������ļ�(key) : ֵ(value)�Լ��ϡ�
dict ={}
dict['name']='Huang'
dict[1]=123

tinydict={'name': 'Chongqing', 'ages': 20}

print(dict["name"])
print(tinydict.keys())
print(tinydict.values())

    # ���캯�� dict() ����ֱ�ӴӼ�ֵ�������й����ֵ����£�
print({x: x**2 for x in (2, 4, 6)})

    # Python��������ת��
s='ChongQIng'
# ������ s ת��Ϊһ��Ԫ��

print(tuple(s))
print(dict(tup)) # ����һ���ֵ䡣str ������һ������ (key,value)Ԫ�顣











