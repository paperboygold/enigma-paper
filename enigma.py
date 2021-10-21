# -*- coding: utf-8 -*-
'''
KIT103 Project: Enigma Machine Main Program

Name: Lucas Townsend
ID: 597588

This is the main file from which the program is called. It can be called from the commandline (command prompt or bash).
Please note that I have not included error catching in most cases so you must be correct with syntax or the program will crash.
The model used is the Kriegsmarine MK3, however it is not a perfect simulation as I was not able to perfectly replicate the physical machine's output.
Nonetheless the encryption used should be just as powerful as the actual machine and there are 8 rotors available in total. See data.py for a list of rotors and reflectors.

Test Case 1)
To encrypt: enigma.py -r I I II -i A B C -p AB CD EF -u B  -s ABC -t THEXAMERICANSXAREXCOMING
Output: HOLHCHIIWAHUMIRYGCRSKCVB

To decrypt: enigma.py -r I I II -i A B C -p AB CD EF -u B  -s ABC -t UPSPKJABEQOBYPKOROWMBYEP
Output: THEXAMERICANSXAREXCOMING

Test Case 2)
To encrypt: enigma.py -r I VII IV -i P O Z -p AL BF OK YX NE TV MI QG PZ SJ -u B -s ZAT -t THEXFUHRERXISXDEAD
Output: BJSKHSRSANAAIHBBEI

To decrypt: enigma.py -r I VII IV -i P O Z -p AL BF OK YX NE TV MI QG PZ SJ -u B -s ZAT -t BJSKHSRSANAAIHBBEI
Output: THEXFUHRERXISXDEAD
'''

import string
import argparse
import sys

import enigmaMachine

ALPHABET = string.ascii_uppercase
ALPHABETSET = set(ALPHABET)

PROG_DESC = 'An Enigma Machine MK3 simulation for the encryption and decryption of text.'

HELP_EPILOG = """\
    Encryption and decryption settings are supplied via the commandline by calling this file.
    Examples:
        $ %(prog)s -r I II III -i 1 2 3 -p AB CD EF GH IJ KL MN -u B -s XYZ -t TESTXTOXPROCESS
    """
    
def fromArgs(parser, args):
    '''Creating an Enigma machine from the command-line.'''
    
    # Joining text for passing to arguments.
    ringstellung = ' '.join(args.ringstellung) if args.ringstellung else None
    plugboard = ' '.join(args.plugboard) if args.plugboard else None
    
    # The machine being returned to the function which will be passed to main() when it is called.
    return enigmaMachine.EnigmaMachine.fromRotorKeys(rotors=args.rotors,
                                      ringstellung=ringstellung,
                                      plugboardSetting=plugboard,
                                      reflector=args.reflector)
   
    
# This is the main function which will parse commandline arguments and generate the Enigma machine object, then process the given text.
def main():
    # Parser setup
    parser = argparse.ArgumentParser(description=PROG_DESC, epilog=HELP_EPILOG, 
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('-r', '--rotors', nargs='+', metavar='ROTOR',
                        help='list of rotors from left to right; e.g I II III')
    parser.add_argument('-i', '--ringstellung', nargs='+',
                        metavar='RINGSTELLUNG',
                        help='ring settings for each rotor from left to right (0-25); e.g. 3 24 5')
    parser.add_argument('-p', '--plugboard', nargs='+', metavar='PLUGBOARD',
                        help='plugboard settings')
    parser.add_argument('-u', '--reflector', help='reflector setting, can be either B or C.')
    parser.add_argument('-s', '--start', help="represents the starting position of the rotors; e.g. Z N Q")
    parser.add_argument('-t', '--text', help='text to process; e.g. TESTXTEXT')

    args=parser.parse_args()
    
    # Creating the machine from arguments
    machine = fromArgs(parser, args)

    # Getting text to encrypt/decrypt.
    if args.text:
        text = args.text
    else:
        text = input('Input text please: ')
    machine.setDisplay(args.start)
    s = machine.processText(text, 'X')
    print(s)
    
def console_main():
    try:
        main()
    except (IOError) as ex:
        sys.stderr.write("%s\n" % ex)
   

if __name__ == '__main__':
    console_main()