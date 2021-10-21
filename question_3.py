def number():
    i=1
    sum=0
    average=0
    while i<=3:
        user=int(input("Enter ur number: "))
        sum=sum+user
        i+=1
    print(sum)
    average=sum/3
    print(average)
number()
