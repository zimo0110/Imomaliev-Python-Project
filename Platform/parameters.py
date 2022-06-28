#level one map, represented with letters as it is easier to visualise letters rather than 1's and 0's
levOne_map = [
'                             ',
'                             ',
'                             ',
' XX    XXX            XX    X',
' XX P                        ',
' XXXX         XX         XX  ',
' XXXX       XX             XX',
' XX    X  XXXX    XX  XX    X',
'       X  XXXX    XX  XXX   X',
'    XXXX  XXXXXX  XX  XXXX  X',
'XXXXXXXX  XXXXXX  XX  XXXX  X']

#parameters that are used across the game
tileDim = 64
scr_width = 1200
scr_height = len(levOne_map) * tileDim