def sum_receipt():
    result= 0
    N = int(input("枚数は？"))
    for i in range(N):
        J = int(input(str(i+1)+"枚目の金額は？"))
        result += J
    
    print("合計は" + str(result) + "円")




sum_receipt()