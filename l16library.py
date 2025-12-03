books = ["Python","Java","C++","C","JavaScript"]
cmdlist = ("list","search","register","delete","quit")

def listcmd():
    if len(books) == 0:
        print("There is no book in the library")
    else:
        print("\n list of books in the library")
        for book in books:
            print(f"{books.index(book) + 1}. {book}")

def searchcmd():
    getsearch = input("Enter your book name to search: ")
    for book in books:
        if getsearch.lower() in book.lower():
            print(f"{books.index(book) + 1}. {book}")

def registercmd():
    bookname = input("Enter your book name to add: ")
    if bookname in books:
        print("Book already exists")
    else:
        books.append(bookname)
        print("Book added successfully")

def deletecmd():
    booknum = input("Enter your book number to delete: ")
    sure = input(f"Are you sure to delete {books[int(booknum) - 1 ]} (yes/no): ").lower()
    if sure == "yes":
        books.pop(int(booknum) - 1)
        print("Book deleted successfully")
    else:
        print("Book not deleted")

def quitcmd():
    print("Thank you!")

while True:
    print("\nMy Library")
    print("--------------")
    print("# list")
    print("# search")
    print("# register")
    print("# delete")
    print("# quit")
    print("--------------")

    cmd = ""
    while not cmd in cmdlist:
        cmd = input("Enter your command: ")

    if cmd == "list":
        listcmd()
    elif cmd == "search":
        searchcmd()
    elif cmd == "register":
        registercmd()
    elif cmd == "delete":
        deletecmd()
    elif cmd == "quit":
        quitcmd()
        break