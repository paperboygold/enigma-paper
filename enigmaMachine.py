# -*- coding: utf-8 -*-
'''
KIT103 Project: Enigma Machine Generator

Name: Lucas Townsend
ID: 597588

This file hold the main class from which Enigma Machine objects are created.
It will return its output to the main() function in engima.py
'''

import string

from enigmaPlugboard import EnigmaPlugboard
from generator import createRotor, createReflector

KEYBOARD = string.ascii_uppercase
KEY_SET = set(KEYBOARD)

class EnigmaMachine:
    
    def __init__(self, rotors, reflector, plugboard):
        '''Paramaters are as follows:
            
            rotors - List of three rotors in string format separated by spaces.
            Options are: I, II, III, IV, V, VI, VII, VIII
            
            reflector - represents the reflector. Option is a string and should be either 'B' or 'C'.
            This represents the reflectors UKWB and UKWC.
            
            plugboard - plugboard object to represent the steckerbrecker at the front of the Enigma machine
        '''
        
        self.rotors = rotors
        self.rotorCount = len(rotors)
        self.reflector = reflector
        self.plugboard = plugboard
        
    @classmethod
    def fromRotorKeys(cls, rotors='I II III', ringstellung='A B C', reflector='B', plugboardSetting='AB CD EF'):
        # Main method for creating a new machine.

        if isinstance(rotors, str):
            rotors = rotors.split()
            
        numRotors = len(rotors)
        if ringstellung is None:
            ringstellung = [0] * numRotors
        elif isinstance(ringstellung, str):
            strings = ringstellung.split()
            ringstellungList = []
            for s in strings:
                ringstellungList.append(ord(s.upper()) - ord('A'))
                
        # Assembling the machine starting with rotors.
        rotorList = []
        rotorList = [createRotor(r[0], r[1]) for r in zip(rotors, ringstellungList)]
        return(cls(rotorList, createReflector(reflector), EnigmaPlugboard.fromKeySheet(plugboardSetting)))
    
    def setDisplay(self, value):
        # Changes the currently displayed character in the 'window'.'''
        
        for i, rotor in enumerate(reversed(self.rotors)):
            rotor.setDisplay(value[-1 - i])
            
    def getDisplay(self):
        # Gets the current values which would be in the Enigma's window, which shows the current rotor setting.
        return f"{self.rotors[-3].getDisplay()} {self.rotors[-2].getDisplay()} {self.rotors[-1].getDisplay()}"
    
    def keyPress(self, key):
        '''Simulates a key press on the machine.
        
        key - representing the character pressed on the keyboard

        '''
        # Mechanical step of the rotor
        self._stepRotors()
        
        # Electrical charge travelling through machine
        signalNum = ord(key) - ord('A')
        lampNum = self._electricSignal(signalNum)
        return KEYBOARD[lampNum]
        
    def _stepRotors(self):
        '''Simulates pressing down on the stepping bar which would turn the axel which in turn pushes the pawls
        upwards and increments the positioning of the rotors.
            The first rotor will always move.
                The middle rotor moves if the right rotor's left notch is over the 2nd paw or its left side notch is over the 3rd rotor's pawl
                    The third rotor will rotate only if the middle rotor has a notch over the 3rd pawl.'''
        
        rotor1 = self.rotors[-1]
        rotor2 = self.rotors[-2]
        rotor3 = self.rotors[-3]
        
        # Decide which rotors can move
        rotate2 = rotor1.notchOnPawl() or rotor2.notchOnPawl()
        rotate3 = rotor2.notchOnPawl()
    
        # Move rotors
        rotor1.rotate()
        if rotate2:
            rotor2.rotate()
        if rotate3:
            rotor3.rotate()
        
    def _electricSignal(self, signalNum):
        '''Simulation of the electrical signal which runs through the machine to perform encryption or decryption.
        
        signalNum - (0-25) simulates the wire which the electrical current travels along
        
        Returns the encrypted/decrypted character.'''
        
        pos = self.plugboard.signal(signalNum)
        
        for rotor in reversed(self.rotors):
            pos = rotor.signalIn(pos)
            
        pos = self.reflector.signalIn(pos)
        
        for rotor in self.rotors:
            pos = rotor.signalOut(pos)
        
        return self.plugboard.signal(pos)
    
    def processText(self, text, replaceChar='X'):
        '''This is the main function for actually processing the text that we want to encrypt or decrypt.
        
        text - is the text we're processing. It will be in uppercase.'
        '''
    
        result = []    
        for key in text:
            c = key.upper()
            
            # Replaces unknown characters (hopefully a space) with an X
            if c not in KEYBOARD:
                if replaceChar:
                    c = replaceChar
                else:
                    continue
            
            result.append(self.keyPress(c))
        
        return ''.join(result)
    
    def getRotorCounts(self):
        # Return the rotor rotation counts as a list of integers.
        return [r.rotations for r in self.rotors]