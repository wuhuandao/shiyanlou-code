a,b = 0,1
while b<100:
    print(b,end=' ') 
    a,b = b,a+b
print()
#print()默认每调用一次就会打印一个换行符，
#print的另一个参数end还替代换行符