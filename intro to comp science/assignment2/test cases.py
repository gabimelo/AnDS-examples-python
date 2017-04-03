test cases

Task 2:

my_list = []
menu = 1
     1
     my_list = ['1']
menu = 1
     3
     my_list = ['1', '3']


menu = 2
    my_list = [ 2, 3, 4]

my_list = [3, 3, 3]
menu = 2
    my_list = [ 3, 3, 3]
     
menu = 3
    [ '3', '3', '3']

menu = 4
    my_list = []

my_list = [3, 2, 4]
menu = 5
    my_list = [ 4, 3, 2]

my_list = [ 2, 3, 4]
menu = 5
    my_list = [ 4, 3, 2]

my_list = [ 2, 3, 4]
menu = 6
    [ '2', '3']
menu = 6
    [ '2']

menu = 7
    1

menu = 8
item = 1
position = 1
my_list = [1, 2]

menu = 8
item = 3
position = 3
my_list = [1, 2, 3]

menu = 9
item = 3
    2

my_list = [1, 1, 1]
menu = 9
item = 1
     0

Task 3:

puzzle = [[' 1', ' 2', ' 3', ' 4'],
          [' 5', ' 6', ' 7', ' 8'], 
          [' 9', '10', '11', '12'], 
          ['13', '14', '15', ' X']]
    menu = u
    [[' 1', ' 2', ' 3', ' 4'],
    [' 5', ' 6', ' 7', ' 8'], 
    [' 9', '10', '11', ' X'], 
    ['13', '14', '15', '12']]

    menu = d
    Invalid movement

    menu = l
    [[' 1', ' 2', ' 3', ' 4'],
    [' 5', ' 6', ' 7', ' 8'], 
    [' 9', '10', '11', '12'], 
    ['13', '14', ' X', '15']]

    menu = r
    Invalid movement

puzzle = [[' X', ' 2', ' 3', ' 4'],
          [' 5', ' 6', ' 7', ' 8'], 
          [' 9', '10', '11', '12'], 
          [' 13', '14', '15', ' 1']]

    menu = u
    Invalid movement

    menu = d
    [[' 5', ' 2', ' 3', ' 4'],
    [' X', ' 6', ' 7', ' 8'], 
    [' 9', '10', '11', '12'], 
    [' 13', '14', '15', ' 1']]

    menu = l
    Invalid movement

    menu = r
    [[' 2', ' X', ' 3', ' 4'],
    [' 5', ' 6', ' 7', ' 8'], 
    [' 9', '10', '11', '12'], 
    [' 13', '14', '15', ' 1']]
