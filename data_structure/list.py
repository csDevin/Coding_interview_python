# str1 = [1, 2, 3, 4, 5, 6, 7]
# print(str1, type(str1))
# text = ""
# for i in str1:
#     text = text + str(i)
# print(text, type(text))

str1 = [1, 2, 3, 4, 5, 6, 7]
print(str1, type(str1[0]), str(str1), type(str(str1)[0]))
a = "".join(str(str1))
print(a, type(a))
