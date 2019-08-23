#coding=utf-8
# import re
#
# #a = re.compile(r'\d{2}')
# a = re.compile(r'\w')
# # b = a.split("a b   c")
# # print(b)
#
# b = a.match("a b c")
# b.group()
# print(b.group())
#
#
# class A:
#     __slots__=['name']
#     def __init__(self):
#         self.name='js'
#         self.age=22
# a=A()
#
# from collections import Counter
#
# colours = (
#     ('Yasoob', 'Yellow'),
#     ('Ali', 'Black'),
#     ('Arham', 'Green'),
#     ('Ali', 'Blue'),
#     ('Yasoob', 'Red'),
#     ('Ahmed', 'Silver'),
# )
#



# favourite_colours = defaultdict(list)
#
#
# for name, colour in colours:
#     favourite_colours[name].append(colour)
#
# print(favourite_colours)
# print(favourite_colours['Ali'])
# print(favourite_colours['aa'])

# favs = Counter(name for name, colour in colours)
# print(favs, favs['Ali'])
#
#
#
# with open('/home/test/tools/haha', 'rb') as f:
#     line_count = Counter(f)
# print(line_count)

# import base64
# print(base64.b64decode(b'TXlyaWFkNzUzLg==').decode())





# from collections import namedtuple
#
# Animal = namedtuple('Animal', 'name age type')
# perry = Animal(name="perry", age=31, type="cat")
#
# print(Animal)
# print(perry)
#
# ## 输出: Animal(name='perry', age=31, type='cat')
#
# print(perry.name)
# print(perry.age)
# print(perry[1])
# # a = perry._asdict()
# # print(a)
# print(dict(perry))

from collections import OrderedDict
d = OrderedDict()
d['b'] = 'B'
d['c'] = 'C'
d['a'] = 'A'
for key,value in d.items():
    print(key,value)

print(d.keys())

















