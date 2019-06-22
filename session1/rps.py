p1 = input('r,p,s? ')
p2 = input('r,p,s? ') 
if p1 == p2 :
    print('tie')

if p1 == 'r':
    if p2 == 's':
        print('p1 wins: rock beats scissors')
    if p2 == 'p':
        print('p2 wins with paper')