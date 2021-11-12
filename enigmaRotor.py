# -*- coding: utf-8 -*-
'''
Enigma Machine Plugboard


This class is responsible for the creation of the Rotor objects as well as the chosen reflector. It returns them to enigmaMachine for assembly.
'''

class EnigmaRotor:

    def __init__(self, rotor, connections, ringstellung=0, step=None):
        self.name = rotor
        self.connectionString = connections.upper()
        self.ringstellung = ringstellung
        self.pos = 0
        self.rotations = 0
        
        # Using list comprehension for populating the entryMap.
        # Takes the ordinal of our position in the rotor connection string and subtracts the ordinal of 'A' (1)
        # This gives us the proper output as we are working from 0-25 not 1-26.'''
        self.entryMap = [ord(pin) - ord('A') for pin in self.connectionString]
        
        #Enumerates through the entryMap and then assigns the value found to the corresponding exit map position.
        self.exitMap = [0] * 26
        for a, b in enumerate(self.entryMap):
            self.exitMap[b] = a
            
        # Map display values to positions.
        # We use chr(ord('A') + n) to refer to get the next letter in the alphabet at each step of the loop.
        # The ord value refers to the unicode value of the character which we divide by 26 to get its position in the human alphabet.
        self.displayMap = {}
        for n in range(26):
            self.displayMap[chr(ord('A') + n)] = (n - self.ringstellung) % 26
        # Reverse the map for positions mapped to display values using set comprehension.
        self.positionMap = {a : b for b, a in self.displayMap.items()}
        
        # Window set for where our notches which will come into contact with the pawls
        self.stepSet = set()
        if step is not None:
            for pos in step:
                if pos in self.displayMap:
                    self.stepSet.add(pos)
                else:
                    print('Stepping: %s' % pos)
    
        # Sets the initial position
        self.setDisplay('A')
        
    def setDisplay(self, val):
        # Spins the rotor so that the 'val' you feed it appears in the window.
        # A value of 'A' would be position 0 with an internal ring setting of 0
        # The rotation position is then set to 0 
        s = val.upper()
        self.pos = self.displayMap[s]
        self.displayVal = s
        self.rotations = 0
        
    def getDisplay(self):
        # Returns the current letter displayed
        return self.displayVal
        
    def signalIn(self, n):
        # Returns the pin number of the output signal (0-25). 
        # Simulates the electrical signal.
        
        pin = (n + self.pos) % 26
        contact = self.entryMap[pin]
        return (contact - self.pos) % 26
    
    def signalOut(self, n):
        # Returns the pin number of the output signal (0-25). 
        # Simulates the electrical signal.
        contact = (n + self.pos) % 26
        pin = self.exitMap[contact]
        return (pin - self.pos) % 26
        
    def notchOnPawl(self):
        # Simulates where the rotor comes into contact with the pawl which attaches to the axel.
        # This contact is what shifts the next rotor in order in the real machine.
        return self.displayVal in self.stepSet
    
    def rotate(self):
        # Following the notchOnPawl function, this function will perform the rotation of the rotors into the next position.
        self.pos = (self.pos + 1) % 26
        self.displayVal = self.positionMap[self.pos]
        self.rotations += 1

    
