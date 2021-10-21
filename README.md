# enigma-paper
A Python implementation of the MK3 Enigma machine.


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
