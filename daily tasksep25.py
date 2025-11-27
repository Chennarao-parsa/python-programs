#flatten a list
'''
l=[1,[2,[3,4],5],6]
l2=[]
def list_flatten(l):
    for i in l:
        if type(i)==list:
            list_flatten(i)
        else:
            l2.append(i)
list_flatten(l)
print(l2)
'''
#decarator
'''
def decfun(f):
    def innerfunc():
        print('Function started')
        f()
        print('Function Ended')
    return innerfunc
@decfun
        
def display():
    print('Hello!')
display()
'''
#reverse a string
'''

def rev_string(s):
    if len(s)<=1:
        return s
    return rev_string(s[1:])+s[0]
print(rev_string("Hello"))

'''
#cls bank
'''
class Bankaccount:
    def __init__(self,account_holder,balance=0):
        self.account_holder=account_holder
        self.balance=balance

    def deposit(self,amt):
        if amt>0:
            self.balance=self.balance+amt
            print(f"deposited {amt} balance is {self.balance}")
        else:
            print("deposited amount is greater than 0")
    def withdrawal(self,amt):
        if amt>0 and amt<=self.balance:
            self.balance=self.balance-amt
            print(f"with draw {amt} balance is {self.balance}")
        else:
            print("withdrawal is not possible")
    def checkbal(self):
        print(f"Account holder {self.account_holder},Balancce{self.balance}")
        return self.balance
obj=Bankaccount("raj",10000)
obj.deposit(10000)
obj.withdrawal(5000)
obj.checkbal()
obj.withdrawal(17000)
obj.deposit(0)
'''
#book details
class Book:
    def __init__(self,title,author,pub_year):
        self.title=title
        self.author=author
        self.publication_year=pub_year
    def book_details(self):
        print(f"book title is {self.title}")
        print(f"Author of book is{self.author}")
        print(f"publication year is {self.publication_year}")
obj=Book("Ramayanam","valmiki",1900)
obj.book_details()
