class Library:

    attributes = ['Name', 'Autor', 'PubYear', 'PageNo']

    def __init__(self, pathToDb):
        self.file = open(pathToDb, 'a+')

    def __del__(self):
        self.file.close()

    def listBooks(self):
        f = self.file
        f.seek(0) #come to the beginning of the file
        str = f.read() #read file
        list = str.splitlines() # list every line

        for book in list:
            bookAsList = book.split(',') #make a temporary list out of attributes for every book
            for i in range(2): #print 'Name' and 'Autor' attributes of the book
                print(f'{self.attributes[i]}: {bookAsList[i]} ')
            print()

    def addBook(self):
        book = []
        for attr in self.attributes:
            temp = input(f'{attr}: ')
            book.append(temp)

        bookAsStr = ','.join(book) #convert the book to a String Line
        self.file.write(f'{bookAsStr}\n') #add the book to the file(database)
        print(f"Book '{book[0]} succesfully added.'")

    def removeBook(self):
        f = self.file
        f.seek(0) #come to the beginning of the file
        str = f.read() #read file
        list = str.splitlines() # list every line
        BookName = input('BookName: ') #get name of the book which will be deleted

        found = False #if wanted book found or not
        for book in list:
            bookAsList = book.split(',') #make list out of attributes
            if BookName == bookAsList[0]: #get Name of the Book
                list.remove(book)
                found = True
                break

        if found:
            print(f"Book '{BookName}' succesfully deleted.")
            f.truncate(0) #make the old txt file(db) size 0, also this erase all data in it.
            newDb = '\n'.join(list) #new text.file(database) with wanted book removed
            f.write(f'{newDb}\n')
        else:
            print(f"Book '{BookName}' can not be found.")

lib = Library('books.txt')


#Main Function
while True:
    x = input('''
***MENU***
1- List Books
2- Add a Book
3- Remove a Book
4- Quit
What would you like to do?(Enter a number,for example press '1' for listing books): ''')
    print()
    if x=='1':
        lib.listBooks()
    elif x=='2':
        lib.addBook()
    elif x=='3':
        lib.removeBook()
    elif x=='4':
        print('Program succesfully terminated')
        del lib
        break
    else:
        print('Please enter a valid number 1,2,3 or 4')


     
