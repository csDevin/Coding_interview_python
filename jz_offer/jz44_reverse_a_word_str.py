# jz44: 翻转单词顺序列
# 使用str1.split(), list1.reverse(), "-".join(list1)这三个函数
def ReverseSentence(self, s):
    if len(s)==' ' or len(s)==' ':
        return s
    list1 = s.split() #正确写法，忽略空字符，连续多个空格能全部忽略
    # list1 = s.split(' ')***错误写法，会把两个空格之间的空字符当成一个字符来看待
    # "the sky is    blue"
    # "blue    is sky the"  # s.split()
    # "blue is sky the"  # s.split(' ')
    list1.reverse()
    s2 = " ".join(list1)
    return s2