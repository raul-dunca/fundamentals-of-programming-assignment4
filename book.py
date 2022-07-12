class Book:
    def __init__(self,isbn,a,t):
        """
        this function initialize a object of class book and here we also verify if the data introduces is valid
        """
        if(len(isbn)==10 and isbn[3]==isbn[6]=="-" and isbn[0].isdigit() and isbn[1].isdigit() and isbn[2].isdigit() and
                isbn[4].isdigit() and isbn[5].isdigit() and isbn[7].isdigit() and isbn[8].isdigit() and isbn[9].isdigit()):
                self.isbn = isbn
        else:
            raise ValueError("\t !Invalid isbn!")
        if (a != '' and all(chr.isalpha() or chr.isspace() for chr in a)):    #verifies if a has only letters and spaces
            self.author = a
        else:
            raise ValueError("\t!Invalid Author!")
        self.title = t
    def get_isbn(self):
        return self.isbn
    def get_title(self):
        return self.title
    def get_author(self):
        return self.author
   # def set_isbn(self,new):
   #     self.isbn=new
   # def set_title(self,new):
   #     self.title=new
   # def set_author(self,new):
   #     self.author=new
    def __str__(self):
        return "Book with isbn: " + str(self.isbn) + ", title: " + str(self.title) + " and author: " + str(self.author)


