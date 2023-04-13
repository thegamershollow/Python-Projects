import binascii
import hashlib
import mmap
from pathlib import Path

savFilePath = '/Users/Cal/Downloads/Pokemon Red (1).sav' 
#input('Drag the .sav file into the command prompt\n\nThe press enter')
savFilePath = savFilePath.replace("'","")
fileCheck = Path(savFilePath)
savFile = open(savFilePath, 'rb')



#* Gen 1 save editor

#chechsum
chechsum = 0
savFile.seek(0x3523,1)
chechsum = savFile.read(8)
#Trainer Name
savFile.seek(0x2598)
gen1TrainerName = savFile.read(7)
nameString = str(gen1TrainerName)[2:-1]
nameString = nameString.replace("\\"," ")
nameString = nameString.replace("P","")
x80 = "A"; x81 = "B"; x82 = "C"; x83 = "D"; x84 = "E"; x85 = "F"; x86 = "G"; x87 = "H"; x88 = "I"; x89 = "J"; x8A = "K"; x8B = "L"; x8C = "M"; x8D = "N"; x8E = "O"; x8F = "P"; x90 = "Q"; x91 = "R"; x92 = "S"; x93 = "T"; x94 = "U"; x95 = "V"; x96 = "W"; x97 = "X"; x98 = "Y"; x99 = "Z"; x9A = "("; x9B = ")"; x9C = "="; x9D = ","; x9E = "["; x9F = "]"; xA0 = "a"; xA1 = "b"; xA2 = "c"; xA3 = "d"; xA4 = "e"; xA5 = "f"; xA6 = "g"; xA7 = "h"; xA8 = "i"; xA9 = "j"; xAA = "k"; xAB = "l"; xAC = "m"; xAD = "n"; xAE = "o"; xAF = "p"; xB0 = "q"; xB1 = "r"; xB2 = "s"; xB3 = "t"; xB4 = "u"; xB5 = "v"; xB6 = "w"; xB7 = "x"; xB8 = "y"; xB9 = "z"; xE1 = "PK"; xE2 = "MN"; xE3 = "-"; xE6 = "?"; xE7 = "!"; xE8 = "."; xF1 = "*"; xF3 = "/"; xF4 = ";"; xF6 = "0"; xF7 = "1"; xF8 = "2"; xF9 = "3"; xFA = "4"; xFB = "5"; xFC = "6"; xFD = "7"; xFE = "8"; xFF = "9"
nameString = nameString.replace('x00',''); nameString = nameString.replace('x80',x80); nameString = nameString.replace('x81',x81); nameString = nameString.replace('x82',x82); nameString = nameString.replace('x83',x83); nameString = nameString.replace('x84',x84); nameString = nameString.replace('x85',x85); nameString = nameString.replace('x86',x86); nameString = nameString.replace('x87',x87); nameString = nameString.replace('x88',x88); nameString = nameString.replace('x89',x89); nameString = nameString.replace('x8A',x8A); nameString = nameString.replace('x8B',x8B); nameString = nameString.replace('x8C',x8C); nameString = nameString.replace('x8D',x8D); nameString = nameString.replace('x8E',x8E); nameString = nameString.replace('x8F',x8F); nameString = nameString.replace('x90',x90); nameString = nameString.replace('x91',x91); nameString = nameString.replace('x92',x92); nameString = nameString.replace('x93',x93); nameString = nameString.replace('x94',x94); nameString = nameString.replace('x95',x95); nameString = nameString.replace('x96',x96); nameString = nameString.replace('x97',x97); nameString = nameString.replace('x98',x98); nameString = nameString.replace('x99',x99); nameString = nameString.replace('x9A',x9A); nameString = nameString.replace('x9B',x9B); nameString = nameString.replace('x9C',x9C); nameString = nameString.replace('x9D',x9D); nameString = nameString.replace('x9E',x9E); nameString = nameString.replace('x9F',x9F); nameString = nameString.replace('xA0',xA0); nameString = nameString.replace('xA1',xA1); nameString = nameString.replace('xA2',xA2); nameString = nameString.replace('xA3',xA3); nameString = nameString.replace('xA4',xA4); nameString = nameString.replace('xA5',xA5); nameString = nameString.replace('xA6',xA6); nameString = nameString.replace('xA6',xA6); nameString = nameString.replace('xA7',xA7); nameString = nameString.replace('xA8',xA8); nameString = nameString.replace('xA9',xA9); nameString = nameString.replace('xAA',xAA); nameString = nameString.replace('xAB',xAB); nameString = nameString.replace('xAC',xAC); nameString = nameString.replace('xAD',xAD); nameString = nameString.replace('xAE',xAE); nameString = nameString.replace('xAF',xAF); nameString = nameString.replace('xB0',xB0); nameString = nameString.replace('xB1',xB1); nameString = nameString.replace('xB2',xB2); nameString = nameString.replace('xB3',xB3); nameString = nameString.replace('xB4',xB4); nameString = nameString.replace('xB5',xB5); nameString = nameString.replace('xB6',xB6); nameString = nameString.replace('xB7',xB7); nameString = nameString.replace('xB8',xB8); nameString = nameString.replace('xB9',xB9); nameString = nameString.replace('xE1',xE1); nameString = nameString.replace('xE2',xE2); nameString = nameString.replace('xE3',xE3); nameString = nameString.replace('xE6',xE6); nameString = nameString.replace('xE7',xE7); nameString = nameString.replace('xE8',xE8); nameString = nameString.replace('xF1',xF1); nameString = nameString.replace('xF3',xF3); nameString = nameString.replace('xF4',xF4); nameString = nameString.replace('xF6',xF6); nameString = nameString.replace('xF7',xF7); nameString = nameString.replace('xF8',xF8); nameString = nameString.replace('xF9',xF9); nameString = nameString.replace('xFA',xFA); nameString = nameString.replace('xFB',xFB); nameString = nameString.replace('xFC',xFC); nameString = nameString.replace('xFD',xFD); nameString = nameString.replace('xFE',xFE); nameString = nameString.replace('xFF',xFF)
nameString = nameString.replace(" ","")
print(nameString)