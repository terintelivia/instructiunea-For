n=int(input("introduceti n:"))
s=0
for i in range(1,n):
    if ((i%3==0)or(i%5==0)):
s+=i
print("suma numerelor care se impart la 3 si 5 de la 1 la ",n,","este" ,s)


        