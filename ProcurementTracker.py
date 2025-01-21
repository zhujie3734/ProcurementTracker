
def main():
    while True:
        menu()
        choice=int(input('Please enter the function number:'))
        if choice in [0,1,2,3,4,5,6]:
            if choice == 0:
                answer = input('Do you really want to exit the system(y/n):')
                if answer == 'y':
                    break
                else:
                    continue
            elif choice == 1:
                insert()
            elif choice == 2:
                delete()
            elif choice == 3:
                modify()
            elif choice == 4:
                show()
            elif choice == 5:
                search()
            elif choice == 6:
                sort()
        else:
            print('You type in the wrong input, Please enter again among 1-7')
            continue

def menu():
    print('◆◆◆◆ Procurement Tracker ◆◆◆◆')
    print('◆◆◆◆     Menu         ◆◆◆◆')
    print('1. Insert Procurement Item')
    print('2. Delete Procurement Item')
    print('3. Modify Procurement Item')
    print('4. Display All the Items')
    print('5. Search Procurement Item')
    print('6. Sort Procurement Item')
    print('0. Exit the system')

def insert():
    pass

def delete():
    pass

def modify():
    pass

def Search():
    pass

def show():
    pass

def sort():
    pass


if __name__ == "__main__":
    main()