def sonning_raqamlar_soni(son):
    son = abs(son)
    raqamlar_soni = 0
    while son > 0:
        son //= 10
        raqamlar_soni += 1
    return raqamlar_soni

son = int(input("Sonni kiriting: "))
print(sonning_raqamlar_soni(son))