def nb(pO,percent,aug,p):
    year = 1

    while True:
        pO = pO + (pO*(percent/100)) + aug
        if int(pO) < p:
            year += 1
        else:
            break

    print(year)

nb(1000,2,50,1200)
nb(1500,5,100,5000)
nb(1500000,2.5,10000,2000000)