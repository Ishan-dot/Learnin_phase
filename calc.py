W= print("++++++++++++++++++  Welcome To A simmple calculator  ++++++++++++++++++")
a=int(input('Enter first num:',))
b=int(input('Enter second num:',))
c=input('Enter the function you want to perform (+,-,x,/:)',)


p=a+b
m=a*b
s=a-b



if c in ('+','add','addition'):
    print('Output:',p)
elif c in ('-', 'sub', 'subtract'):
    print('Output:',s)
elif c in ('*','mult','multiplication'):
    print('Output:',m)
elif c in ('/','div','division'):
    if b==0:
        print('Cant divide by 0!!!')
    else:
        print('Output:',a/b)
else:
    print('Invalid Input')