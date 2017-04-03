"""
@author Gabriela Melo and Brian Ezra
@since 04/05/2015
@modified 08/05/2015
"""

class Army:
    def __init__(self, name, soldiers, archers, cavalries):
        '''
        creates an Army class that uses Stack
        @ param name: string for the Army's name
        @ param soldiers: integer, positive
        @ param archers: integer, positive
        @ param cavalries: integer, positive
        @ post: Army class created
        @ return: Army class
        @ complexity: O(1) -> because soldiers, archers, cavalries though varies, have maximum
        '''
        self.name = name
        self.money = 20

        try:
            (soldiers, archers, cavalries) = self._verifyInput(soldiers, archers, cavalries)
        except (ValueError, AssertionError):
            raise

        try:
            self.money -= self.calculateMoney(soldiers, archers, cavalries)
        except AssertionError:
            raise

        self.createStack(soldiers, archers, cavalries)

    def _verifyInput(self, soldiers, archers, cavalries):
        '''
        verifies the user inputted values for soldiers, archers, and cavalry
        @ param soldiers: integer, at least 0
        @ param archers: integer, at least 0
        @ param cavalries: integer, at least 0
        @ pre: Army class
        @ return: error if any of the parameter is(are) not in the above^ condition
        @ complexity: O(1)
        '''
        try:
            soldiers = int(soldiers)
        except ValueError:
            print("Soldiers should be a number")
            raise
        assert soldiers >= 0, "Soldiers must be positive"

        try:
            archers = int(archers)
        except ValueError:
            print("Archers should be a number")
            raise
        assert archers >= 0, "Archers must be positive"

        try:
            cavalries = int(cavalries)
        except ValueError:
            print("Cavalries should be a number")
            raise
        assert cavalries >= 0, "Cavalries must be positive"

        return (soldiers, archers, cavalries)

    def calculateMoney(self, soldiers, archers, cavalries):
        '''
        makes sure that player does not spend more than 20$
        @ param soldiers: integer => 0
        @ param archers: integer => 0
        @ param cavalries: integer => 0
        @ pre: param verified are integer => 0, Army class
        @ return: integer => 0
        @ complexity: O(1)
        '''
        import fighter

        soldierMoney = fighter.Soldier().getCost()*soldiers
        archerMoney = fighter.Archer().getCost()*archers
        cavalryMoney = fighter.Cavalry().getCost()*cavalries

        moneySpent = soldierMoney + archerMoney + cavalryMoney

        assert moneySpent <= self.money, "Can't spend more than 20 dollars"

        return moneySpent

    def createStack(self, soldiers, archers, cavalries):
        '''
        creates an object of the Stack class and pushes one or all 3 of the fighter classes based on user input
        @ param soldiers: integer => 0
        @ param archers: integer => 0
        @ param cavalries: integer => 0
        @ pre: param all verified, Army class
        @ post: an object of Stack class is created and filled with object(s) of another class
        @ return: None
        @ complexity: O(1)
        '''
        import fighter
        import stack
        self.my_army = stack.Stack(20)

        for _ in range(cavalries):
            self.my_army.push(fighter.Cavalry())
        for _ in range(archers):
            self.my_army.push(fighter.Archer())
        for _ in range(soldiers):
            self.my_army.push(fighter.Soldier())

def gladitorialCombat(Player1_army, Player2_army):
    '''
    pops 1 unit from each player's army and make them fight each other until one of them or both is empty
    @ param Player1_army: an instance of the army class
    @ param Player2_army: an instance of the army class
    @ post: either or both army objects empty
    @ return: string indicating which stack of the army object is not empty (who won)
    @ complexity:O(1)
    '''
    while not Player1_army.my_army.is_empty() and not Player2_army.my_army.is_empty():
        U1 = Player1_army.my_army.pop()
        U2 = Player2_army.my_army.pop()

        battle(U1, U2)

        endBattle(Player1_army, Player2_army, U1, U2)

    displayResult(Player1_army, Player2_army)

def battle(U1, U2):
    '''
    called from gladiatorialCombat and using methods from each of U1 and U2,  make those units attack each other
    @ param U1: an instance of one of the fighter class
    @ param U2: an instance of one of the fighter class
    @ return: None
    @ complexity: O(1)
    '''
    if U1.getSpeed() > U2.getSpeed():
        U2.defend(U1.attack())
        if U2.isAlive():
            U1.defend(U2.attack())

    elif U1.getSpeed() == U2.getSpeed():
        U2.defend(U1.attack())
        U1.defend(U2.attack())

    elif U1.getSpeed() < U2.getSpeed():
        U1.defend(U2.attack())
        if U1.isAlive():
            U2.defend(U1.attack())

def test_battle():
    import fighter
    correct = True
    U1 = fighter.Soldier()
    U2 = fighter.Soldier()
    for _ in range(2):
        battle(U1, U2)
        if not U1.isAlive() or not U2.isAlive():
            correct = False
    battle(U1, U2)
    if U1.isAlive() or U2.isAlive():
        correct = False

    U1 = fighter.Soldier()
    U2 = fighter.Archer()
    for _ in range(2):
        battle(U1, U2)
        if not U1.isAlive() or not U2.isAlive():
            correct = False
    battle(U1, U2)
    if U1.isAlive() or not U2.isAlive():
        correct = False

    U1 = fighter.Archer()
    U2 = fighter.Cavalry()
    for _ in range(2):
        battle(U1, U2)
        if not U1.isAlive() or not U2.isAlive():
            correct = False
    battle(U1, U2)
    if U1.isAlive() or not U2.isAlive():
        correct = False

    return correct

def endBattle(Player1_army, Player2_army, U1, U2):
    ''' 
    pushes back units into the army stack if they are still alive
    @ param Player1_army: an instance of the army class
    @ param Player2_army: an instance of the army class
    @ post: might change the stack of any army
    @ return: None
    @ complexity: O(1)
    '''
    if U1.isAlive() and U2.isAlive():
        U1.loseLife(1)
        U2.loseLife(1)
        Player1_army.my_army.push(U1)
        Player2_army.my_army.push(U2)
    else:
        if U1.isAlive():
            U1.gainExperience(1)
            Player1_army.my_army.push(U1)
        elif U2.isAlive():
            U2.gainExperience(1)
            Player2_army.my_army.push(U2)

def test_endBattle():
    import fighter
    correct = True
    Player1_army = Army('name', 0, 0, 0)
    Player2_army = Army('name', 0, 0, 0)
    U1 = fighter.Soldier()
    U2 = fighter.Soldier()
    endBattle(Player1_army, Player2_army, U1, U2)
    a_string = "\n\nThis unit is of type Soldier, \nits current life is 2 \nand its experience is 0"
    if str(U1) != a_string or str(U2) != a_string:
        correct = False
    if U1 != Player1_army.my_army.pop() or U2 != Player2_army.my_army.pop():
        correct = False

    U2.loseLife(2)
    endBattle(Player1_army, Player2_army, U1, U2)
    a_string = "\n\nThis unit is of type Soldier, \nits current life is 2 \nand its experience is 1"
    if str(U1) != a_string:
        correct = False
    if U1 != Player1_army.my_army.pop():
        correct = False

    U1.loseLife(2)
    U2 = fighter.Archer()
    endBattle(Player1_army, Player2_army, U1, U2)
    a_string = "\n\nThis unit is of type Archer, \nits current life is 3 \nand its experience is 1"
    if str(U2) != a_string:
        correct = False
    if U2 != Player2_army.my_army.pop():
        correct = False

    return correct

def displayResult(Player1_army, Player2_army):
    '''
    decides who won the game by looking at each players' stacks and then print the units left in that stack
    @ param Player1_army: an instance of the army class
    @ param Player2_army: an instance of the army class
    @ return: prints the game results
    @ complexity: O(n) where n is stack length of the army class
    '''
    if not Player1_army.my_army.is_empty():
        print("Player 1 won")
        print(str(Player1_army.my_army))
    elif not Player2_army.my_army.is_empty():
        print("Player 2 won")
        print(str(Player2_army.my_army))
    else:
        print("Game is a draw")

def test_army():
    correct = True

    test1 = Army("army1", 20, 0, 0)
    if test1.name != "army1":
        correct = False
    if test1.money != 0:
        correct = False
    for _ in range(20):
        item = test1.my_army.pop()
        if item.getCost() != 1:
            correct = False

    try:
        test2 = Army("army2", 0, -20, 0)
        correct = False
    except AssertionError:
        correct = True

    test3 = Army("army3", 5, 3, 3)
    for _ in range(5):
        item = test3.my_army.pop()
        if item.getCost() != 1:
            correct = False
    for _ in range(3):
        item = test3.my_army.pop()
        if item.getCost() != 2:
            correct = False
    for _ in range(3):
        item = test3.my_army.pop()
        if item.getCost() != 3:
            correct = False

    try:
        test4 = Army("army4", 0, 0, "s")
        correct = False
    except ValueError:
        correct = True

    try:
        test5 = Army("army5", 0, 20, 0)
        correct = False
    except AssertionError:
        correct = True

    return correct

if __name__ == '__main__':

  possible = False
  while not possible:
      name = input("\nPlease enter name for Player 1: ")
      soldiers = input("Enter amount of soldiers: ")
      archers = input("Enter amount of archers: ")
      cavalries = input("Enter amount of cavalry: ")
      try:
          player1 = Army(name, soldiers, archers, cavalries)
          possible = True
      except (AssertionError, ValueError):
          print("Please try again")

  possible = False
  while not possible:
      name = input("\nPlease enter name for Player 2: ")
      soldiers = input("Enter amount of soldiers: ")
      archers = input("Enter amount of archers: ")
      cavalries = input("Enter amount of cavalry: ")
      try:
          player2 = Army(name, soldiers, archers, cavalries)
          possible = True
      except (AssertionError, ValueError):
          print("Please try again")

  gladitorialCombat(player1, player2)
