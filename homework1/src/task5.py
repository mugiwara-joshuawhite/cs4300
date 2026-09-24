'''
task5.py
Uses lists and dictionaries
'''

def favorite_books():
    '''
    favorite_books - uses list slicing to print 3 books and their authors
    '''
    books = ["The Hobbit - J.R.R. Tolkien", "God Emporer of Dune - Frank Herbert", "Catching Fire - Suzanne Collins"]
    for i in range(0, len(books)):
        print(books[i])

def student_database():
    '''
    student_database - creates a dictionary of students and their IDs
    '''
    # Note, the assignment specifications only say to create the dictionary and not to do anything with it, which
    # contradicts the "dict ops" requirement in the rubric, so in the test I just test that it is a dictionary and that
    # I can properly find a student in it
    students = dict()
    students["Alex Albertson"] = "000001"
    students["Bianca Baker"] = "000002"
    students["Chase Carson"] = "000003"
    students["Diana Day"] = "000004"
    students["Enid Ellis"] = "000005"
    students["Frank Freeman"] = "000006"
    students["Gary Green"] = "000007"
    return students