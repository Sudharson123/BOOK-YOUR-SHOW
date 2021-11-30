import datetime
import re
print("::::::::::::::::::::::::::::::::::: BOOK YOUR SHOW :::::::::::::::::::::::::::::::::::")
row =str(input('Enter the number of Rows:'))
column =str(input('Enter the number of Columns:'))
while row.isdigit()==False or column.isdigit()==False:
    print('****************** ROWS AND COLUMNS MUST BE IN NUMBERS ****************** ')
    row = str(input('Enter the number of Rows:'))
    column = str(input('Enter the number of Columns:'))
    continue
rows=int(row)
columns=int(column)
class seats_():
    def __init__(self):
        global rows
        global columns
        self.rows=rows
        self.columns=columns
        self.mat=[]
        self.info={}
        self.total_seats = self.rows * self.columns
        self.total_income=0
        self.current_income=0
        self.tickets=0
        for i in range(1,self.rows+1):
            a=[]
            for j in range(1,self.columns+1):
                a.append('S')
            self.mat.append(a)
    def show_seats(self):
        print(' THEATRE '.center(80,'*'))
        for i in range(0, self.rows + 1):
            if i == 0:
                for j in range(1, self.columns + 1):
                    print('   ', j, end='')
            else:
                print('\n', i, end='')
                for k in range(self.columns):
                    print(' ', self.mat[i - 1][k], end='  ')
        print()
    def buy_ticket(self):
        print('BOOK YOUR TICKET'.center(80,'*'))
        r= str(input('Enter the Row number:'))
        c= str(input('Enter the Column number:'))
        while r.isdigit() == False or c.isdigit() == False or int(r) not in range(1,rows+1) or int(c) not in range(1,columns+1):
            print('************ INPUT MUST BE IN NUMBERS ************')
            print('************ ALSO IN RANGE BETWEEN {} ROWS AND {} COLUMNS ************'.format(rows,columns))
            r = str(input('Enter the Row number:'))
            c = str(input('Enter the Column number:'))
            continue
        if self.total_seats > 60:
            first = self.rows // 2
            second=self.rows-first
            rr=self.columns*first
            cc=self.columns*second
            self.total_income=self.total_income+(((rr*10)+(cc*8)))
            if int(r)<=first:
                self.price =10
                print('Your Ticket Price is $10')
            else:
                self.price=8
                print('Your Ticket Price is $8')
        else:
            self.price =10
            self.total_income=self.total_income+(10*(self.rows*self.columns))
            print('Your Ticket Price is $10')
        print('Do You Want to Book Your Ticket??')
        print('1.Yes')
        print('2.No')
        s = int(input('Your Choice:'))
        while s not in range(1, 3):
            print('Your choice should be Either 1 or 2')
            print('1.Yes')
            print('2.No')
            s = int(input('Your Choice:'))
            continue
        if s==1:
            print('||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||')
            d = str(input('NAME:'))
            while re.findall('[0-9]|[@_!#$%^&*()<>?/|}{~:]',d):
                print('******* Name must be in alphabets *******')
                d = str(input('NAME:'))
                continue
            e = str(input('MOBILE NUMBER:'))
            b=bool(re.findall('^[6-9][0-9]{9}$',e))
            while b!=True:
                print('******* Mobile number should be in 10 digits only *******')
                e = str(input('MOBILE NUMBER:'))
                b = bool(re.findall('^[6-9][0-9]{9}$', e))
                continue
            f = str(input('AGE:'))
            ag=bool(re.findall('^[0-9]{2}$',f))
            while ag!=True:
                print('******* Enter a valid Age *******')
                f = str(input('AGE:'))
                ag=bool(re.findall('^[0-9]{2}$',f))
                continue
            print('********************************')
            print("1.Male\n2.Female\n3.Transgender")
            g=int(input('Enter your input for Gender:'))
            i=''
            if g==1:
                i="Male"
            elif g==2:
                i="Female"
            elif g==3:
                i="Transgender"
            else:
                print('Enter your choice between 1 to 3')
            t= str(datetime.datetime.now().replace(microsecond=0))
            dic = {}
            dic[int(r),int(c)] = {}
            dic[int(r),int(c)]=['NAME =' +d,'MOBILE NUMBER =' +e,'AGE =' +f,'DATE & TIME ='+t,'GENDER =' +i]
            self.info.update(dic)
            self.mat[int(r)-1][int(c)-1]='B'
            self.current_income=self.current_income+self.price
            self.tickets=self.tickets+1
            print("Thank You!!!Your Ticket Got Booked..\nYour Seat is Shown Below as 'B'..")
            self.show_seats()
        elif s==2:
            print('**************** Thank You...Hope see you soon!! ****************')
    def user_info(self):
        print('||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||')
        self.t=int(input('Enter your Row number:'))
        self.v=int(input('Enter your Column number:'))
        try:
            o = self.info[self.t, self.v]
            print('USER DETAILS'.center(80, '*'))
            for details in o:
                print(details)
        except KeyError or ValueError:
            print('************ SORRY...Yet This Seat Is Not Booked ************ ')
    def statistics(self):
        if self.total_income != 0:
            print('STATISTICS'.center(80, '*'))
            percent = (self.current_income / self.total_income) * 100
            print('Number Of Purchased Tickets:{}'.format(self.tickets))
            print('Percentage:{0:.2f}%'.format(percent))
            print('Current Income:${}'.format(self.current_income))
            print('Total Income:${}'.format(self.total_income))
        else:
            print('********** SORRY...Till Now No Tickets are Booked **********')