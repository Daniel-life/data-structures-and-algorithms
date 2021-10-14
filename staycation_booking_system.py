# Daniel Cheong Jun Jie, 200157E, Group 1
import sys
from datetime import datetime
record = {}


def menu():
    print("Welcome to Andes Hotel's staycation booking system!")
    print("1: Add record")
    print("2: Update selected record")
    print("3: Remove record")
    print("4: Display all records")
    print("5: Bubble sort or Selection sort - Price")
    print("6: Insertion sort - age")
    print("7: Binary Search - book no")
    print("8: Linear Search - room no")
    print("0: Exit Application")
    try:
        user = int(input("What action do you want to perform today (0-6)? "))
        if user == 1:
            add()

        elif user == 2:
            update_selected()

        elif user == 3:
            remove()

        elif user == 4:
            display_all()

        elif user == 5:
            price_data()

        elif user == 6:
            age_data()

        elif user == 7:
            book_data()

        elif user == 8:
            room_data()

        elif user == 0:
            sys.exit("Thank you. We Hope to see you again!")

        else:
            print("Please only input a number from 0 to 6.")
            menu()

    except ValueError:
        print("Please enter a valid number.")
        menu()
    return False


def add():
    try:
        index = 0
        while index < 20:
            input_package = input("What package did you get (0 to exit)? ")
            if input_package == str(0):
                print("exiting add record session...")
                break
            else:
                input_name = input("What's your name? ")
                input_age = int(input("What's your age? "))
                input_book = int(input("Whats your booking number? "))
                input_room_no = int(input("Whats your room no? "))
                input_check_in = input("What's your check-in date (dd/mm/yyyy)? ")
                datetime.strptime(input_check_in, '%d/%m/%Y')
                input_check_out = input("What's your check-out date (dd/mm/yyyy)? ")
                datetime.strptime(input_check_out, '%d/%m/%Y')
                input_price = float(input("Whats the price of the package? "))
                index += 1
                record[index] = {'name': input_name,
                                 'age': input_age,
                                 'book': input_book,
                                 'package': input_package,
                                 'room': input_room_no,
                                 'check-in date': input_check_in,
                                 'check-out date': input_check_out,
                                 'price': input_price}
                print("Record sucessfully added!")

    except ValueError:
        print("Please enter a valid value.")
        add()
    except TypeError:
        print("Please enter the correct type.")
        add()


def update_selected():
    update = int(input("select record to update (0 to exit): "))
    if update == 0:
        print("Exiting update session...")
        menu()

    elif update in record:
        for key, value in record[update].items():
            print(key, ":", value)
            print("- - - - - - - - - -")

        user = input(
            "Which detail do you want to update (name, age, package, room, check-in date, check-in time, check-out date, check-out time, price)? ")
        if user in record[update]:
            new = input("please input the new value: ")
            new_record = {user: new}
            record[update].update(new_record)
            print("You have changed the value of %s to %s" % (user, new))
            print("Here is the updated record:")
            for key, value in record[update].items():
                print(key, ":", value)
                print("- - - - - - - - - -")
                update_selected()

        else:
            print("Detail is not found in record!")
            update_selected()
    else:
        print("Record not found!")
        update_selected()


def remove():
    delete = int(input("Select record to delete: "))
    if delete in record:
        record[delete].clear()
        print("Record %d successfully deleted!" % delete)
    else:
        print("Record not found!")

    exit = input("do you want to exit (y/n)? ")
    if exit.lower() == "y":
        print("exiting remove session...")
        menu()
    else:
        remove()


def display_all():
    print("Here are all of your records: ")
    for i in range(1, len(record) + 1):
        print("Record %d:" % i)
        for key, value in record[i].items():
            print(key, ":", value)
        print("\n")

    exit = input("Do you want to exit? (y/n) ")
    if exit.lower() == "y":
        print("exiting display session...")
        menu()
    else:
        display_all()


def price_data():
    price = []

    for i in record:
        price.append(record[i]['price'])
    print("Prices: ", price)

    sort = input("what sorting method would you prefer (selection/bubble)? ")
    if sort == "bubble":
        bubble_sort(price)

    elif sort == "selection":
        ascend_descend = input("Do you want to print the price in ascending or descending order? ")

        if ascend_descend == "ascending":
            ascending_selection_sort(price)
        elif ascend_descend == "descending":
            descending_selection_sort(price)

    else:
        print("Please enter selection or bubble only.")
        price_data()

    exit = input("Do you want to exit? (y/n) ")
    if exit.lower() == "y":
        print("exiting price sort session...")
        menu()
    else:
        price_data()


def room_data():
    room = []
    for i in record:
        room.append(record[i]["room"])
    print("room record: ", room)
    linear_search(room)

    exit = input("Do you want to exit? (y/n) ")
    if exit.lower() == "y":
        print("exiting room search session...")
        menu()
    else:
        room_data()


def age_data():
    age = []
    for i in record:
        age.append(record[i]["age"])
    print("age record: ", age)
    insertion_sort(age)

    exit = input("Do you want to exit? (y/n) ")
    if exit.lower() == "y":
        print("exiting age sort session...")
        menu()
    else:
        age_data()


def book_data():
    book = []
    for i in record:
        book.append(record[i]["book"])
    print("book record: ", book)
    x = int(input("Enter booking number you want to search"))
    binary_search(book, x)
    book_search(book, x)

    exit = input("Do you want to exit? (y/n) ")
    if exit.lower() == "y":
        print("exiting book search session...")
        menu()
    else:
        book_data()


def descending_selection_sort(price_data):
    n = len(price_data)

    for i in range(n - 1):
        small_index = i

        for j in range(n - 1, i, -1):
            if price_data[j] > price_data[small_index]:
                small_index = j

        if small_index != i:
            tmp = price_data[i]
            price_data[i] = price_data[small_index]
            price_data[small_index] = tmp

    print("Sorted price in descending order: ")
    print("%s" % price_data)


def ascending_selection_sort(price_data):
    n = len(price_data)

    for i in range(n - 1):
        small_index = i

        for j in range(i + 1, n):
            if price_data[small_index] > price_data[j]:
                small_index = j

        if small_index != i:
            tmp = price_data[i]
            price_data[i] = price_data[small_index]
            price_data[small_index] = tmp


def bubble_sort(price_data):
    for i in range(1, len(price_data) + 1):
        n = len(price_data)

        for i in range(n - 1, 0, -1):
            noSwap = True

            for j in range(i):
                if price_data[j] > price_data[j + 1]:
                    temp = price_data[j]
                    price_data[j] = price_data[j + 1]
                    price_data[j + 1] = temp

            if noSwap:
                break
    print("Sorted price: ", price_data)


def insertion_sort(age_data):
    n = len(age_data)

    for i in range(1, n):
        value = age_data[i]

        j = i - 1
        while j >= 0 and value < age_data[j]:
            age_data[j + 1] = age_data[j]
            j -= 1
        age_data[j + 1] = value

    print("Sorted record: ")
    for i in range(n):
        print("%d" % age_data[i])


def binary_search(book_data, x):
    low = 0
    high = len(book_data) - 1

    while low <= high:
        mid = (high + low) // 2

        if book_data[mid] == x:
            first = mid
            cont = True
            while first > 0 and cont:
                if book_data[first - 1] == x:
                    first -= 1
                else:
                    cont = False
            return first

        elif x < book_data[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1


def book_search(book_data, x):
    if binary_search(book_data, x) == -1:
        print("Booking number not found!")
    else:
        print("Booking record: ", book_data)
        print("booking number found at poistion", binary_search(book_data, x))


def linear_search(room_data):
    n = len(room_data)
    x = int(input("Enter the room that you want to search: "))

    for i in range(n):
        print(i)
        if room_data[i] == x:
            print("%d is found at position %d!" % (x, i))
            break
        print("%d is not found in this position!" % x)


while True:
    if menu():
        break
        
