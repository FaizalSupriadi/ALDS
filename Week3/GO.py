import random_player
import gomoku

class playerMe:
	def __init__(self, black_=True):
        """Constructor for the player."""
        self.black = black_

    def new_game(self, black_):
        """At the start of each new game you will be notified by the competition.
        this method has a boolean parameter that informs your agent whether you
        will play black or white.
        """
        self.black = black_

    def move(self, board, last_move, valid_moves, max_time_to_move=1000):
        """This is the most important method: the agent will get:
        1) the current state of the board
        2) the last move by the opponent
        3) the available moves you can play (this is a special service we provide ;-) )
        4) the maximimum time until the agent is required to make a move in milliseconds [diverging from this will lead to disqualification].
        """
        return random.choice(valid_moves)

    def id(self):
        """Please return a string here that uniquely identifies your submission e.g., "name (student_id)" """
        return "Faizal(1735666)"

class node:
	def __init__(self, data=None,):
		self.parent = None
		self.children = []
		self.Q = data
		self.N = 0

class tree:

	def __init__(self):
		self.head= None
		
	def append(self, child):
		if self.head == None:
			self.head = node(child)
		newNode = node(child)
		self.newNode.parent = self.head
		self.head.children.append(newNode)
		
	def highest(self):
		high = []
		for i in self.head.children.Q:
			high.append(i)
		return max(high)

def FindSpotToExpand(root):
	if len(root.valid_moves()) <=0:
		return root
	if len(root.children()) < len(root.valid_moves()):
		newNode = node(random.choice(root.valid_moves()))
		root.append(node(random.choice(root.valid_moves())))
		newNode = root.highest()
	return FindSpotToExpand(newNode)

def rollout(leaf):
	while !leaf.is_terminal():
		a = random_player.move(random.choice(valid_moves))
		leaf = new game
	return result

def BackupValue( leaf, node ):
	while node is not null:
		node.N+=1
		if node%2 == 0:
			node.Q = node.Q - leaf
		else:
			node.Q = node.Q + leaf
		node = node.parent
			
def UCT(state):
	root = tree.append(node(state)) #gomoku.current_board()
	 start_time = time.time_ns()
	 stop_time = 0
	while stop_time>= 19999:
		
		leaf = FindSpotToExpand(root)
		val = rollout(leaf)
		BackupValue(leaf,val)
		stop_time = time.time_ns()
	return best move
					
UCT(gomoku.current_board())