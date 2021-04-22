while(1):
    num = int(input("please input the num: "))
    num_0x = hex(num)
    num_0b = bin(num)
    print(num_0x, type(num_0x), num_0b, type(num_0b))
    num_intx = int(num_0x, 16)
    num_intb = int(num_0b, 2)
    print(num_intx, num_intb)