contacts = {}

while True:
    print("\n Contact Book App")
    print("1. Create Contact")
    print("2. View Contact")
    print("3. Update Contact ")
    print("4. Search Contact")
    print("5. Delete Contact")
    print("6. Count Contact")
    print("7. Exit")

    choice = input('Enter your choice = ')

    if choice == '1':
        name = input('Enter your name = ')
        if name in contacts:
            print(f'Contact name {name} already exists!')
        else:
            age = input('Enter your age = ')
            email = input('Enter your email = ')
            mobile = input('Enter your mobile number = ')
            contacts[name] = {'age': int(age), 'email':email, 'mobile':mobile }
            print(f'Contact name {name} hs been created successfully!!')


    
    elif choice == '2':
        name = input('Enter contact name to view = ')
        if name in contacts:
            contact = contacts[name]
            print(f'Name:{name}, Age:{age}, Mobile Number:{mobile}')
        else:
            print('Contact Not Found!!')



    elif choice =='3':
        name = input('Enter contact name to update = ')
        if name in contacts:
            age = input('Enter your updated age = ')
            email = input('Enter your updated email = ')
            mobile = input('Enter your updated mobile number = ')
            contacts[name] = {'age': int(age), 'email':email, 'mobile':mobile }
        else:
            print('Contact Not Found!!')


    elif choice == '4':
        search_name = input('Enter contact name to search = ')
        found = False
        for name, contact in contacts.items():
            if search_name.lower() in name.lower():
                print(f'Found - Name:{name}, Age:{age}, Mobile Number:(mobile), Email:{email}')
                found = True
        if not found:
            print('No contact found with that name')

    

    elif choice == '5':
        name = input('Enter contact name to delete = ')
        if name in contacts:
            del contacts[name]
            print(f'Conatct name {name} has been deleted successfully!!')
        else:
            print('Contact does not exists')


    
    elif choice == '6':
        print(f'Total contacts in your book : {len(contacts)}')


    elif choice == '7':
        print('See you soon.. Closing the program')
        break

    else:
        print('Invalid Input')


    

