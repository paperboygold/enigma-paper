# -*- coding: utf-8 -*-
'''
Enigma Machine Plugboard

This file holds information about the rotors and reflectors for use elsewhere in the program.'''

ROTORS = {
            'I': {
                'connections': 'EKMFLGDQVZNTOWYHXUSPAIBRCJ', 'notch': 'Q',
                },
            'II': {
                'connections': 'AJDKSIRUXBLHWTMCQGZNPYFVOE', 'notch': 'E',
                },
            'III': {
                'connections': 'BDFHJLCPRTXVZNYEIWGAKMUSQO', 'notch': 'V',
                },
            'IV': {
                'connections': 'ESOVPZJAYQUIRHXLNFTGKDCMWB', 'notch': 'J',
                },
            'V': {
                'connections': 'VZBRGITYUPSDNHLXAWMJQOFECK', 'notch': 'Z',
                },
            'VI': {
                'connections': 'JPGVOUMFYQBENHZRDKASXLICTW', 'notch': 'ZM',
                },
            'VII': {
                'connections': 'NZJHGRCXMYSWBOUFAIVLPEKQDT', 'notch': 'ZM',
                },
            'VIII': {
                'connections': 'FKQHTLXOCBJSPDZRAMEWNIUYGV', 'notch': 'ZM',
                },
            }

REFLECTORS = {
    'B': 'YRUHQSLDPXNGOKMIEBFZCWVJAT',
    'C': 'FVPJIAOYEDRZXWGCTKUQSBNMHL',
    }
