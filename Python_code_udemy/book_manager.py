import struct

record_size=60
file_name="library.dat"

def pack_record(book_id,title,author,stock):
    title=title.strip().encode().ljust(30)
    author=author.strip().encode().ljust(20)

    return struct.pack('i30s20si',book_id,title,author,stock)

def unpack_record(record_bytes):
    book_id,title,author,stock=struct.unpack('i30s20si',record_bytes)

    return{
        "BOOK_ID":book_id,
        "Title":title.decode().strip(),
        "Author":author.decode().strip(),
        "stock":stock
    }

def add_book():
    book_id=int(input("enter the book id: "))
    title=input('enter book name: ')
    author=input('enter author name: ')
    stock=int(input("enter stock: "))

    record=pack_record(book_id,title,author,stock)

    with open('file_name','ab') as file:
        file.write(record)
        print('Add Successfully')

def view_books():
    with open(file_name,'rb') as file:
        print('\n===books record===')
        while True:
            record=file.read(record_size)
            if not record:
                break
            book=unpack_record(record)
            print(book)

def search_book():
    book_id=int(input("Enter book id for search: "))
    with open(file_name,'rb') as file:
        print('\n===books record===')
        while True:
            record=file.read(record_size)
            if not record:
                break
            book=unpack_record(record)
            if book["BOOK_ID"]==book_id:
                print("Book found: ",book)
                return
    print("Book not found.") 

def delete_book():
    book_id=int(input('Enter Book Id to delete: '))
    found=False
    with open(file_name,'r+b') as file:
        index=0
        while True:
            file.seek(index*record_size)
            record=file.read(record_size)
            if not record: break
            book=unpack_record(record)
            if book["BOOK_ID"]==book_id:
                file.seek(index*record_size)
                book['stock']=0
            file.write(pack_record(book["BOOK_ID"],book['title'],book['author'],book['stock']))
            found=True
            print("Book deleted (stock=0).")
            break
        index+=1
        




