hang = int(input("nhập số hàng: "))
cot = int(input("nhập số cột: "))

cho_da_dat = []

def datcho():
    for i in range(hang):
        for j in range(cot):
            if (i, j) in cho_da_dat:
                print("X", end=" ")
            else:
                print("_", end=" ")
        print()
    
    so_hang = int(input("nhập số hàng: "))
    so_cot = int(input("nhập số cột: "))
    
    if so_hang <= 0 or so_hang > hang or so_cot <=0 or so_cot > cot:
        print("cho ngoi khong ton tai")
        return
    
    if (so_hang-1, so_cot-1) in cho_da_dat:
        print("cho ngoi da dc dat")
        return
    
    cho_da_dat.append((so_hang-1, so_cot-1))
    print("dat cho thanh cong")

def xemcho():
    for i in range(hang):
        for j in range(cot):
            if (i, j) in cho_da_dat:
                print("X", end=" ")
            else:
                print("_", end=" ")
        print()
    print("con lai", str(hang*cot - len(cho_da_dat)), "cho")
    
    print("cho da dat:", cho_da_dat)

while True:
    print("""
1. dat cho ngoi
2. xem cho ngoi
3. thoat
""")

    lc = int(input("lua chon: "))
    if lc == 1:
        datcho()
    elif lc == 2:
        xemcho()
    else:
        break