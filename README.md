# enigma-paper
A Python implementation of the MK3 Enigma machine. Only kept for my reference since it is a combination of at least three different people's code (unless that's what developing actually comes down to, in which case, I dunno man) mostly created for my own understanding of the Enigma Machine.


## Examples
### Example One
  To encrypt: enigma.py -r I I II -i A B C -p AB CD EF -u B  -s ABC -t THEXAMERICANSXAREXCOMING
  
  Output: UPSPKJABEQOBYPKOROWMBYEP

  To decrypt: enigma.py -r I I II -i A B C -p AB CD EF -u B  -s ABC -t UPSPKJABEQOBYPKOROWMBYEP
  
  Output: THEXAMERICANSXAREXCOMING

### Example Two
  To encrypt: enigma.py -r I VII IV -i P O Z -p AL BF OK YX NE TV MI QG PZ SJ -u B -s ZAT -t THEXFUHRERXISXDEAD
  
  Output: BJSKHSRSANAAIHBBEI

  To decrypt: enigma.py -r I VII IV -i P O Z -p AL BF OK YX NE TV MI QG PZ SJ -u B -s ZAT -t BJSKHSRSANAAIHBBEI
  
  Output: THEXFUHRERXISXDEAD
