class library:

    def __init__(self):
        self.nobooks=0
        self.books=[]

    def addbooks(self,book):
        self.books.append(book)
        self.nobooks=len(self.books)

    def show(self):
        print(f"This genre has {self.nobooks} books")

li=library()
li.addbooks("harry potter 1")
li.addbooks("harry potter 2")
li.show()
    

    