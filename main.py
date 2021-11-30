
import bookyourshow
result=bookyourshow.seats_()
while True:
    print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
    print('             1.SHOW SEATS')
    print('             2.BUY TICKET')
    print('             3.STATISTICS')
    print('             4.USER INFO')
    print('             0.EXIT')
    print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
    f = int(input('Enter Your Choice:'))
    while f not in range(0,5):
        print('Please..Enter Your Choice Between 1 to 4')
        f = int(input('Enter Your Choice:'))
        continue
    if f == 1:
        print(result.show_seats())
    elif f==2:
        print(result.buy_ticket())
    elif f==3:
        print(result.statistics())
    elif f==4:
        print(result.user_info())
    elif f== 0:
        print('************ Thank You...Hope Will see you soon!! ************')
        break