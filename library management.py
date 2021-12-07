'''build a library project from where
student can issue or return a book.
and library keeps maintain that all data and 
fruitfull replies will be gotta print there'''

class library:
    def __init__(self,books):
        self.books=books
    def show_books(self):
        print("\n  * ".join(self.books).upper())
    def borrow_book(self,bookname):
        if bookname in self.books:
            print(f"You have issued {bookname} successfully!")
            self.books.remove(bookname)
        
        else: 
            print(f"sorry this({bookname}) book is not available")
            
    def submit_book(self,bookname):
        if bookname in self.books:
            print(f"this({bookname}) book is already submitted Don\'t Cheat")
        else:
            self.books.append(bookname)
            print(f"[{bookname}] book is submitted successfully")

class student:
    def borrow_book_s(self):
        name = input('please enter book name : ')
        return name
    def submit_book_s(self):
        name = input('enter book name you want to submit : ')
        return name

# firstly make an object instantiation so that memory can allocate
A1 = library(['thermo','automobile','python','dbms','gk'])
S1 = student()
# Creating a menu to operate
welcomemsg = '''
__________________________
------- Welcome --------
   to Jatin Library
__________________________
Choose an option:
1. Show books
2. borrow a book
3. submit a book
4. exit
__________________________'''
while True:     #this is a infinite loop who do not had limit
    print(welcomemsg)
    try:
        I = int(input('enter here : '))
        # here make a conditional operation by if ledder
        if I == 1:
            A1.show_books()
        elif I == 2:
            A1.borrow_book(S1.borrow_book_s())
        elif I == 3:
            A1.submit_book(S1.submit_book_s())
        elif I == 4:
            print('Thanks.....')
            exit()
        else:
            print('Oops.. Your input was wrong..\n Please enter available options:')
    except ValueError:print('Please enter right value. try again...')