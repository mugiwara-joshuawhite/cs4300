import src.task7 as t7
from sympy import Matrix

def test_solve_rref_matrix():
    a = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    assert t7.solve_rref_matrix(a)[0] == (-1, 2)