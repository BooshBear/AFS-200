print('All of the products over $19.99 are 15% OFF')
print('All of the products over $39.99 are 25% OFF')
discount1 = 0.15
discount2 = 0.25
product = input('What product do you want to buy? ')
baseprice = input('What is the base price? ')
baseprice = float(baseprice)
howmany = input('How many do you want? ')
howmany = int(howmany)
sum = baseprice * howmany
salestax = sum * 0.065
withtax = (sum + salestax)

print('Your Receipt')
print('-------------------------')
print(str(howmany) +' '+ product + ' @ $' + str(baseprice) + ' each')
print('Sales Tax $' + str(round(salestax, 2)))
if baseprice < 19.99:
    print('Total amount due $' + str(round(withtax, 2)))
if 19.99 <= baseprice <= 39.99:
    print('Total amount due $' + str(round(withtax - (withtax * discount1), 2)))
    print('Amount saved $' + str(round(withtax * discount1, 2)))
if baseprice > 39.99:
    print('Total amount due $' + str(round(withtax - (withtax * discount2), 2)))
    print('Amount saved $' + str(round(withtax * discount2, 2)))