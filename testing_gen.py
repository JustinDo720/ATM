from bank_register import gen_card_number as gn, gen_cvc_number as gc

for i in range(1000000000000000000000000000000000000000000000000):
    a = gn()
    if a[0] == '0':
        print('Na')
        break
    elif a[12] == '0':
        print('Na2')
        break
    else:
        print('gg')
        break