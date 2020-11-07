nr1=int(input("introduceti nr1 :"))
nr2=int(input("introduceti nr2 :"))
nr3=int(input("introduceti nr3 :"))
nr4=int(input("introduceti nr4 :"))
nr5=int(input("introduceti nr5 :"))
nr6=int(input("introducetu nr6 :"))
s1=0
s2=0
s3=0
s4=0
s5=0
s6=3
for i in range(1,n1+1):
    s1+=i
for i in range(2,n2+1):
    s2+=(i-1)*i
for i in range(1,n3+1):
    p=1
    for n in range(1,i+1):
        p*=n
    s3+=p
for i in range(1,n4+1):
    s4+=i*10+2
for i in range(1,n5+1):
    s5+=i/(i+1)
for i in range(2,n6+1):
    if i<10:
        s6+=20+i
    else:
        s6+=20*(10**(i//10))+i
print("s1=",s1,sep="")
print("s2=",s2,sep="")
print("s3=",s3,sep="")
print("s4=",s4,sep="")
print("s5=",s5,sep="")
print("s6=",s6,sep="")