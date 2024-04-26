from csp import *

# Gera a variável a partir das coordenadas (x,y): V_x_y
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

""" Constantes do jogo Numberlink """

""" TIPOS DE CANOS 
Pontas
* n: virado para cima, norte.
* w: virado para a esquerda, oeste.
* e: virado para a direita, este.
* s: virado para baixo, sul.
* ns: cano vertical
* we: cano horizontal
Cotovelos
* ne: cotovelo para cima e para a direita
* nw: cotovelo para cima e para a esquerda
* se: cotovelo para baixo e para a direita
* sw: cotovelo para baixo e para a esqueda
"""
COTOVELOS_NORTE = ['ne', 'nw']
COTOVELOS_ESQUERDA = ['nw', 'sw']
COTOVELOS_DIREITA = ['ne', 'se']
COTOVELOS_SUL = ['se', 'sw']
COTOVELOS = COTOVELOS_NORTE + COTOVELOS_SUL
VERTICAIS = ['ns']
HORIZONTAIS = ['we']
ORTOGONAIS = VERTICAIS + HORIZONTAIS
PONTAS_NORTE = ['n']
PONTAS_SUL = ['s']
PONTAS_ESTE = ['e']
PONTAS_OESTE = ['w']
PONTAS = PONTAS_NORTE + PONTAS_SUL + PONTAS_ESTE + PONTAS_OESTE
CANOS = COTOVELOS + ORTOGONAIS + PONTAS


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
    validCanos = []
    validColors = colors

    # If the value is a color, then the domain can only contain pontas of that color
    if( value != '.' ):
        validCanos = PONTAS
        validColors = [value]
    else : # If the value is a dot, then the domain can contain any color and any type of cano except pontas
        validCanos = COTOVELOS + HORIZONTAIS + VERTICAIS

        
    # Remove pontas virados a norte, cotovelos virados para cima e verticais para a primeira linha
    if varLine == 0:
        validCanos = [x for x in validCanos if x != 'n' and x != 'ne' and x != 'nw' and x != 'ns' ]
    # Remove pontas viradas a sul, cotovelos virados baixo e verticais para a ultima linha
    if varLine == len(aPuzzle) - 1:
        validCanos = [x for x in validCanos if x != 's' and x != 'se' and x != 'sw' and x != 'ns' ]
    # Remove pontas viradas a este, cotovelos virados a este e horizontais para a ultima coluna
    if varCol == len(aPuzzle) - 1:
        validCanos = [x for x in validCanos if x != 'e' and x != 'ne' and x != 'se' and x != 'we' ]
    # Remove pontas viradas a oeste, cotovelos virados a oeste e horizontais para a primeira coluna
    if varCol == 0:
        validCanos = [x for x in validCanos if x != 'w' and x != 'nw' and x != 'sw' and x != 'we' ]
    
    north = aPuzzle[varLine-1][varCol] if varLine > 0 else None
    south = aPuzzle[varLine+1][varCol] if varLine < len(aPuzzle) - 1 else None
    east = aPuzzle[varLine][varCol+1] if varCol < len(aPuzzle) - 1 else None
    west = aPuzzle[varLine][varCol-1] if varCol > 0 else None

    if north != '.' and north != None:
        validCanos = [x for x in validCanos if x != 'n']
    if south != '.' and south != None:
        validCanos = [x for x in validCanos if x != 's']
    if east != '.' and east != None:
        validCanos = [x for x in validCanos if x != 'e']
    if west != '.' and west != None:
        validCanos = [x for x in validCanos if x != 'w']


    # Now that we conputed the valid canos and colors, we can create the domain for each variable
    for color in sorted(validColors):
            for cano in sorted(validCanos):
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
            # if var2 is
            #  north of var1 then cano2 must be ('s', 'ns', 'ne', 'nw')
            if (var2Line < var1Line) and (var2Col == var1Col) :
                if cano2 not in ['s', 'ns', 'se', 'sw'] or color1 != color2:
                    return False
            # if var2 is east of var1 then cano2 must be ('s', 'n', 'ne', 'se')
            if (var2Line == var1Line) and (var2Col > var1Col):
                if cano2 not in ['s', 'n', 'ns', 'ne', 'se', 'e']:
                    return False
            # if var2 is south of var1 then cano2 must be ('n', 'se', 'sw', 'ns')
            if (var2Line > var1Line) and (var2Col == var1Col) :
                if cano2 not in ['n', 'ns', 'ne', 'nw'] or color1 != color2 :
                    return False  
            # if var2 is west of var1 then cano2 must be ('s', 'n', 'ns', 'nw', 'sw')
            if (var2Line == var1Line) and (var2Col < var1Col):
                if cano2 not in ['s', 'n', 'ns', 'nw', 'sw', 'w']:
                    return False
        # When cano1 is we
        if cano1 == 'we':
            # if var2 is north of var1 then cano2 must be ('n', 'w', 'e', 'we', 'se', 'sw)
            if (var2Line < var1Line) and (var2Col == var1Col) :
                if cano2 not in ['n', 'w', 'e', 'we', 'se', 'sw']:
                    return False
            # if var2 is east of var1 then cano2 must be ('w', 'we', 'nw', 'sw')
            if (var2Line == var1Line) and (var2Col > var1Col):
                if cano2 not in ['w', 'we', 'nw', 'sw'] or color1 != color2:
                    return False
            # if var2 is south of var1 then cano2 must be ('w', 'e', 'we', 'ne', 'nw')
            if (var2Line > var1Line) and (var2Col == var1Col):
                if cano2 not in ['s', 'w', 'e', 'we', 'ne', 'nw']:
                    return False
            # if var2 is west of var1 then cano2 must be ('e', 'we', 'ne', 'se')
            if (var2Line == var1Line) and (var2Col < var1Col):
                if cano2 not in ['e', 'we', 'ne', 'se'] or color1 != color2:
                    return False
        # When cano1 is ne
        if cano1 == 'ne':
            # if var2 is north of var1 then cano2 must be ('n', 'w', 'e', 'we', 'se', 'sw')
            if (var2Line < var1Line) and (var2Col == var1Col) :
                if cano2 not in ['s', 'ns', 'se', 'sw'] or color1 != color2:
                    return False
            # if var2 is east of var1 then cano2 must be ('w', 'we', 'nw', 'sw')
            if (var2Line == var1Line) and (var2Col > var1Col):
                if cano2 not in ['w', 'we', 'nw', 'sw'] or color1 != color2:
                    return False
            # if var2 is south of var1 then cano2 must be ('n', 'ns', 'se', 'sw')
            if (var2Line > var1Line) and (var2Col == var1Col):
                if cano2 not in ['s', 'se', 'sw', 'w', 'e', 'we']:
                    return False
            # if var2 is west of var1 then cano2 must be ('s', 'n', 'ns', 'nw', 'sw')
            if (var2Line == var1Line) and (var2Col < var1Col):
                if cano2 not in ['e', 's', 'n', 'ns', 'nw', 'sw']:
                    return False
        # When cano1 is nw
        if cano1 == 'nw':
            # if var2 is north of var1 then cano2 must be ('w', 'e', 'we', 'se', 'sw')
            if (var2Line < var1Line) and (var2Col == var1Col) :
                if cano2 not in ['s', 'ns', 'se', 'sw'] or color1 != color2:
                    return False
            # if var2 is east of var1 then cano2 must be ('s', 'n', 'ns', 'ne', 'se')
            if (var2Line == var1Line) and (var2Col > var1Col):
                if cano2 not in ['e', 's', 'n', 'ns', 'ne', 'se']:
                    return False
            # if var2 is south of var1 then cano2 must be ('n', 'ns', 'se', 'sw')
            if (var2Line > var1Line) and (var2Col == var1Col):
                if cano2 not in ['e', 'w', 's', 'sw', 'se', 'we']:
                    return False
            # if var2 is west of var1 then cano2 must be ('e', 'we', 'ne', 'se')
            if (var2Line == var1Line) and (var2Col < var1Col):
                if cano2 not in ['e', 'we', 'ne', 'se'] or color1 != color2:
                    return False
        # When cano1 is se
        if cano1 == 'se':
            # if var2 is north of var1 then cano2 must be ('s', 'ns', 'ne', 'nw')
            if (var2Line < var1Line) and (var2Col == var1Col):
                if cano2 not in ['e', 'n', 'w', 'ne', 'nw', 'we']:
                    return False
            # if var2 is east of var1 then cano2 must be ('s', 'n', 'ne', 'se')
            if (var2Line == var1Line) and (var2Col > var1Col):
                if cano2 not in ['w', 'we', 'nw', 'sw'] or color1 != color2:
                    return False
            # if var2 is south of var1 then cano2 must be ('n', 'se', 'sw', 'ns')
            if (var2Line > var1Line) and (var2Col == var1Col) :
                if cano2 not in ['n', 'ne', 'nw', 'ns'] or color1 != color2:
                    return False
            # if var2 is west of var1 then cano2 must be ('s', 'n', 'ns', 'nw', 'sw')
            if (var2Line == var1Line) and (var2Col < var1Col):
                if cano2 not in ['nw', 'sw', 'w','ns', 'n', 's']:
                    return False
        # When cano1 is sw
        if cano1 == 'sw':
            # if var2 is north of var1 then cano2 must be ('s', 'ns', 'ne', 'nw')
            if (var2Line < var1Line) and (var2Col == var1Col) :
                if cano2 not in ['ne', 'we', 'ne', 'nw', 'n', 'w', 'e']:
                    return False
            # if var2 is east of var1 then cano2 must be ('s', 'n', 'ne', 'se')
            if (var2Line == var1Line) and (var2Col > var1Col):
                if cano2 not in ['s', 'n', 'e', 'ns', 'ne', 'se']:
                    return False
            # if var2 is south of var1 then cano2 must be ('n', 'se', 'sw', 'ns')
            if (var2Line > var1Line) and (var2Col == var1Col) :
                if cano2 not in ['ne', 'nw', 'n', 'ns'] or color1 != color2:
                    return False
            # if var2 is west of var1 then cano2 must be ('s', 'n', 'ns', 'nw', 'sw')
            if (var2Line == var1Line) and (var2Col < var1Col):
                if cano2 not in ['se', 'we', 'ne', 'e',] or color1 != color2:
                    return False
    
    ##  TERMINALS  ##
    elif len(cano1) == 1:
    
        # When cano1 is N
        if cano1 == 's':
            # if var2 is north of var1 then cano2 must be ('n', 'w', 'e', 'we', 'se', 'sw')
            if (var2Line < var1Line) and (var2Col == var1Col) :
                if cano2 not in ['se', 'sw', 's', 'w', 'e', 'we']:
                    return False
            # if var2 is east of var1 then cano2 must be ('w', 'we', 'nw', 'sw')
            if (var2Line == var1Line) and (var2Col > var1Col):
                if cano2 not in ['ns', 'n', 's', 'se', 'ne', 'e']:
                    return False
            # if var2 is south of var1 then cano2 must be ('w', 'e', 'we', 'ne', 'nw')
            if (var2Line > var1Line) and (var2Col == var1Col) :
                if cano2 not in ['ns', 'ne', 'nw'] or color1 != color2:
                    return False
            # if var2 is west of var1 then cano2 must be ('e', 'we', 'ne', 'se')
            if (var2Line == var1Line) and (var2Col < var1Col):
                if cano2 not in ['s', 'n', 'w', 'ns', 'nw', 'sw']:
                    return False
        # When cano1 is E
        if cano1 == 'w':
            # if var2 is north of var1 then cano2 must be ('n', 'w', 'e', 'we', 'se', 'sw)
            if (var2Line < var1Line) and (var2Col == var1Col) :
                if cano2 not in ['n', 'w', 'e', 'we', 'ne', 'nw']:
                    return False
            # if var2 is east of var1 then cano2 must be ('w', 'we', 'nw', 'sw')
            if (var2Line == var1Line) and (var2Col > var1Col):
                if cano2 not in ['n', 'ne', 'sw', 'ns', 's', 'e']:
                    return False
            # if var2 is south of var1 then cano2 must be ('w', 'e', 'we', 'ne', 'nw')
            if (var2Line > var1Line) and (var2Col == var1Col) :
                if cano2 not in ['s', 'w', 'e', 'we', 'se', 'sw']:
                    return False
            # if var2 is west of var1 then cano2 must be ('e', 'we', 'ne', 'se')
            if (var2Line == var1Line) and (var2Col < var1Col):
                if cano2 not in ['we', 'se', 'ne'] or color1 != color2:
                    return False  
        # When cano1 is S
        if cano1 == 'n':
            # if var2 is north of var1 then cano2 must be ('s', 'ns', 'ne', 'nw')
            if (var2Line < var1Line) and (var2Col == var1Col) :
                if cano2 not in ['ns', 'se', 'sw'] or color1 != color2:
                    return False
            # if var2 is east of var1 then cano2 must be ('s', 'n', 'ne', 'se')
            if (var2Line == var1Line) and (var2Col > var1Col):
                if cano2 not in ['s', 'n', 'e', 'ns', 'ne', 'se']:
                    return False
            # if var2 is south of var1 then cano2 must be ('n', 'se', 'sw', 'ns')
            if (var2Line > var1Line) and (var2Col == var1Col) :
                if cano2 not in ['s', 'w', 'e', 'we', 'se', 'sw']:
                    return False
            # if var2 is west of var1 then cano2 must be ('s', 'n', 'ns', 'nw', 'sw')
            if (var2Line == var1Line) and (var2Col < var1Col):
                if cano2 not in ['s', 'n', 'w', 'ns', 'sw', 'nw']:
                    return False
        # When cano1 is W
        if cano1 == 'e':
            # if var2 is north of var1 then cano2 must be ('n', 'w', 'e', 'we', 'se', 'sw')
            if (var2Line < var1Line) and (var2Col == var1Col) :
                if cano2 not in ['n', 'w', 'e', 'we', 'ne', 'nw']:
                    return False
            # if var2 is east of var1 then cano2 must be ('s', 'n', 'ns', 'ne', 'se')
            if (var2Line == var1Line) and (var2Col > var1Col):
                if cano2 not in ['we', 'nw', 'sw'] or color1 != color2:
                    return False
            # if var2 is south of var1 then cano2 must be ('n', 'ns', 'se', 'sw')
            if (var2Line > var1Line) and (var2Col == var1Col) :
                if cano2 not in ['s', 'w', 'e', 'we', 'se', 'sw']:
                    return False
            # if var2 is west of var1 then cano2 must be ('e', 'we', 'ne', 'se')
            if (var2Line == var1Line) and (var2Col < var1Col):
                if cano2 not in ['s', 'n', 'w', 'ns', 'nw', 'sw']:
                    return False
    return True

def parse_neighbors(v, aPuzzle):
    neighbors = []
    # v is in the form V_X_Y. Extract x and y where Y is the puzzle line (top to bottom= and X is the column (left to right)
    varCol, varLine = map(int, v.split('_')[1:])
    var = aPuzzle[varLine][varCol]
    # extract the value at x, y of the north, south east and west neighbour
    north = aPuzzle[varLine-1][varCol] if varLine > 0 else None
    if north != None and not (north != '.' and var != '.')  :
            neighbors.append(f"V_{varCol}_{varLine-1}")

    south = aPuzzle[varLine+1][varCol] if varLine < len(aPuzzle) - 1 else None
    if( south != None and not(south != '.' and var != '.') ):
        neighbors.append(f"V_{varCol}_{varLine+1}")

    east = aPuzzle[varLine][varCol+1] if varCol < len(aPuzzle) - 1 else None
    if( east != None and not(east != '.' and var != '.')):
        neighbors.append(f"V_{varCol+1}_{varLine}")

    west = aPuzzle[varLine][varCol-1] if varCol > 0 else None
    if( west != None and not(west != '.' and var != '.')):
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
            neighbors[v] = sorted(parse_neighbors(v, aPuzzle))
            domains[v] = parse_domain(v, colors, aPuzzle)
            

    # Ensure each varialble domain is consistent
    #for v in variables:
    #    queue = [(v, Xk) for Xk in neighbors[v]]
    #    while queue:
    #        v1, v2 = queue.pop()
    #        for v1_val in domains[v1]:
    #            if( all( not constraint_function(v1, v1_val, v2, v2_val) for v2_val in domains[v2] )):
    #                domains[v1].remove(v1_val)
                    

    return (variables, domains, neighbors)


def encaixa(var1Tupple, var2Tupple):
    # Canos que encaixam tem de estar virados um para o outro
    (cano1, color1) = var1Tupple
    (cano2, color2) = var2Tupple
    # Pontas nunca encaixam uma na outra
    if len(cano1) == 1 and len(cano2) == 1:
        return False
    # Canos verticais e horizontais nunca encaixam um no outro
    if( cano1 in VERTICAIS and cano2 in HORIZONTAIS or cano1 in HORIZONTAIS and cano2 in VERTICAIS ):
        return False
    
    # cotovelos encaixam em canos que estao virados para o lado oposto ou nos seus correspondentes horizontais ou verticais
    if( (cano1 in COTOVELOS_DIREITA and cano2 in COTOVELOS_ESQUERDA + HORIZONTAIS) or 
         cano1 in COTOVELOS_ESQUERDA and cano2 in COTOVELOS_DIREITA + HORIZONTAIS):
        return True
    if( (cano1 in COTOVELOS_NORTE and cano2 in COTOVELOS_SUL + VERTICAIS) or 
        (cano1 in COTOVELOS_SUL and cano2 in COTOVELOS_NORTE + VERTICAIS) ):
        return True


def contraint_function2(var1, var1Tupple, var2, var2Tupple):
    """# Definicao das restricoes
        - Canos que encaixam tem de ser da mesma cor
        - Canos terminais nao podes estar adjacentes
        - Canos que nao encaixam nao podem ter orientacoes ortogonais"""
    if encaixa(var1Tupple, var2Tupple):
        return true

def CSP_numberlink( puzzle):
    variables, domains, neighbors = numberLinkParsePuzzle(puzzle)
    return CSP(variables, domains, neighbors, constraint_function)



	
try:
    puzzle=[['.','.','.','.','.','.'],
        ['.','.','.','.','.','.'],
        ['.','.','.', 3 ,'.','.'],
        ['.','.','.','.','.','.'],
        ['.','.','.','.', 2 ,'.'],
        [ 2 , 1 , 3 ,'.','.', 1 ]]
    p = CSP_numberlink(puzzle)
    z=AC3(p)
    for v in sorted(p.variables):
        print(v,':',sorted(z.curr_domains[v]))
except Exception as e:
    print(repr(e))

    
"""
try:
    puzzle=[['.','.','.','.','.','.'],
        ['.','.','.','.','.','.'],
        ['.','.','.', 3 ,'.','.'],
        ['.','.','.','.','.','.'],
        ['.','.','.','.', 2 ,'.'],
        [ 2 , 1 , 3 ,'.','.', 1 ]]
    p = CSP_numberlink(puzzle)

    p = CSP_numberlink(puzzle)
    
    # Removing  ('ne', 2) from V_3_5 [('ne', 2)] because of  V_3_4 and  [('ns', 1), ('ns', 2)]
    print(p.constraints('V_3_5',('ne', 2),'V_3_4',('ns', 1)))
    print(p.constraints('V_3_5',('ne', 2),'V_3_4',('ns', 2)))

    z=AC3(p)

    for v in sorted(p.variables):
        print(v,':',sorted(z.curr_domains[v]))
except Exception as e:
    print(repr(e))


"""