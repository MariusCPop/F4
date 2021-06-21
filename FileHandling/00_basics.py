### File handling basics https://realpython.com/working-with-files-in-python/ https://realpython.com/read-write-files-python/
my_file = open('test.txt')
try:
    print(my_file.read())
    print("It worked")
    # print(my_file.read())
    # print("It did not print")
    # my_file.seek(0)
    # print(my_file.read())
    # print("It works again")
    # print(my_file.readline())  # returneaza un string
    # my_file.seek(0)
    # print(my_file.readlines())  # returneaza o lista
finally:
    my_file.close()

# ### context manager, my_file e cunoscut sub denumirea de handle
# with open('test.txt') as my_file:
#     print(my_file.readlines())
#
# ### scrie un rand intr-un fisier gol sau suprascrie un fisier vechi
# with open('test.txt', mode='w') as my_file:
#     text = my_file.write('Hey it\'s me!')
#     print(text)
#
# ### adauga la fisier
# with open('test.txt', mode='a') as my_file:
#     text = my_file.write(';)')
#     print(text)
#
# ### daca nu exista fisierul il creeaza
# with open('sad.txt', mode='w') as my_file:
#     text = my_file.write(':(')
#     print(text)
#
# ### utilitatea with e ca inchide fisierul chiar si in cazul unor erori, deci nu trebuie adaugat "try except"
