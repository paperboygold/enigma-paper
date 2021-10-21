# -*- coding: utf-8 -*-
'''
KIT103 Project: Enigma Machine Plugboard

Name: Lucas Townsend
ID: 597588

This file is for generating new rotors and reflector objects.'''

from data import ROTORS, REFLECTORS
from enigmaRotor import EnigmaRotor

def createRotor(rotorType, ringstellung):
    rotorData = ROTORS[rotorType]
    return EnigmaRotor(rotorType, rotorData['connections'], ringstellung, rotorData['notch'])
                
def createReflector(reflectorType):
    return EnigmaRotor(reflectorType, connections=REFLECTORS[reflectorType]) 