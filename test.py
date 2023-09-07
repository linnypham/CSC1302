class Location:
    def __init__(self, x, y): #TODO: Implement the Location class according to the given UML class diagram and descriptions
        self.x = x
        self.y = y
    def __str__(self):
        return '({},{})'.format(self.x,self.y)

location1 = Location(2,1)

print(location1)