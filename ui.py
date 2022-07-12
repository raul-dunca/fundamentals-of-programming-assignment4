from src.services.functions import function
from copy import deepcopy

class ui:
    def __init__(self):
        self._func = function()

    def __print_menu(self):
        print("1. Add a book")
        print("2. Display the list of books")
        print("3. Filter the list so that book titles starting with a given word are deleted from the list")
        print("4. Undo the last operation that modified program data")
        print("5. Exit")

    def _print_circles(self):
        books = self._func.get_list()
        for b in books:
            print(str(b))  # no more to_str functions, we use Python provided syntax

    def start(self):
        stack=[]
        stack.append(deepcopy(self._func.get_list()))
        while True:
            try:
                self.__print_menu()
                opt = input()
                if opt == "1":
                    isbn=input("Give the isbn of the book: ")
                    author=input("Give the author of the book: ")
                    title=input("Give the title of the book: ")
                    self._func.add_book(isbn,author,title)
                    stack.append(deepcopy(self._func.get_list()))
                elif opt == "2":
                    self._print_circles()
                elif opt=="3":
                    word=input("Given word: ")
                    a=self._func.filter_list(word)
                    if a!=True:
                        stack.append(deepcopy(self._func.get_list()))
                elif opt=="4":
                    self._func._book_list=self._func.undo(stack).copy()
                elif opt == "5":
                    return
                else:
                    print("Bad selection!")
            except ValueError as ve:
                print(ve)
            except IndexError as ie:
                print(ie)

console = ui()
console.start()