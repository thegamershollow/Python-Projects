import binascii
import hashlib
import os
from pathlib import Path

#prompt = input('Type the number corresponding to the option you want to select below.\n1. View Gen1 Save\n2. Edit Gen1 Save\n3. Help\n4. Exit\n\noption: ')
# prompt 1
#if prompt == '1':
#    print('Option1')
# prompt 2
#if prompt == '2':
#    print('Option2')
# prompt 3
#if prompt == '3':
#    print('Option3')
# prompt 4
#if prompt == '4':
#    print('Option4')

savFilePath = '/Users/Cal/Documents/Github/Python-Projects/PKMN GB:GBA:GBC Save Editor/Saves (For analysis)/Pokemon Red.sav'
# '/Users/Cal/Documents/Github/Python-Projects/PKMN GB:GBA:GBC Save Editor/Saves (For analysis)/Pokemon Red.sav'
# '/Users/Cal/Downloads/Pokemon Red (1).sav'

#input('Drag the .sav file into the command prompt\n\nThe press enter')
savFilePath = savFilePath.replace("'","")
fileCheck = Path(savFilePath)
savFile = open(savFilePath, 'rb')

#* Pokémon Character Decoder
def decodeText(var):
    decoder = str(var)[2:-1]
    decoder = decoder.replace("\\"," ")
    decoder = decoder.replace("P","")
    x80 = "A"; x81 = "B"; x82 = "C"; x83 = "D"; x84 = "E"; x85 = "F"; x86 = "G"; x87 = "H"; x88 = "I"; x89 = "J"; x8A = "K"; x8B = "L"; x8C = "M"; x8D = "N"; x8E = "O"; x8F = "P"; x90 = "Q"; x91 = "R"; x92 = "S"; x93 = "T"; x94 = "U"; x95 = "V"; x96 = "W"; x97 = "X"; x98 = "Y"; x99 = "Z"; x9A = "("; x9B = ")"; x9C = "="; x9D = ","; x9E = "["; x9F = "]"; xA0 = "a"; xA1 = "b"; xA2 = "c"; xA3 = "d"; xA4 = "e"; xA5 = "f"; xA6 = "g"; xA7 = "h"; xA8 = "i"; xA9 = "j"; xAA = "k"; xAB = "l"; xAC = "m"; xAD = "n"; xAE = "o"; xAF = "p"; xB0 = "q"; xB1 = "r"; xB2 = "s"; xB3 = "t"; xB4 = "u"; xB5 = "v"; xB6 = "w"; xB7 = "x"; xB8 = "y"; xB9 = "z"; xE1 = "PK"; xE2 = "MN"; xE3 = "-"; xE6 = "?"; xE7 = "!"; xE8 = "."; xF1 = "*"; xF3 = "/"; xF4 = ";"; xF6 = "0"; xF7 = "1"; xF8 = "2"; xF9 = "3"; xFA = "4"; xFB = "5"; xFC = "6"; xFD = "7"; xFE = "8"; xFF = "9"
    decoder = decoder.replace('x00',''); decoder = decoder.replace('x80',x80); decoder = decoder.replace('x81',x81); decoder = decoder.replace('x82',x82); decoder = decoder.replace('x83',x83); decoder = decoder.replace('x84',x84); decoder = decoder.replace('x85',x85); decoder = decoder.replace('x86',x86); decoder = decoder.replace('x87',x87); decoder = decoder.replace('x88',x88); decoder = decoder.replace('x89',x89); decoder = decoder.replace('x8A',x8A); decoder = decoder.replace('x8B',x8B); decoder = decoder.replace('x8C',x8C); decoder = decoder.replace('x8D',x8D); decoder = decoder.replace('x8E',x8E); decoder = decoder.replace('x8F',x8F); decoder = decoder.replace('x90',x90); decoder = decoder.replace('x91',x91); decoder = decoder.replace('x92',x92); decoder = decoder.replace('x93',x93); decoder = decoder.replace('x94',x94); decoder = decoder.replace('x95',x95); decoder = decoder.replace('x96',x96); decoder = decoder.replace('x97',x97); decoder = decoder.replace('x98',x98); decoder = decoder.replace('x99',x99); decoder = decoder.replace('x9A',x9A); decoder = decoder.replace('x9B',x9B); decoder = decoder.replace('x9C',x9C); decoder = decoder.replace('x9D',x9D); decoder = decoder.replace('x9E',x9E); decoder = decoder.replace('x9F',x9F); decoder = decoder.replace('xA0',xA0); decoder = decoder.replace('xA1',xA1); decoder = decoder.replace('xA2',xA2); decoder = decoder.replace('xA3',xA3); decoder = decoder.replace('xA4',xA4); decoder = decoder.replace('xA5',xA5); decoder = decoder.replace('xA6',xA6); decoder = decoder.replace('xA6',xA6); decoder = decoder.replace('xA7',xA7); decoder = decoder.replace('xA8',xA8); decoder = decoder.replace('xA9',xA9); decoder = decoder.replace('xAA',xAA); decoder = decoder.replace('xAB',xAB); decoder = decoder.replace('xAC',xAC); decoder = decoder.replace('xAD',xAD); decoder = decoder.replace('xAE',xAE); decoder = decoder.replace('xAF',xAF); decoder = decoder.replace('xB0',xB0); decoder = decoder.replace('xB1',xB1); decoder = decoder.replace('xB2',xB2); decoder = decoder.replace('xB3',xB3); decoder = decoder.replace('xB4',xB4); decoder = decoder.replace('xB5',xB5); decoder = decoder.replace('xB6',xB6); decoder = decoder.replace('xB7',xB7); decoder = decoder.replace('xB8',xB8); decoder = decoder.replace('xB9',xB9); decoder = decoder.replace('xE1',xE1); decoder = decoder.replace('xE2',xE2); decoder = decoder.replace('xE3',xE3); decoder = decoder.replace('xE6',xE6); decoder = decoder.replace('xE7',xE7); decoder = decoder.replace('xE8',xE8); decoder = decoder.replace('xF1',xF1); decoder = decoder.replace('xF3',xF3); decoder = decoder.replace('xF4',xF4); decoder = decoder.replace('xF6',xF6); decoder = decoder.replace('xF7',xF7); decoder = decoder.replace('xF8',xF8); decoder = decoder.replace('xF9',xF9); decoder = decoder.replace('xFA',xFA); decoder = decoder.replace('xFB',xFB); decoder = decoder.replace('xFC',xFC); decoder = decoder.replace('xFD',xFD); decoder = decoder.replace('xFE',xFE); decoder = decoder.replace('xFF',xFF)
    decoder = decoder.replace(" ","")
    var = decoder
    return var

#* Gen 1 save viewer

#chechsum
chechsum = 0
savFile.seek(0x3523,1)
chechsum = savFile.read(8)

#Trainer Name
savFile.seek(0x2598)
gen1TrainerName = savFile.read(7)
gen1TrainerName = decodeText(gen1TrainerName)
#print('Trainer Name: '+gen1TrainerName+'\n')

#Obtained Badges
savFile.seek(0x2602)
gymBadges = savFile.read(7)
obtGymBadges = str(gymBadges)[2:-1]
gymBadges = obtGymBadges.replace("\\"," ")
def badges():
    badgeList = 'Boulder', 'Cascade', 'Thunder', 'Rainbow', 'Soul', 'Marsh', 'Volcano', 'Earth'
    badgeList.count()
    boulderObt = ''
print(gymBadges)