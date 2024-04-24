from csp import *
import constants as const
from testdata import *


""" Given functions we can use in our code """
def gVar(x,y):
    return 'V_'+str(x)+'_'+str(y)

    
def puzzle_display(puzzle):
    comp=len(puzzle)
    for y in range(comp):
        for x in range(comp):
            print(puzzle[y][x],end=' ')
        print()

def puzzle_resolvido(puzzle,assignment):
    new_puzzle=puzzle.copy()
    for l in range(len(new_puzzle)):
        for c in range(len(new_puzzle[0])):
            if new_puzzle[l][c] =='.':
                new_puzzle[l][c]=assignment[gVar(c,l)][1]
    return new_puzzle




def getPuzzleColors(puzzle):
    colors = []
    for line in puzzle:
        for value in line:
            if value != '.':
                if value not in colors:
                    colors.append(value)
    return colors

def parse_domain(v, colors, aPuzzle) :
    # v is in the form V_X_Y. Extract x and y where Y is the puzzle line (top to bottom= and X is the column (left to right)
    varCol, varLine = map(int, v.split('_')[1:])
    value = aPuzzle[varLine][varCol]
    domain = []
    validCanos = const.CANOS
    validColors = colors
    # Remove pontas virados a norte, cotovelos virados para cima e verticais para a primeira linha
    if varLine == 0:
        validCanos = [x for x in validCanos if x != 'n' and x != 'ne' and x != 'nw' and x != 'ns' ]
    # Remove pontas viradas a sul, cotovelos virados baixo e verticais para a ultima linha
    if varLine == len(aPuzzle) - 1:
        validCanos = [x for x in validCanos if x != 's' and x != 'se' and x != 'sw' and x != 'ns' ]
    # Remove pontas viradas a oeste, cotovelos virados a este e horizontais para a ultima coluna
    if varCol == len(aPuzzle) - 1:
        validCanos = [x for x in validCanos if x != 'w' and x != 'ne' and x != 'se' and x != 'we' ]
    # Remove pontas viradas a este, cotovelos virados a oeste e horizontais para a primeira coluna
    if varCol == 0:
        validCanos = [x for x in validCanos if x != 'e' and x != 'nw' and x != 'sw' and x != 'we' ]

    # Remove anything that is not a ponta from the domain if the value is a color and remove 
    # any color that is not the current color
    if( value != '.' ):
        validCanos = [x for x in validCanos if len(x) == 1]
        validColors = [value]
    # Remove anything that is a ponta from the domain if the value is not ponta
    elif( value == '.' ):
        validCanos = [x for x in validCanos if len(x) == 2]

    for color in validColors:
            for cano in validCanos:
                domainTupple = (cano, color)
                domain.append(domainTupple)
    return domain

def constraint_function(var1, var1Tupple, var2, var2Tupple):
    (cano1, color1) = var1Tupple
    (cano2, color2) = var2Tupple
    var1Col, var1Line = map(int, var1.split('_')[1:])
    var2Col, var2Line = map(int, var2.split('_')[1:])
    if( cano1 == '.' or cano2 == '.' ):
        print ("ERROR: cano1 or cano2 is '.'")

    # NON TERMINALS
    if len(cano1) == 2:
        
        # When cano1 is ns
        if cano1 == 'ns':
            # if var2 is north of var1 then cano2 must be ('n', 'ns', 'ne', 'nw')
            if (var2Line < var1Line) and (var2Col == var1Col) :
                if cano2 not in ['n', 'ns', 'ne', 'nw'] and color1 != color2:
                    return False
            # if var2 is east of var1 then cano2 must be ('n', 's', 'ne', 'se')
            if (var2Line == var1Line) and (var2Col > var1Col):
                if cano2 not in ['n', 's', 'ns', 'ne', 'se', 'w']:
                    return False
            # if var2 is south of var1 then cano2 must be ('s', 'se', 'sw', 'ns')
            if (var2Line > var1Line) and (var2Col == var1Col) :
                if cano2 not in ['s', 'ns', 'se', 'sw']:
                    return False  
            # if var2 is west of var1 then cano2 must be ('n', 's', 'ns', 'nw', 'sw')
            if (var2Line == var1Line) and (var2Col < var1Col):
                if cano2 not in ['n', 's', 'ns', 'nw', 'sw', 'e'] and color1 != color2:
                    return False
        # When cano1 is we
        if cano1 == 'we':
            # if var2 is north of var1 then cano2 must be ('s', 'e', 'w', 'we', 'se', 'sw)
            if (var2Line < var1Line) and (var2Col == var1Col) :
                if cano2 not in ['s', 'e', 'w', 'we', 'se', 'sw']:
                    return False
            # if var2 is east of var1 then cano2 must be ('e', 'we', 'nw', 'sw')
            if (var2Line == var1Line) and (var2Col > var1Col):
                if cano2 not in ['e', 'we', 'nw', 'sw'] and color1 != color2:
                    return False
            # if var2 is south of var1 then cano2 must be ('e', 'w', 'we', 'ne', 'nw')
            if (var2Line > var1Line) and (var2Col == var1Col):
                if cano2 not in ['n', 'e', 'w', 'we', 'ne', 'nw']:
                    return False
            # if var2 is west of var1 then cano2 must be ('w', 'we', 'ne', 'se')
            if (var2Line == var1Line) and (var2Col < var1Col) and color1 != color2:
                if cano2 not in ['w', 'we', 'ne', 'se']:
                    return False
        # When cano1 is ne
        if cano1 == 'ne':
            # if var2 is north of var1 then cano2 must be ('s', 'e', 'w', 'we', 'se', 'sw')
            if (var2Line < var1Line) and (var2Col == var1Col) :
                if cano2 not in ['s', 'e', 'w', 'we', 'se', 'sw']:
                    return False
            # if var2 is east of var1 then cano2 must be ('e', 'we', 'nw', 'sw')
            if (var2Line == var1Line) and (var2Col > var1Col) and color1 != color2:
                if cano2 not in ['e', 'we', 'nw', 'sw']:
                    return False
            # if var2 is south of var1 then cano2 must be ('s', 'ns', 'se', 'sw')
            if (var2Line > var1Line) and (var2Col == var1Col) and color1 != color2:
                if cano2 not in ['s', 'ns', 'se', 'sw']:
                    return False
            # if var2 is west of var1 then cano2 must be ('n', 's', 'ns', 'nw', 'sw')
            if (var2Line == var1Line) and (var2Col < var1Col):
                if cano2 not in ['e', 'n', 's', 'ns', 'nw', 'sw']:
                    return False
        # When cano1 is nw
        if cano1 == 'nw':
            # if var2 is north of var1 then cano2 must be ('e', 'w', 'we', 'se', 'sw')
            if (var2Line < var1Line) and (var2Col == var1Col) :
                if cano2 not in ['s', 'e', 'w', 'we', 'se', 'sw']:
                    return False
            # if var2 is east of var1 then cano2 must be ('n', 's', 'ns', 'ne', 'se')
            if (var2Line == var1Line) and (var2Col > var1Col):
                if cano2 not in ['w', 'n', 's', 'ns', 'ne', 'se']:
                    return False
            # if var2 is south of var1 then cano2 must be ('s', 'ns', 'se', 'sw')
            if (var2Line > var1Line) and (var2Col == var1Col):
                if cano2 not in ['s', 'ns', 'se', 'sw'] and color1 != color2:
                    return False
            # if var2 is west of var1 then cano2 must be ('w', 'we', 'ne', 'se')
            if (var2Line == var1Line) and (var2Col < var1Col):
                if cano2 not in ['w', 'we', 'ne', 'se'] and color1 != color2:
                    return False
        # When cano1 is se
        if cano1 == 'se':
            # if var2 is north of var1 then cano2 must be ('n', 'ns', 'ne', 'nw')
            if (var2Line < var1Line) and (var2Col == var1Col):
                if cano2 not in ['n', 'ns', 'ne', 'nw'] and color1 != color2:
                    return False
            # if var2 is east of var1 then cano2 must be ('n', 's', 'ne', 'se')
            if (var2Line == var1Line) and (var2Col > var1Col):
                if cano2 not in ['e', 'we', 'nw', 'sw'] and color1 != color2:
                    return False
            # if var2 is south of var1 then cano2 must be ('s', 'se', 'sw', 'ns')
            if (var2Line > var1Line) and (var2Col == var1Col) :
                if cano2 not in ['n', 'e', 'w', 'we', 'ne', 'nw']:
                    return False
            # if var2 is west of var1 then cano2 must be ('n', 's', 'ns', 'nw', 'sw')
            if (var2Line == var1Line) and (var2Col < var1Col):
                if cano2 not in ['n', 's', 'e','ns', 'nw', 'sw']:
                    return False
        # When cano1 is sw
        if cano1 == 'sw':
            # if var2 is north of var1 then cano2 must be ('n', 'ns', 'ne', 'nw')
            if (var2Line < var1Line) and (var2Col == var1Col) :
                if cano2 not in ['n', 'ns', 'ne', 'nw'] and color1 != color2:
                    return False
            # if var2 is east of var1 then cano2 must be ('n', 's', 'ne', 'se')
            if (var2Line == var1Line) and (var2Col > var1Col):
                if cano2 not in ['n', 's', 'w', 'ns', 'ne', 'se']:
                    return False
            # if var2 is south of var1 then cano2 must be ('s', 'se', 'sw', 'ns')
            if (var2Line > var1Line) and (var2Col == var1Col) :
                if cano2 not in ['n', 'e', 'w', 'we', 'ne', 'nw']:
                    return False
            # if var2 is west of var1 then cano2 must be ('n', 's', 'ns', 'nw', 'sw')
            if (var2Line == var1Line) and (var2Col < var1Col):
                if cano2 not in ['w', 'we', 'ne', 'se',] and color1 != color2:
                    return False
    
    ##  TERMINALS  ##
    elif len(cano1) == 1:
    
        # When cano1 is N
        if cano1 == 'n':
            # if var2 is north of var1 then cano2 must be ('s', 'e', 'w', 'we', 'se', 'sw')
            if (var2Line < var1Line) and (var2Col == var1Col) :
                if cano2 not in ['s', 'e', 'w', 'we', 'se', 'sw']:
                    return False
            # if var2 is east of var1 then cano2 must be ('e', 'we', 'nw', 'sw')
            if (var2Line == var1Line) and (var2Col > var1Col):
                if cano2 not in ['n', 's', 'w', 'ns', 'ne', 'es']:
                    return False
            # if var2 is south of var1 then cano2 must be ('e', 'w', 'we', 'ne', 'nw')
            if (var2Line > var1Line) and (var2Col == var1Col) :
                if cano2 not in ['ns', 'se', 'sw'] and color1 != color2:
                    return False
            # if var2 is west of var1 then cano2 must be ('w', 'we', 'ne', 'se')
            if (var2Line == var1Line) and (var2Col < var1Col):
                if cano2 not in ['n', 's', 'e', 'ns', 'nw', 'sw']:
                    return False
        # When cano1 is E
        if cano1 == 'e':
            # if var2 is north of var1 then cano2 must be ('s', 'e', 'w', 'we', 'se', 'sw)
            if (var2Line < var1Line) and (var2Col == var1Col) :
                if cano2 not in ['s', 'e', 'w', 'we', 'se', 'sw']:
                    return False
            # if var2 is east of var1 then cano2 must be ('e', 'we', 'nw', 'sw')
            if (var2Line == var1Line) and (var2Col > var1Col):
                if cano2 not in ['n', 's', 'w', 'ns', 'ne', 'se']:
                    return False
            # if var2 is south of var1 then cano2 must be ('e', 'w', 'we', 'ne', 'nw')
            if (var2Line > var1Line) and (var2Col == var1Col) :
                if cano2 not in ['n', 'e', 'w', 'we', 'ne', 'nw']:
                    return False
            # if var2 is west of var1 then cano2 must be ('w', 'we', 'ne', 'se')
            if (var2Line == var1Line) and (var2Col < var1Col):
                if cano2 not in ['we', 'ne', 'se'] and color1 != color2:
                    return False  
        # When cano1 is S
        if cano1 == 's':
            # if var2 is north of var1 then cano2 must be ('n', 'ns', 'ne', 'nw')
            if (var2Line < var1Line) and (var2Col == var1Col) :
                if cano2 not in ['ns', 'ne', 'nw'] and color1 != color2:
                    return False
            # if var2 is east of var1 then cano2 must be ('n', 's', 'ne', 'se')
            if (var2Line == var1Line) and (var2Col > var1Col):
                if cano2 not in ['n', 's', 'w', 'ns', 'ne', 'se']:
                    return False
            # if var2 is south of var1 then cano2 must be ('s', 'se', 'sw', 'ns')
            if (var2Line > var1Line) and (var2Col == var1Col) :
                if cano2 not in ['n', 'e', 'w', 'we', 'ne', 'nw']:
                    return False
            # if var2 is west of var1 then cano2 must be ('n', 's', 'ns', 'nw', 'sw')
            if (var2Line == var1Line) and (var2Col < var1Col):
                if cano2 not in ['n', 's', 'e', 'ns', 'sw', 'nw']:
                    return False
        # When cano1 is W
        if cano1 == 'w':
            # if var2 is north of var1 then cano2 must be ('s', 'e', 'w', 'we', 'se', 'sw')
            if (var2Line < var1Line) and (var2Col == var1Col) :
                if cano2 not in ['s', 'e', 'w', 'we', 'se', 'sw']:
                    return False
            # if var2 is east of var1 then cano2 must be ('n', 's', 'ns', 'ne', 'se')
            if (var2Line == var1Line) and (var2Col > var1Col):
                if cano2 not in ['we', 'nw', 'sw'] and color1 != color2:
                    return False
            # if var2 is south of var1 then cano2 must be ('s', 'ns', 'se', 'sw')
            if (var2Line > var1Line) and (var2Col == var1Col) :
                if cano2 not in ['n', 'e', 'w', 'we', 'ne', 'nw']:
                    return False
            # if var2 is west of var1 then cano2 must be ('w', 'we', 'ne', 'se')
            if (var2Line == var1Line) and (var2Col < var1Col):
                if cano2 not in ['n', 's', 'e', 'ns', 'nw', 'sw']:
                    return False
        return True

def parse_neighbors(v, aPuzzle):
    neighbors = []
    # v is in the form V_X_Y. Extract x and y where Y is the puzzle line (top to bottom= and X is the column (left to right)
    varCol, varLine = map(int, v.split('_')[1:])
    var = aPuzzle[varLine][varCol]
    # extract the value at x, y of the north, south east and west neighbour
    north = aPuzzle[varLine-1][varCol] if varLine > 0 else None
    if( north != None ):
        neighbors.append(f"V_{varCol}_{varLine-1}")

    south = aPuzzle[varLine+1][varCol] if varLine < len(aPuzzle) - 1 else None
    if( south != None ):
        neighbors.append(f"V_{varCol}_{varLine+1}")

    east = aPuzzle[varLine][varCol+1] if varCol < len(aPuzzle) - 1 else None
    if( east != None ):
        neighbors.append(f"V_{varCol+1}_{varLine}")

    west = aPuzzle[varLine][varCol-1] if varCol > 0 else None
    if( west != None ):
        neighbors.append(f"V_{varCol-1}_{varLine}")

    return neighbors

def numberLinkParsePuzzle(aPuzzle):
    variables = []
    neighbors = {}
    domains = {}
    colors = getPuzzleColors(aPuzzle)

    # Verify puzzle is a grid
    if not all(len(row) == len(aPuzzle) for row in aPuzzle):
        raise ValueError('Puzzle is not a grid')

    comp=len(aPuzzle)
    for y in range(comp):
        for x in range(comp):
            v = f"V_{x}_{y}"
            variables.append(v)    
            neighbors[v] = parse_neighbors(v, aPuzzle)
            domains[v] = parse_domain(v, colors, aPuzzle)

    return (variables, domains, neighbors)


puzzle1, puzzle1ExpectedVariables, expectedPuzzle1Domains = puzzle1TestDetails()

puzzle_display(puzzle1)
variables, domains, neighbors = numberLinkParsePuzzle(puzzle1)

numberLinkCSP = CSP(variables, domains, neighbors, constraint_function)
assert sorted(numberLinkCSP.variables) == sorted(puzzle1ExpectedVariables)
for v in sorted(numberLinkCSP.variables) :
    print("Parsed: ", v, sorted(numberLinkCSP.domains[v]))
    print("Expecd: ", v, sorted(expectedPuzzle1Domains[v]))
    assert sorted(numberLinkCSP.domains[v]) == sorted(expectedPuzzle1Domains[v])
