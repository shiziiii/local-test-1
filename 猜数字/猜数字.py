import random

num=random.randint(1,10)
guess_num=int(input("在1~10中猜一个数字"))
#三层if嵌套判断
if guess_num==num:
    print("第一次就猜对了")
else:
    if guess_num>num:
        print("猜大了，请再猜一次：")
    else:
        print("猜小了，请再猜一次：")
    guess_num=int(input())
    if guess_num==num:
        print("第二次就猜对了")
    else:
        if guess_num>num:
            print("猜大了，请再猜一次：")
        else:
            print("猜小了，请再猜一次：")
        guess_num = int(input())
        if guess_num == num:
            print("第三次才猜对")
        else:
            if guess_num > num:
                print("猜大了")
            else:
                print("猜小了")
            print("正确的数字是%d"%num)