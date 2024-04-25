from SI_proj3_XX import CSP_numberlink

def runTest2 () :
    puzzle=[['.','.','.','.','.','.'],
        ['.','.','.','.','.','.'],
        ['.','.','.', 3 ,'.','.'],
        ['.','.','.','.','.','.'],
        ['.','.','.','.', 2 ,'.'],
        [ 2 , 1 , 3 ,'.','.', 1 ]]
    puzzleExpectedVariables = ['V_0_0', 'V_0_1', 'V_0_2', 'V_0_3', 'V_0_4', 'V_0_5', 'V_1_0', 'V_1_1', 'V_1_2', 'V_1_3', 'V_1_4', 'V_1_5', 'V_2_0', 'V_2_1', 'V_2_2', 'V_2_3', 'V_2_4', 'V_2_5', 'V_3_0', 'V_3_1', 'V_3_2', 'V_3_3', 'V_3_4', 'V_3_5', 'V_4_0', 'V_4_1', 'V_4_2', 'V_4_3', 'V_4_4', 'V_4_5', 'V_5_0', 'V_5_1', 'V_5_2', 'V_5_3', 'V_5_4', 'V_5_5']
    expectedPuzzleDomains = \
    {'V_0_0' : [('se', 1), ('se', 2), ('se', 3)],
    'V_0_1' : [('ne', 1), ('ne', 2), ('ne', 3), ('ns', 1), ('ns', 2), ('ns', 3)],
    'V_0_2' : [('ne', 1), ('ne', 2), ('ne', 3), ('ns', 1), ('ns', 2), ('ns', 3)],
    'V_0_3' : [('ne', 1), ('ne', 2), ('ne', 3), ('ns', 1), ('ns', 2), ('ns', 3)],
    'V_0_4' : [('ne', 1), ('ne', 2), ('ne', 3), ('ns', 1), ('ns', 2), ('ns', 3)],
    'V_0_5' : [('n', 2)],
    'V_1_0' : [('se', 1), ('se', 2), ('se', 3), ('sw', 1), ('sw', 2), ('sw', 3), ('we', 1), ('we', 2), ('we', 3)],
    'V_1_1' : [('ne', 1), ('ne', 2), ('ne', 3), ('ns', 1), ('ns', 2), ('ns', 3), ('nw', 1), ('nw', 2), ('nw', 3), ('se', 1), ('se', 2), ('se', 3), ('sw', 1), ('sw', 2), ('sw', 3), ('we', 1), ('we', 2), ('we', 3)],
    'V_1_2' : [('ne', 1), ('ne', 2), ('ne', 3), ('ns', 1), ('ns', 2), ('ns', 3), ('nw', 1), ('nw', 2), ('nw', 3), ('se', 1), ('se', 2), ('se', 3), ('sw', 1), ('sw', 2), ('sw', 3), ('we', 1), ('we', 2), ('we', 3)],
    'V_1_3' : [('ne', 1), ('ne', 2), ('ne', 3), ('ns', 1), ('ns', 2), ('ns', 3), ('nw', 1), ('nw', 2), ('nw', 3), ('se', 1), ('se', 2), ('se', 3), ('sw', 1), ('sw', 2), ('sw', 3), ('we', 1), ('we', 2), ('we', 3)],
    'V_1_4' : [('ne', 1), ('ne', 2), ('ne', 3), ('ns', 1), ('ns', 2), ('ns', 3), ('nw', 1), ('nw', 2), ('nw', 3), ('se', 1), ('se', 2), ('se', 3), ('sw', 1), ('sw', 2), ('sw', 3), ('we', 1), ('we', 2), ('we', 3)],
    'V_1_5' : [('n', 1)],
    'V_2_0' : [('se', 1), ('se', 2), ('se', 3), ('sw', 1), ('sw', 2), ('sw', 3), ('we', 1), ('we', 2), ('we', 3)],
    'V_2_1' : [('ne', 1), ('ne', 2), ('ne', 3), ('ns', 1), ('ns', 2), ('ns', 3), ('nw', 1), ('nw', 2), ('nw', 3), ('se', 1), ('se', 2), ('se', 3), ('sw', 1), ('sw', 2), ('sw', 3), ('we', 1), ('we', 2), ('we', 3)],
    'V_2_2' : [('ne', 1), ('ne', 2), ('ne', 3), ('ns', 1), ('ns', 2), ('ns', 3), ('nw', 1), ('nw', 2), ('nw', 3), ('se', 1), ('se', 2), ('se', 3), ('sw', 1), ('sw', 2), ('sw', 3), ('we', 1), ('we', 2), ('we', 3)],
    'V_2_3' : [('ne', 1), ('ne', 2), ('ne', 3), ('ns', 1), ('ns', 2), ('ns', 3), ('nw', 1), ('nw', 2), ('nw', 3), ('se', 1), ('se', 2), ('se', 3), ('sw', 1), ('sw', 2), ('sw', 3), ('we', 1), ('we', 2), ('we', 3)],
    'V_2_4' : [('ne', 1), ('ne', 2), ('ne', 3), ('ns', 1), ('ns', 2), ('ns', 3), ('nw', 1), ('nw', 2), ('nw', 3), ('se', 1), ('se', 2), ('se', 3), ('sw', 1), ('sw', 2), ('sw', 3), ('we', 1), ('we', 2), ('we', 3)],
    'V_2_5' : [('e', 3), ('n', 3)],
    'V_3_0' : [('se', 1), ('se', 2), ('se', 3), ('sw', 1), ('sw', 2), ('sw', 3), ('we', 1), ('we', 2), ('we', 3)],
    'V_3_1' : [('ne', 1), ('ne', 2), ('ne', 3), ('ns', 1), ('ns', 2), ('ns', 3), ('nw', 1), ('nw', 2), ('nw', 3), ('se', 1), ('se', 2), ('se', 3), ('sw', 1), ('sw', 2), ('sw', 3), ('we', 1), ('we', 2), ('we', 3)],
    'V_3_2' : [('e', 3), ('n', 3), ('s', 3), ('w', 3)],
    'V_3_3' : [('ne', 1), ('ne', 2), ('ne', 3), ('ns', 1), ('ns', 2), ('ns', 3), ('nw', 1), ('nw', 2), ('nw', 3), ('se', 1), ('se', 2), ('se', 3), ('sw', 1), ('sw', 2), ('sw', 3), ('we', 1), ('we', 2), ('we', 3)],
    'V_3_4' : [('ne', 1), ('ne', 2), ('ne', 3), ('ns', 1), ('ns', 2), ('ns', 3), ('nw', 1), ('nw', 2), ('nw', 3), ('se', 1), ('se', 2), ('se', 3), ('sw', 1), ('sw', 2), ('sw', 3), ('we', 1), ('we', 2), ('we', 3)],
    'V_3_5' : [('ne', 1), ('ne', 2), ('ne', 3), ('nw', 1), ('nw', 2), ('nw', 3), ('we', 1), ('we', 2), ('we', 3)],
    'V_4_0' : [('se', 1), ('se', 2), ('se', 3), ('sw', 1), ('sw', 2), ('sw', 3), ('we', 1), ('we', 2), ('we', 3)],
    'V_4_1' : [('ne', 1), ('ne', 2), ('ne', 3), ('ns', 1), ('ns', 2), ('ns', 3), ('nw', 1), ('nw', 2), ('nw', 3), ('se', 1), ('se', 2), ('se', 3), ('sw', 1), ('sw', 2), ('sw', 3), ('we', 1), ('we', 2), ('we', 3)],
    'V_4_2' : [('ne', 1), ('ne', 2), ('ne', 3), ('ns', 1), ('ns', 2), ('ns', 3), ('nw', 1), ('nw', 2), ('nw', 3), ('se', 1), ('se', 2), ('se', 3), ('sw', 1), ('sw', 2), ('sw', 3), ('we', 1), ('we', 2), ('we', 3)],
    'V_4_3' : [('ne', 1), ('ne', 2), ('ne', 3), ('ns', 1), ('ns', 2), ('ns', 3), ('nw', 1), ('nw', 2), ('nw', 3), ('se', 1), ('se', 2), ('se', 3), ('sw', 1), ('sw', 2), ('sw', 3), ('we', 1), ('we', 2), ('we', 3)],
    'V_4_4' : [('e', 2), ('n', 2), ('s', 2), ('w', 2)],
    'V_4_5' : [('ne', 1), ('ne', 2), ('ne', 3), ('nw', 1), ('nw', 2), ('nw', 3), ('we', 1), ('we', 2), ('we', 3)],
    'V_5_0' : [('sw', 1), ('sw', 2), ('sw', 3)],
    'V_5_1' : [('ns', 1), ('ns', 2), ('ns', 3), ('nw', 1), ('nw', 2), ('nw', 3), ('sw', 1), ('sw', 2), ('sw', 3)],
    'V_5_2' : [('ns', 1), ('ns', 2), ('ns', 3), ('nw', 1), ('nw', 2), ('nw', 3), ('sw', 1), ('sw', 2), ('sw', 3)],
    'V_5_3' : [('ns', 1), ('ns', 2), ('ns', 3), ('nw', 1), ('nw', 2), ('nw', 3), ('sw', 1), ('sw', 2), ('sw', 3)],
    'V_5_4' : [('ns', 1), ('ns', 2), ('ns', 3), ('nw', 1), ('nw', 2), ('nw', 3), ('sw', 1), ('sw', 2), ('sw', 3)],
    'V_5_5' : [('n', 1), ('w', 1)]}

    p = CSP_numberlink(puzzle)
    for v in sorted(p.variables):
        print(v,':',sorted(p.domains[v]))
        sortedDomains = sorted(p.domains[v], key=lambda x: (x[0], x[1]))
        sortedExtectedDomains = sorted(expectedPuzzleDomains[v], key=lambda x: (x[0], x[1]))
        message = f"Domain \n{sortedDomains} for variable {v} is not as expected \n{sortedExtectedDomains}"
        assert sortedDomains == sortedExtectedDomains , message
    print('Test 2 passed')

def puzzle2TestDetails () :
    puzzle2=[['.','.','.','.','.','.'],
        ['.','.','.','.','.','.'],
        ['.','.','.', 3 ,'.','.'],
        ['.','.','.','.','.','.'],
        ['.','.','.','.', 2 ,'.'],
        [ 2 , 1 , 3 ,'.','.', 1 ]]
    
    puzzle1ExpectedVariables = ['V_0_0', 'V_0_1', 'V_0_2', 'V_0_3', 'V_0_4', 'V_0_5', 'V_1_0', 'V_1_1', 'V_1_2', 'V_1_3', 'V_1_4', 'V_1_5', 'V_2_0', 'V_2_1', 'V_2_2', 'V_2_3', 'V_2_4', 'V_2_5', 'V_3_0', 'V_3_1', 'V_3_2', 'V_3_3', 'V_3_4', 'V_3_5', 'V_4_0', 'V_4_1', 'V_4_2', 'V_4_3', 'V_4_4', 'V_4_5', 'V_5_0', 'V_5_1', 'V_5_2', 'V_5_3', 'V_5_4', 'V_5_5']
    #expectedPuzzle1Domains = 

runTest2()

"""
puzzle=[['.','.','.','.','.','.'],
        ['.','.','.','.','.','.'],
        ['.','.','.', 3 ,'.','.'],
        ['.','.','.','.','.','.'],
        ['.','.','.','.', 2 ,'.'],
        [ 2 , 1 , 3 ,'.','.', 1 ]]
puzzle_display(puzzle)
p = CSP_numberlink(puzzle)
r = backtracking_search(p, verbose = True)

print('V_2_4:', p.curr_domains['V_2_4'])

new_puzzle=puzzle_resolvido(puzzle,r)

puzzle_display(new_puzzle)

exit()

puzzle=[['.','.','.','.','.','.'],
        ['.','.','.','.','.','.'],
        ['.','.','.', 3 ,'.','.'],
        ['.','.','.','.','.','.'],
        ['.','.','.','.', 2 ,'.'],
        [ 2 , 1 , 3 ,'.','.', 1 ]]
p = CSP_numberlink(puzzle)
print(p.constraints('V_1_0',('se',1),'V_2_0',('we',2)))
"""
exit()

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

puzzle1, puzzle1ExpectedVariables, expectedPuzzle1Domains = puzzle1TestDetails()
puzzle_display(puzzle1)
numberLinkCSP = CSP_numberlink(puzzle1)
assert sorted(numberLinkCSP.variables) == sorted(puzzle1ExpectedVariables)
for v in sorted(numberLinkCSP.variables) :
    print("Parsed: ", v, sorted(numberLinkCSP.domains[v]))
    print("Expecd: ", v, sorted(expectedPuzzle1Domains[v]))
    assert sorted(numberLinkCSP.domains[v]) == sorted(expectedPuzzle1Domains[v])

