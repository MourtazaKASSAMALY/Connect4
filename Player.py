class Player :
	def __init__(self, color, name=""):
		"""
    Params:
    	color : int 
    		0 : Red; 1 : Yellow
      name : str
      	Name of the player, if left empty the computer is the player.
  	"""
		self.color = int(color)  # yellow or red
    self.name = str(name)
		self.computer = bool(name=="")  # if no name, then it is the computer
		if name == "": 
    	self.name = "Computer"
    self.nb_wins = int(0)  # count the number of wins