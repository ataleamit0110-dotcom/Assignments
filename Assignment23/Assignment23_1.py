class BookStore:
    noOfBooks = 0
    def __init__(self, name, author):
        self.Name = name
        self.Author = author
        BookStore.noOfBooks =  BookStore.noOfBooks + 1
    
    def display(self):
        print("%s by %s. No of books: %d" %
              (self.Name, self.Author, BookStore.noOfBooks))


obj1 = BookStore("C programming", "Dennis Ritchie")
obj1.display()
obj2 = BookStore("Let us C", "Yashwant Kanetkar")
obj2.display()