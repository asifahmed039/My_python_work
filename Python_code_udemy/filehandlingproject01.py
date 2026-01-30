#journal entry project

fileName='journal.txt'

def write_entry():
    entry=input('write your journal entry: ')+'\n'
    with open(fileName,'w') as file:
        file.write(entry)

def read_all():
    with open(fileName,'r') as file:
        print('\n All journal enties')
        print(file.read())

def search_entries():
    keyword=input('Enter keyword to search: ')

    with open(fileName,'r') as file:
        all_line=file.readlines()
        for line in all_line:
            if keyword.lower() in line.lower():
                print(line.strip())
                return
    print("no match entries.")





def main_menu():
    while True:
        print('\n==== File journal Menu =====')
        print('1. Add Entry')
        print('2. Read all enteries')
        print('3. Search enteries')
        print('4. Exit')

        choice=input('choose option(1-4): ')

        if choice=='1':
            write_entry()
        elif choice=='2':
            read_all()
        elif choice=='3':
            search_entries()
        elif choice=='4':
            print('Goodbye')
        else:
            print('invalid choice')





if __name__=="__main__":
    main_menu()