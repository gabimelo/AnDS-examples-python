"""
@author Gabriela Melo and Brian Ezra
@since 04/05/2015
@modified 08/05/2015
"""

class Soldier:
	def __init__(self):
		'''
		initialize the object soldier
		@ return: object of this class
		@ complexity: O(1)
		'''
		self.life = 3
		self.experience = 0

	def isAlive(self):
		'''
		returns if this object's life is not 0 or below
		@ return: boolean
		@ complexity:O(1)
		'''
		return (self.life > 0)

	def loseLife(self, lostLife):
		'''
		reduce life of the object of this class
		@ param lostLife: integer, positive
		@ return: error if lostlife not positive or is not a number
		@ complexity: O(1)
		'''
		try:
			lostLife = int(lostLife)
		except ValueError:
			print("Life lost should be a number")
			raise

		assert lostLife > 0, "Life must be positive"

		self.life -= lostLife

	def gainExperience(self, gainedExperience):
		'''
		increase this object's experience based on value given on argument
		@ param gainedExperience: integer, positive
		@ return: error if argument not integer or not positive
		@ complexity: O(1)
		'''
		try:
			gainedExperience = int(gainedExperience)
		except ValueError:
			print("Gained experience should be a number")
			raise

		assert gainedExperience > 0, "Gained experience must be positive"

		self.experience += gainedExperience

	def getCost(self):
		'''
		returns the cost of this object
		@ return: 1
		@ complexity: O(1)
		'''
		return 1

	def getSpeed(self):
		'''
		returns the speed of this object
		@ return: integer, positive
		@ complexity: O(1)
		'''
		return 1+self.experience

	def attack(self):
		'''
		returns the damage done by this object
		@ return: integer, positive
		@ complexity: O(1)
		'''
		return 1+self.experience

	def defend(self, damage):
		'''
		reduce life based on damage taken
		@ param damage: integer, positive
		@ return: None
		@ complexity: O(1)
		'''
		try:
			damage = int(damage)
		except ValueError:
			print("Damage should be a number")
			raise

		if damage > self.experience:
			lostLife = 1
			self.loseLife(lostLife)

	def __str__(self):
		'''
		prints the details of this object
		@ return: string
		@ complexity: O(1)
		'''
		return ("\n\nThis unit is of type Soldier, \nits current life is " + str(self.life) + " \nand its experience is " + str(self.experience))

class Archer:
	def __init__(self):
		'''
		initialize the object Archer
		@ return: object of this class
		@ complexity: O(1)
		'''
		self.life = 3
		self.experience = 0

	def isAlive(self):
		'''
		returns if this object's life is not 0 or below
		@ return: boolean
		@ complexity:O(1)
		'''
		return (self.life > 0)

	def loseLife(self, lostLife):
		'''
		reduce life of the object of this class
		@ param lostLife: integer, positive
		@ return: error if lostlife not positive or is not a number
		@ complexity: O(1)
		'''
		try:
			lostLife = int(lostLife)
		except ValueError:
			print("Life lost should be a number")
			raise

		assert lostLife > 0, "Life must be positive"

		self.life -= lostLife

	def gainExperience(self, gainedExperience):
		'''
		increase this object's experience based on value given on argument
		@ param gainedExperience: integer, positive
		@ return: error if argument not integer or not positive
		@ complexity: O(1)
		'''
		try:
			gainedExperience = int(gainedExperience)
		except ValueError:
			print("Gained experience should be a number")
			raise

		assert gainedExperience > 0, "Gained experience must be positive"

		self.experience += gainedExperience

	def getCost(self):
		'''
		returns the cost of this object
		@ return: 2
		@ complexity: O(1)
		'''
		return 2

	def getSpeed(self):
		'''
		returns the speed of this object
		@ return: integer, positive
		@ complexity: O(1)
		'''
		return 3

	def attack(self):
		'''
		returns the damage done by this object
		@ return: integer, positive
		@ complexity: O(1)
		'''
		return 1+self.experience

	def defend(self, damage):
		'''
		reduce life based on damage taken
		@ param damage: integer, positive
		@ return: None
		@ complexity: O(1)
		'''
		try:
			damage = int(damage)
		except ValueError:
			print("Damage should be a number")
			raise

		lostLife = 1
		self.loseLife(lostLife)

	def __str__(self):
		'''
		prints the details of this object
		@ return: string
		@ complexity: O(1)
		'''
		return ("\n\nThis unit is of type Archer, \nits current life is " + str(self.life) + " \nand its experience is " + str(self.experience))
               
class Cavalry:
	def __init__(self):
		'''
		initialize the object Cavalry
		@ return: object of this class
		@ complexity: O(1)
		'''
		self.life = 4
		self.experience = 0

	def isAlive(self):
		'''
		returns if this object's life is not 0 or below
		@ return: boolean
		@ complexity:O(1)
		'''
		return (self.life > 0)

	def loseLife(self, lostLife):
		'''
		reduce life of the object of this class
		@ param lostLife: integer, positive
		@ return: error if lostlife not positive or is not a number
		@ complexity: O(1)
		'''
		try:
			lostLife = int(lostLife)
		except ValueError:
			print("Life lost should be a number")
			raise

		assert lostLife > 0, "Life must be positive"

		self.life -= lostLife

	def gainExperience(self, gainedExperience):
		'''
		increase this object's experience based on value given on argument
		@ param gainedExperience: integer, positive
		@ return: error if argument not integer or not positive
		@ complexity: O(1)
		'''
		try:
			gainedExperience = int(gainedExperience)
		except ValueError:
			print("Gained experience should be a number")
			raise

		assert gainedExperience > 0, "Gained experience must be positive"

		self.experience += gainedExperience

	def getCost(self):
		'''
		returns the cost of this object
		@ return: 2
		@ complexity: O(1)
		'''
		return 3

	def getSpeed(self):
		'''
		returns the speed of this object
		@ return: integer, positive
		@ complexity: O(1)
		'''
		return 2

	def attack(self):
		'''
		returns the damage done by this object
		@ return: integer, positive
		@ complexity: O(1)
		'''
		return 1+2*self.experience

	def defend(self, damage):
		'''
		reduce life based on damage taken
		@ param damage: integer, positive
		@ return: None
		@ complexity: O(1)
		'''
		try:
			damage = int(damage)
		except ValueError:
			print("Damage should be a number")
			raise

		if damage > self.experience/2:
			lostLife = 1
			self.loseLife(lostLife)

	def __str__(self):
		'''
		prints the details of this object
		@ return: string
		@ complexity: O(1)
		'''
		return ("\n\nThis unit is of type Cavalry, \nits current life is " + str(self.life) + " \nand its experience is " + str(self.experience))
		

def menu():
	quit = False
	while not quit:
		objects = [1, 2, 3, 4]
		print(	'''
			1. Soldier
			2. Archer
			3. Cavalry
			4. quit
			
				''')
		try:
			command = int(input('input object type: '))
			if not command in objects:
				raise ValueError
		except (ValueError, TypeError):
			print('unknown command, try again')
		if command == 1:
			fighter = Soldier()
		elif command == 2:
			fighter = Archer()
		elif command == 3:
			fighter = Cavalry()
		elif command == 4:
			quit = True
		if command != 4:
			menu2(fighter)

def menu2(fighter):
	quit = False
	while not quit:
		commands = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
		print(	'''
			1. isAlive
			2. loseLife
			3. gainExperience
			4. getCost
			5. getSpeed
			6. attack
			7. defend
			8. __str__
			9. reset
			0. quit/ change fighter
				''')
		try:
			command = int(input('input command type: '))
			if not command in commands:
				raise ValueError
		except (ValueError, TypeError):
			print('unknown command, try again')

		if command == 1:
			if fighter.isAlive():
				print("Fighter is alive")
			else:
				print("Fighter is dead")
		elif command == 2:
			lostLife = input("Enter amount of life lost: ")
			try:
				fighter.loseLife(lostLife)
			except (AssertionError, ValueError):
				print("Could not proceed with function")

		elif command == 3:
			gainedExperience = input("Enter amount of experience gained: ")
			try:
				fighter.gainExperience(gainedExperience)
			except (AssertionError, ValueError):
				print("Could not proceed with function")
		elif command == 4:
			print("Cost of fighter is: " + str(fighter.getCost()))
		elif command == 5:
			print("Speed of fighter is: " + str(fighter.getSpeed()))
		elif command == 6:
			print("This fighter performs " + str(fighter.attack()) + " damage")
		elif command == 7:
			damage = input("Enter amount of damage")
			try:
				fighter.defend(damage)
			except ValueError:
				print("Could not proceed with function")
		elif command == 8:
			print(str(fighter))
		elif command == 9:
			fighter.__init__()
		elif command == 0:
			quit = True

if __name__ == '__main__':
	menu()
