'''
task7.py
Showcases a use case of sympy to solve a Matrix using RREF
Disclosure: This code was written by me, but was previously used for my Linear Algebra course.
'''
# Imports
from sympy import Matrix, symbols, pprint, Eq, linsolve    #I chose sympy as the package to use as an example
from sympy.parsing.sympy_parser import parse_expr

def solve_rref_matrix(mat: Matrix):
    '''
    solve_rref_matrix: Solves a matrix mat using Reduced Row Eschelon Form (RREF)
    '''

    #Variables
    equations = list()                      #Equations that will be created
    variables = symbols(f"x1:{mat.cols}")   #sympy symbols for x1 - xn
    free = list()                           #Free variables after rref
    
    #RREF and print the matrix
    rref_mat = mat.rref()
    reduced = rref_mat[0]
    pivots = rref_mat[1]
    pprint(reduced)
    
    #Get the free variable(s)
    #Pivots are 0-indexed while mat.cols is not, necessitating 0 - mat.cols - 2 and i + 1 to get x[free]
    for i in range(0, (mat.cols - 1)):
        if i not in pivots:
            free.append(i + 1)
    
    #Turn into true linear equations to make them easier to solve with sympy
    reduced_str_lineqs = lineqs_from_matrix(reduced)
    
    for lineq in reduced_str_lineqs:
        
        #Sympy expects a left hand side and a right hand side
        lhs, rhs = lineq.split("=")
        
        #parse_expr is able to turn a string into an expression in sympy
        #https://stackoverflow.com/questions/33606667/from-string-to-sympy-expression
        lhs = parse_expr(lhs)
        rhs = parse_expr(rhs)
        
        equations.append(Eq(lhs, rhs))
    
    #Get solved equations with linsolve
    #next(iter()) creates a tuple from them because the result of linsolve() is difficult to work with
    #https://stackoverflow.com/questions/49902898/solve-system-of-linear-equations-in-sympy
    solved_equations = linsolve(equations, variables)
    solved_equations = next(iter(solved_equations))
    
    #Print the solved equations
    for n in range(0, len(solved_equations)):
        print(f"x{n + 1} = {solved_equations[n]}")
    
    return [solved_equations, free]

def lineqs_from_matrix(mat: Matrix):
    '''
    lineqs_from_matrix
    Represents a sympy matrix as a system of linear equations (list of strings) using x1, x2, etc.
    Assumes is an augmented matrix, not a coefficient matrix
    '''
    #Variables
    lineqs = list()    #list of strings representing linear equations
    x = 1   #Which x is being written x1, x2, etc.
            
    #Loop through rows (n) and columns (m) of matrix
    for n in range (0, mat.rows):
        
        #Add a new string to the end for this new linear equation
        lineqs.append("")
        
        for m in range (0, mat.cols):
            
            #pull the element
            element = mat[n, m]
            
            #Only continue if not 0 (cause there would be no reason to write) or if at the end (because = 0) is a possibility
            if element != 0 or m == (mat.cols - 1):
                
                #If at start, and not at end
                if len(lineqs[n]) == 0 and m != (mat.cols - 1):
                    
                    #If negative, start with a negative sign
                    if element < 0:
                        lineqs[n] = f"-"
                    
                    #If -1 or 1, don't use the coefficient
                    if abs(element) == 1:
                        lineqs[n] = f"{lineqs[n]}x{x}"
                        
                    #If not -1 or 1, use the coefficient
                    else:
                        lineqs[n] = f"{lineqs[n]}{abs(element)}x{x}"
                
                #If at end
                elif m == (mat.cols - 1):
                    
                    #If at end and no equation has been made yet, throw away the equation
                    #at first i tried to make it 0 = 0, but that messed with linsolve later
                    if len(lineqs[n]) == 0:
                        lineqs.pop(n)
                        
                    #Otherwise add = element
                    else:
                        lineqs[n] = f"{lineqs[n]} = {element}"
                
                #If in the middle
                else:
                    
                    #If negative
                    if element < 0:
                        lineqs[n] = f"{lineqs[n]} - "
                    
                    #If positive
                    else:
                        lineqs[n] = f"{lineqs[n]} + "
                    
                    #If -1 or 1
                    if abs(element) == 1:
                        lineqs[n] = f"{lineqs[n]}x{x}"
                        
                    #If non-one constant
                    else:
                        lineqs[n] = f"{lineqs[n]}{element}x{x}"
            
            #Move on to next x
            x += 1
        
        #Reset x for next row
        x = 1
        
    return lineqs