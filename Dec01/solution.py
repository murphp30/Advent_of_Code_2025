class Dial:
    """Class to update dial position"""
    def __init__(self):
        self._position = 50
        self._nnotches = 100
        self.npasses = 0
    
    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        self._position = value

    def update_position(self, instruction):
        direction = instruction[0]
        distance = int(instruction[1:])
        self.npasses += distance//self._nnotches
        if direction == "L":
            if (self.position != 0) and (self.position - distance%self._nnotches) <= 0:
                self.npasses +=1
            self.position = (self.position - distance)%self._nnotches

        elif direction == "R":
            if (self.position != 0) and (self.position + (distance%self._nnotches)) >= self._nnotches:
                self.npasses +=1
            self.position = (self.position + distance)%self._nnotches
            
        else:
            print("Error, direction undefined")
        
dial = Dial()
n_zeros = 0

with open("Dec01/input") as file:
    while line:=file.readline():
        turn = line.rstrip()
        dial.update_position(turn)
        print(dial.position, dial.npasses)
        if dial.position == 0:
            n_zeros +=1

print(f"Password: {n_zeros}")
print(f"Password method 0x434C49434B: {dial.npasses}")
