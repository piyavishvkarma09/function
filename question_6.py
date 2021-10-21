def check_speed(speed):
    if speed<70:
        print("ok")
    elif speed >70:
        a=speed-70
        b=a//5
        print(b,"point")
        if b>12:
            print("your License suspended")
user=int(input("enter the speed"))
check_speed(user)