#Library  Management system
"""
    menu 
        1.Add Book
        2.Search Book
        3.View all book
        4.Delete Book
        
        """
from book_manager import *

def show_menu():
    while True:
        print('====Library Management System=====')
        print('1.Add Book')
        print('2.View Book')
        print('3.Search  Book by ID')
        print('4.Delete Book')
        print('5.Exit')
        choice=input('Enter your choice b/w (1 to 5): ')

        if choice=='1':
            add_book()
        elif choice=='2':
            view_book()
        elif choice=='3':
            search_book()
        elif choice=='4':
            delete_book()
        elif choice=='5':
            break
        else:
            print('Invalid input')
        input('\nPress enter to continue....')


if__name__=="__main__":
    show_menu()


