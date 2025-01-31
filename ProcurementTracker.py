import os

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
            break
    save(item_list)

def save(lst):
    try:
        f=open(filename,'a',encoding='utf-8')
    except:
        f=open(filename,'w',encoding='utf-8')
    
    for i in lst:
        f.write(str(i)+'\n')
    f.close
       
def delete():
    while True:
        id=input('Please enter the item id you want to delete:')
        if id != "":
            if os.path.exists(filename):
                with open(filename,'r',encoding='utf-8') as rfile:
                    item_old=rfile.readlines()
            else:
                item_old=[]
            flag= False

            if item_old:
                d={}
                with open(filename,'w',encoding='utf-8') as wfile:
                    for item in item_old:
                        d=dict(eval(item))
                        if d['item_id'] != id:
                            wfile.write(str(item)+'\n')
                        else:
                            flag=True
                    if flag == True:
                        print('Procurement item has been deleted successfully')
                        answer=input('Do you want to continue,y/n:')
                        if answer == 'y':
                            continue
                        else:
                            break
                    else:
                        print('Did not find the item')
            else:
                print('No item stored!')
    
    show_item()

def show_item(lst):
    if len(lst) == 0:
        print('cannot find item info')
        return
    format_title='{:^6}\t{:^12}\t{:^8}\t{:^8}\t{:^18}\t{:^12}\t{:^3}\t{:^6}\t'
    print(format_title.format('item_id','item_name','desc','vendor','wp','unit_price','qty','total'))

    format_data='{:^6}\t{:^12}\t{:^8}\t{:^8}\t{:^18}\t{:^12}\t{:^3}\t{:^6}\t'
    for item in lst:
        print(format_data.format(item.get('item_id'),
                                 item.get('item_name'),
                                 item.get('desc'),
                                 item.get('vendor'),
                                 item.get('wp'),
                                 item.get('unit_price'),
                                 item.get('qty'),
                                 int(item.get('unit_price')*int(item.get('qty')))))
            
def modify():
    show()
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8') as rfile:
            item_old = rfile.readlines()
    else:
        return
     
    id=input('Please enter item id')
    with open(filename,'w',encoding='utf-8') as wfile:
                
        for item in item_old:
            d=dict(eval(item))
            if d['item_id'] != id:
                wfile.write(str(d)+'\n')
            else:
                while True:
                    try:
                        d['item_name']=input('Please enter the item name')
                        d['desc']=input('Please enter item description:')
                        d['unit_price']=float(input('Please enter the unit price of the item:'))
                        d['qty']=int(input('Please enter how many you purchase:'))
                        d['vendor']=input('Please enter vendor name of the Item:')
                        d['wp']=input('Please enter the warranty period of the item(eg. 20250107-20251231)')

                    except:
                        print('Your input is not correct, Please enter the correct format')
                    else:
                        break
                
                wfile.write(str(d)+'\n')   
        
        answer=input('do you want to continue(y/n):')
        if answer =='y':
            modify()

def search():
    new_item=[]
    while True:
        id=''
        name=''
        if os.path.exists(filename):
            mode=input('Please enter how to search item 1:id 2:name:')
            if mode == '1':
                id=input('Please input item id:')
            elif mode == '2':
                name=input('Please input item name:')
            else:
                print('type the wrong mode')
                search()
            with open(filename,'r',encoding='utf-8') as rfile:
                item_old=rfile.readlines()

                for item in item_old:
                    d=dict(eval(item))
                    if id == d['item_id']:
                        new_item.append(d)
                    elif name == d['item_name']:
                        new_item.append(d)
            
            show_item(new_item)
            new_item.clear()
            answer=input('Do you want to continue y/n:')
            if answer == 'y':
                search()
            else:
                break
        else:
            print('Do not have item info')

def show():
    new_item=[]
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8') as rfile:
            item_old=rfile.readlines()
            for item in item_old:
                d=dict(eval(item))
                new_item.append(d)
            show_item(new_item) 
    else:
        print('No item info stored')


def sort():
    new_item=[]
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8') as rfile:
            old_item=rfile.readlines()

            for item in old_item:
                d=dict(eval(item))
                new_item.append(d)
            
    sort_mode=input('Please input sort type: 0 as asc 1 as des:')
    if sort_mode == '0':
        sort_bool=False
    elif sort_mode == '1':
        sort_bool=True
    else:
        print('You type in the wrong choose')
        sort()

    mode=input('Please input how to sort the item: 1: sort by unit price  2: sort by qty')
    if mode == '1':
        new_item.sort(key=lambda x:int(x['unit_price']),reverse=sort_bool)
    elif mode == '2':
        new_item.sort(key=lambda x:int(x['qty']),reverse=sort_bool)
    else:
        print('You type in the wrong number')
        sort()
    show_item(new_item)

if __name__ == "__main__":
    main()