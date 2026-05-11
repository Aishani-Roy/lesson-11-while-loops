num=int(input("enter number"))
sum=0
temp=num
while temp>0:
    digit=temp%10
    sum=sum+digit**3
    temp//=10
if sum==num:
    print("armstrong number")
else:
    print("not armstrong number")            
