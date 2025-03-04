# class Library:
#     def __init__(self,books,no_of_books):
#         self.books =  books
#         self.no_of_books = no_of_books

#     def show_books(self):
#         if (type(self.books) == list):
#             print(f"The Books Present in the library are:")
#             for i in range(0,len(self.books)):
#                 print(self.books[i])
#         else:
#             print(f"The Library have only one book which is {self.books}")

#     def add_book(self,new_book):
#         if (type(self.books) == list and type(new_book) == list):
#             self.books.extend(new_book)
#             self.no_of_books = len(self.books)
#         elif (type(self.books) == list or type(new_book) == list):
#             if type(self.books) == list:
#                 self.books.append(new_book)
#                 self.no_of_books = len(self.books)
#             else:
#                 new_book.append(self.books)
#                 self.books = new_book
#                 self.no_of_books = len(self.books)
#         else:
#             self.books = [self.books,new_book]
#             self.no_of_books = 2

#     def No_books(self):
#         print(f"The Total Number of Books present in the Library are {self.no_of_books}")

# b = ["Cengage","HCV","Maths for ml","cs 229"]
# # print(type(b) == list)

# a = Library(b,len(b))

# a.show_books()
# # c = ["Electro","Add Bad","BE the best in your bloodline"]
# c = "Electro_dynamics"
# a.add_book(c)
# a.show_books()
# a.No_books()

