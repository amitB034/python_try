def sum_receipt():
    result= 0
    N = int(input("枚数は？"))
    print(N)
    for i in range(N):
        J = int(input(str(i+1)+"枚目の金額は？"))
        print(J)
        result += J
    
    print("合計は" + str(result) + "円")




sum_receipt()