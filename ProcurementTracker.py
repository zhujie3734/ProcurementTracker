
filename=r'E:\Software Engineering\git_repo\ProcurementTracker\ProcurementTracker_record.txt'

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
    item_list=[]
    while True:
        item_id=input('Please enter item id:')
        if not item_id:
            break
        item_name=input('Please enter item name:')
        if not item_name:
            break
        try:
            desc=input('Please enter item description:')
            unit_price=float(input('Please enter the unit price of the item:'))
            qty=int(input('Please enter how many you purchase:'))
            vendor=input('Please enter vendor name of the Item:')
            wp=input('Please enter the warranty period of the item(eg. 20250107-20251231)')

        except:
            print('Your input is not correct, Please enter the correct format')
        item={'item_id':item_id, 'item_name':item_name, 'desc':desc, 'unit_price':unit_price,'qty':qty,'vendor':vendor,'wp':wp}
        item_list.append(item)
        answer = input('Do you really want to continue(y/n):')
        if answer =='y':
            continue
        else:
            save(item_list)
            break

def save(lst):
    try:
        f=open(filename,'a',encoding='utf-8')
    except:
        f=open(filename,'w',encoding='utf-8')
    
    for i in lst:
        f.write(str(i)+'\n')
    f.close
       
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