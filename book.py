book_lst = []
while True:
    def book_plass(book):
        book_lst.append(book)
    def book_minus(book):
        book_lst.remove(book)
    def book_print():
        print(book_lst)
    menu = int(input('1 - вывести список книг, 2 - добавить, 3 - убрать, 4 - отчистить.'))
    if menu == 1:
        book_print()
    elif menu == 2:
        book_plass(input('напиши книгу'))
    elif menu == 3:
        book_minus(input('напиши книгу'))
    elif menu == 4:
        book_lst.clear()