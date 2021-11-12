# -*- coding: utf-8 -*-
'''
Enigma Machine Plugboard

This file contains the Plugboard behavior and settings and returns it to the EnigmaMachine class.
'''

import copy
import string

LABELS = string.ascii_uppercase

MAX_PAIRS = 13

class EnigmaPlugboard:
    
    def __init__(self, wiringPairs=None):
        
        # Default wiring
        self.wiringMap = list(range(26))
        self._backupMap = list(range(26)) # Exclude
        
        if not wiringPairs:
            return
            
        for pair in wiringPairs:
            m = pair[0]
            n = pair[1]
            if not (0 <= m < 26) or not (0 <= n < 26):  
                print("Welp. Something went wrong...")
            self.wiringMap[m] = n
            self.wiringMap[n] = m
            
    @classmethod
    def fromKeySheet(cls, settings=None):
        # Will take the settings provided by the user and use it to configure the plugboard.
        if not settings:
            return cls(None)
        
        wiringPairs = []
        
        pairs = settings.upper().split()
        
        for p in pairs:
            if len(p) != 2:
                print("Invalid pair.")
                
        m = p[0]
        n = p[1]
        
        wiringPairs.append((ord(m) - ord('A'), ord(n) - ord('A')))
        
        return cls(wiringPairs)

    def getPairs(self):
        # Gets the current pairs on the plugboard/steckerbrecker.
        pairs = set()
        for x in range(0, 26):
            y = self.wiringMap[x]
            if x != y and (y, x) not in pairs:
                pairs.add((x, y))
    
        return pairs

    def __str__(self):
        # Modifies the __str__ return behavior to join pairs together. Does an fstring work here considering the for loop?
        pairs = list(self.getPairs())
        pairs.sort()
        return ' '.join('{}{}'.format(chr(t[0] + ord('A')),
                                      chr(t[1] + ord('A'))) for t in pairs)
        # f"{chr(t[] + ord('A'))'}{chr(t[1] + ord('A'))}"
    def signal(self, n):
        # For where the signal enters the plugboard via the wire. It returns 0-25 and signal direction is irrelevant.'''
        return self.wiringMap[n]
    
    def getWiring(self):
        # Recursively copies the wiring map.
        return copy.deepcopy(self.wiringMap)
    
    def isWired(self, n):
        # Checks if the connection n has a cable attached
        return self.wiringMap[n] != n
    
    def isFree(self, n):
        # Checks if the connection does not have a cable attached.
        return self.wiringMap[n] == n
    
    def __enter__(self):
        # Saves the state of the map on enter.
        for n in range(26):
            self._backupMap[n] = self.wiringMap[n]
        return self
    
    def __exit__(self, *exc_info):
        # Restores default wiring upon exit.
        for n in range(26):
            self.wiringMap[n]
        
    def connection(self, n):
        # Returns a plug number from 0-25 for what's connected to a given plug.
        return self.wiringMap[n]
    
    def disconnect(self, n):
        # Remove a cable from plug number n 0-25.
        x = self.wiringMap[n]
        self.wiringMap[x] = x
        self.wiringMap[n] = n
        
    def connect(self, x, y):
        # Connect plug x to plug y, and remove old connections.
        m = self.wiringMap[x]
        n = self.wiringMap[y]
        self.wiringMap[m] = m
        self.wiring_map[n] = n
        self.wiringMap[x] = y
        self.wiringMap[y] = x
        
    def isConnected(self, x, y):
        # Checks if plug x is connected to plug y and returns true if yes, false if no.
        return self.wiringMap[x] == y and self.wiringMap[y] == x
    
        
