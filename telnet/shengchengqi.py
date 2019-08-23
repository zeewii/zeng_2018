#coding=utf-8
#生成器学习

#迭代器
list1 = [1, 2, 3]
it = iter(list1)
print(type(it), it)
print(next(it))

#生成器
def count(n):
    while n > 0:
        # print("hello world!")
        m = yield n     # 生成值: n
        # print(m)
        n -= 1


c = count(10)
print(type(c), c)

# print(next(c))
# print(c.send("haha"))
# print(c.__next__())
# # c.throw(GeneratorExit)
# c.close()
# print(c.__next__())

for i in c:
    print(i)

