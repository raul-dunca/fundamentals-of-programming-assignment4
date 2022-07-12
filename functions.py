from src.domain.book import Book
from copy import deepcopy
from random import randint
from random import shuffle
class function:
    def __init__(self):
        """
        we initialize the list of book with 10 random generation of books the title and author are taken from the list
        below each having 20 elements
        """
        random_authors = ["Paul Pogba", "Bill Gates", "Pierre Gasly", "Kevin Durant", "Mihai Eminescu", "Elon Musk",
                          "Edwardo Erique", "Felix Lengyel", "Mihail Sadoveanu", "Marius Moga", "Max Verstappen",
                          "Giovani Buffon", "George Russell", "Ion Creanga", "Sasuke Uchiha", "Cristiano Ronaldo",
                          "LeBron James", "Michael Jordan", "Tudor Arghezi", "Lucian Blaga"]
        random_titles = ["Robinson Crusoe", "Frankenstein", "Moby-Dick", "Little Women", "Kidnapped", "Spider-man",
                         "Three Men in a Boat", "Dracula", "Little Kids", "The Call of the Wild", "The Witcher",
                         "The Golden Bowl", "Little Town", "The History of Mr Polly", "The Platypus",
                         "The Good Soldier", "Ulysses", "The Book", "A Passage to India", "The Sun Also Rises"]
        self._book_list=[]
        for i in range(0,10):
            shuffle(random_titles)
            self.add_book(str(randint(100, 999)) + "-" + str(randint(10, 99)) + "-" + str(randint(100, 999)),random_authors[randint(0,19)],random_titles[0])
            del random_titles[0]

    def add_book(self,i,a,t):
        """
        here we first check if the item we want to add has an unique isbn and a unique title bcs the same book
        cant be written by 2 authors and them if they are unique we check if the isbn and author are valid
        calling Book(x,y,z) and if all the condition are met we add the new element to the list
        :param i:isbn of the element we want to add
        :param a:author of the element we want to add
        :param t:title of the element we want to add
        :return:True only if one of the condition is not met otherwise just add the element
        """
        for j in range (0,len(self._book_list)):
            if(self._book_list[j].get_isbn()==i):
                raise ValueError("\t!Isbn already exists!")
        for j in range (0,len(self._book_list)):
            if(self._book_list[j].get_title()==t):
                raise ValueError("\t!A book can't have more than 1 author!")
        self._book_list.append(Book(i, a, t))
    def get_list(self):
        return self._book_list
    def filter_list(self,word):
        """
        we just get the first word form each title and check if its the different from "word" if so we add it to the
        result list  and then we copy in our list the result list, also this function return True if no elemnt
        was removed
        """
        rez=[]
        k=int(0)
        for i in range(0,len(self._book_list)):
            l=self._book_list[i].get_title().split(" ",maxsplit=1)
            if l[0]!=word:
                k=k+1
                rez.append(self._book_list[i])
        if k!=len(self._book_list):
            self._book_list=deepcopy(rez)
        else:
            return True
    def undo(self,stack):
        if (len(stack) > 1):
            stack.pop()
            return stack[-1]
        else:
            raise IndexError("\t!Cant undo anymore!")
def test_add_book():
    a=function()
    a.add_book("321-94-208","Karl Jacobs","The Beast")
    assert a._book_list[10].get_title()=="The Beast"
    assert a._book_list[10].get_isbn()=="321-94-208"
    assert a._book_list[10].get_author()=="Karl Jacobs"
    b=function()
    try:
        b.add_book("isbn", "Yao Ming", "The Dunk")
        assert False
    except ValueError as ve:
        assert str(ve) == "\t !Invalid isbn!"
    try:
        a.add_book("321-94-932", "Yao Ming", "The Beast")
        assert False
    except ValueError as ve:
        assert str(ve) == "\t!A book can't have more than 1 author!"
test_add_book()