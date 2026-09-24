import src.task5 as t5

def test_favorite_books(capsys):
    t5.favorite_books()
    assert capsys.readouterr().out == "The Hobbit - J.R.R. Tolkien\nGod Emporer of Dune - Frank Herbert\nCatching Fire - Suzanne Collins\n"

def test_student_database():
    students = t5.student_database()
    assert isinstance(students, dict)
    assert students["Alex Albertson"] == "000001"
    assert students["Gary Green"] == "000007"