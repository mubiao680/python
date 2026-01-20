'''
常用的值类型
Python 中常用的有 6 种值（数据）的类型
整数(int)，如：10、-10
浮点数(float)，如：13.14、-13.14
复数(complex)，如：4+3j，以 j 结尾表示复数
布尔(bool)，表达现实生活中的逻辑，即真和假，True 表示真，False 表示假。True 本质上是一个数字记作 1，False 记作 0
字符串(string)，描述文本的一种数据类型，由任意数量的字符组成，程序中需要加上引号来表示字符串
列表(List)，有序的可变序列，Python 中使用最频繁的数据类型，可有序记录一堆数据
元组(Tuple)，有序的不可变序列，可有序记录一堆不可变的 Python 数据集合
集合(Set)，无序不重复集合，可无序记录一堆不重复的 Python 数据集合
字典(Dictionary)，无序 Key-Value 集合，可无序记录一堆 Key-Value 型的 Python 数据集合
'''
# 我们可以通过 type() 语句来得到数据的类型：
# 语法：
# type(被查看类型的数据)
# 在 print 语句中，直接输出类型信息：


'''type()语句的使用方式'''

'''1. 在print语句中，直接输出类型信息：'''

print(type("黑马程序员"))
print(type(666))
print(type(11.345))

'''2. 用变量存储type()的结果（返回值）：'''

print(type("黑马程序员"))
string_type = type("黑马程序员")
print(type(666))
int_type = type(666)
print(type(11.345))
float_type = type(11.345)

print(string_type)
print(int_type)
print(float_type)

'''type()语句可以查看变量的数据类型'''

# type 查看变量的类型

name = "周杰轮"
age = 11
height = 172.55
print(type(name))
print(type(age))
print(type(height))

# 变量有类型吗？
# 我们通过 type(变量) 可以输出类型，这是查看变量的类型还是数据的类型？
# 查看的是：变量存储的数据的类型。因为，变量无类型，但是它存储的数据有。


# 总结

# 1. 使用什么语句可以查看数据的类型？
# type()
#
# 2. 如下代码，name_type 变量可以存储变量 name 的类型信息，是因为？
# name = "黑马程序员"
# name_type = type(name)
# 因为 type() 语句会给出结果（返回值）
#
# 3. 变量有没有类型？
# 没有，字符串变量表示变量存储了字符串而不是表示变量就是字符串