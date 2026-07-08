from library import Library  # now import library class
l1 = Library()  # initialize object library

while True:
    print("\n ______library manangement system______")
    print("1. add book")
    print("2. remove book")
    print("3. search book")
    print("4. register user")
    print("5. view user profile")
    print("6. issue book")
    print("7. return book")
    print("8. show inventory")
    print("9. active loans")
    print("10. Exit")

    choice = input("Enter your choice (1-10): ")
    if choice == "1":
        isbn = input("ISBN: ")
        title = input("Title: ")
        author = input("Author: ")
        l1.add_book(isbn, title, author)
    elif choice == "2":
        isbn = input("ISBN: ")
        l1.remove_book(isbn)
    elif choice == "3":
        keyword = input("Enter ISBN/Title/Author: ")
        l1.search_book(keyword)
    elif choice == "4":
        user_id = input("User ID: ")
        user_name = input("User Name: ")
        membership = input("membership(student/teacher): ")
        l1.register_users(user_id, user_name, membership)
    elif choice == "5":
        user_id = input("User ID: ")
        l1.view_profile(user_id)
    elif choice == "6":
        isbn = input("ISBN: ")
        user_id = input("User ID: ")
        l1.issue_book(isbn, user_id)

    elif choice == "7":
        user_id = input("User ID: ")
        isbn = input("ISBN: ")
        l1.return_book(user_id, isbn)
    elif choice == "8":
        l1.inventory()
    elif choice == "9":
        l1.active_loans()
    elif choice == "10":
        print("Good Bye.!")
        break
    else:
        print("invalid choice.")