# load in obj file

# input hex format (5 vertices)
# 0A 76 20 2D 32 2E 38 31 32 35 30 30 20 35 37 2E 32 35 37 38 30 31 20 33 2E 34 36 30 38 39 36 
# 0A 76 20 2D 32 2E 38 33 32 30 30 30 20 35 37 2E 31 34 34 35 30 31 20 33 2E 36 38 33 35 39 36 
# 0A 76 20 2D 32 2E 36 35 36 32 30 30 20 35 37 2E 31 39 31 33 39 39 20 33 2E 36 31 37 31 39 36 
# 0A 76 20 2D 33 2E 30 31 31 37 30 30 20 35 37 2E 32 37 37 33 30 32 20 33 2E 34 38 34 33 39 36 
# 0A 76 20 32 2E 38 31 32 35 30 30 20 35 37 2E 32 35 37 38 30 31 20 33 2E 34 36 30 38 39 36  

# v start = 0A 76 20, vt start = 0A 76 74 20
# 20 = divider between values 

# output example (first 12 bytes are vertices - 4 each for XYZ) first two = ones place signed, second two = decimal place (x/256)
# 00 21 3E 59 05 AB    0.1289 62.3477 5.6680
# FF C9 3E 5B 05 93   -0.2148 62.3555 5.5742
# 00 37 3E 5B 05 93    0.2148 62.3555 5.5742
# FF DF 3E 59 05 AB   -0.1289 62.3477 5.6680
# FC 29 3C 78 02 D3   -3.8398 60.4688 2.8242

# RSF Reference facemask
# vx vx vy vy vz vz sp sp            
# 00 21 3E 59 05 AB|00 04|F6 F1 13 85 00 00 3B B2|00 00 00 00 13 13 13 13 
# FF C9 3E 5B 05 93|00 04|40 A6 2E CB 00 00 3C 00|00 00 00 00 13 13 13 13 
# 00 37 3E 5B 05 93|00 04|40 A6 29 35 00 00 3C 00|00 00 00 00 13 13 13 13 
# FF DF 3E 59 05 AB|00 04|F6 F1 14 7B 00 00 3B B2|00 00 00 00 13 13 13 13 
# FC 29 3C 78 02 D3|00 04|DE F4 4C 6E 00 00 3B 85|00 00 00 00 13 13 13 13 
# FC B5 3B C5 03 AD|00 04|68 CE EE AE 3C 00 38 7D|00 00 00 00 13 13 13 13 

## RSF Reference Helmet
# vx vx vy vy vz vz sp sp                         u1 u2 v1 v2
# FF 9F 3A 97 FC 8B|00 13|E9 FF 9B EF F7 5F E8 06|00 00 39 FF|A4 D5 25 7D A4 D5 25 7D 
# FF FF 3A 96 FC 7F|00 13|F5 96 8A D1 F1 1F C7 FD|00 00 39 FF|A4 DD 25 7D A4 DD 25 7D 
# FF FF 3B 4D FC 6A|00 13|FF C0 4B FF EC 9F 9F FD|00 00 39 FF|A4 DD 25 67 A4 DD 25 67 
# FD 7D 3D CF 04 80|00 13|AF 4A 62 D0 92 FD D5 F3|24 3A 39 C1|34 7F 32 E4 34 7F 32 E4 
# FD 39 3D BA 04 52|00 13|F9 9F 78 AD 9F 3D A5 6B|25 33 39 B6|34 66 33 08 34 66 33 08

# 00 B9 3A 1E FC 9C 00 13 FA 9B 92 05 05 A4 75 FB|00 00 39 FF|A7 A4 24 46 A7 A4 24 46 
# 01 54 3A 1E FC BF 00 13 DB 97 CD 95 24 A8 3A 6B|00 00 39 FF|A7 90 24 48 A7 90 24 48
# 00 EC 3A D7 FC 88 00 13 D8 9B 86 61 27 A4 81 9F|00 00 39 FF|A7 9C 24 2E A7 9C 24 2E 
# FC C5 3A 00 FF F7 00 13 1D 09 BB B3 FB FB 0C 0E|33 0A 39 14|30 49 37 2C 30 49 37 2C 
# FC BF 39 FC FF F3 00 13 1D 09 BB B3 FB FB 0C 0E|33 06 39 14|30 42 37 2F 30 42 37 2F


# v start = 0A 76 20, vt start = 0A 76 74 20

# index
# 00 00 00 01 00 02 
# 00 00 00 03 00 01 
# 00 04 00 05 00 06 
# 00 04 00 07 00 05 
# 00 07 00 08 00 05 
# 00 07 00 09 00 08 
# 00 0A 00 08 00 09 
# 00 0A 00 09 00 0B 
# 00 0C 00 0A 00 0B 
# 00 0C 00 0D 00 0A

import math
import os
from rsfFormatter import rsfFormatter
import csv

def openOBJ(obj):
    currPath = os.getcwd()
    print(currPath)
    fpath = os.path.join(currPath,'obj2hex',obj)
    # print(fpath)
    f = open(fpath,'r')
    fraw = f.read()
    # print(f'fraw: {fraw}')
    return fraw

def sortOBJ(objIn, type):
    vL = []
    typeSp = f'{type}'
    print(typeSp)
    # print(f'fl2: {fl2}')
    objSplit = objIn.split(' ')
    fl = [s for s in objSplit if s != '\n' and s != ' ']
    print(fl)
    separatorInd = [index for (index, item) in enumerate(objSplit) if item == typeSp]

        
    print(f'separator inds: {separatorInd}')
   
    
    vStartInds = []
    
    for i in separatorInd:
        if type == 'v':
            if fl2[i+1] == qv[0] and fl2[i+2] == qv[1]:
                # print(f'vertex buffer found at {i}')
                vStartInds.append(i)
        elif type == 'vt':
            if fl2[i+1] == qv[0] and fl2[i+2] == qv[1] and fl2[i+3] == qv[2]:
                # print(f'uv buffer found at {i}')
                vStartInds.append(i)
        elif type == 'f':
            if fl2[i+1] == qv[0] and fl2[i+2] == qv[1]:
                vStartInds.append(i)
            
            
    # print(vStartInds)

    for i in vStartInds:
        fl3 = []
        fl3.append(sep)
        for j in range(i+1,len(fl2)):   
            v = fl2[j]  
            # print(v)
            if v == '0A':
                # print('end of buffer')
                break
            else:
                fl3.append(v)
        # print(fl3)
        vS = ' '.join([str(elem) for k,elem in enumerate(fl3)])
        #print(vS)
        vL.append(vS)
    return vL

def getVerts(data): 
    hexTocp1252 = bytes.fromhex(data).decode('cp1252')
    vOut = hexTocp1252.split(' ')
    vOut.pop(0)
    vOut = list(map(float,vOut))
    return vOut

def getFaces(data): 
    hexTocp1252 = bytes.fromhex(data).decode('cp1252')
    
    vOut = hexTocp1252.split(' ')
    vOut.pop(0)
    fOut = []

    for i in vOut:
        bytesOut = ['00']*6
        ispl = i.split('/')
        for k in range(0,5,2):
            # v1
            #print(f'k = {k}')
            j = ispl[int((k/2))]
            #print(j)
            if int(j) < 256:
                #print('j less than 256')
                for sublist in posDic:
                    if sublist[0] == int(j):
                        bytesOut[k+1] = sublist[1]
                        break
            else:
                #print('j 256 or higher')
                f = divmod(int(j),256)
                #print(f'matching hex for {f[0]}')
                for sublist in posDic:
                    if sublist[0] == f[0]:
                        bytesOut[k] = sublist[1]
                #print(f'matching hex for {f[1]}')
                for sublist in posDic:
                    if sublist[0] == f[1]:
                        bytesOut[k+1] = sublist[1]
        for i in bytesOut:
            fOut.append(i)
    
    fStrOut = listToString(fOut)
    return fStrOut

def buildTable():
    vals = range(0,256)
    posDic = [[i, '{:02X}'.format(i)] for i in vals]
    negDic = [[i-255, '{:02X}'.format(i)] for i in vals]
    return posDic, negDic

def searchList(j, mode):
    bytesOut = [0]*2
    
    (d, i)= math.modf(j)
    #print(f'checking {j}')
    dfull = math.ceil(d*256)
    #print(dfull)
    if i >= 0: # int greater than zero
        #print(f'positive i: {int(i)}')
        for sublist in posDic:
            if sublist[0] == int(i):
                bytesOut[0] = sublist[1]
                break 
        for sublist in posDic:
            if dfull == 0:
                bytesOut[1] = '00' # if zero assign 00
            elif sublist[0] == dfull-1:
                bytesOut[1] = sublist[1]
                break        
    else: # int less than zero
        #print(f'negative i: {int(i)}')
        for sublist in negDic:
            if sublist[0] == int(i):
                bytesOut[0] = sublist[1]
                break 
        for sublist in negDic: 
            if dfull == 0: # if zero assign FF
                bytesOut[1] = 'FF'      
            elif sublist[0] == dfull:
                bytesOut[1] = sublist[1]
                break
    return bytesOut

def splitVerts(dataIn, type):
    
    if type == 'v':
    # receive XYZ verts, split into X Y and Z
        vBytes = [0]*3  
        # x: 
        vBytes[0:1] = searchList(dataIn[0], 0, 1)
        # y:
        vBytes[2:3] = searchList(dataIn[1], 2, 3)
        # z: 
        vBytes[4:5] = searchList(dataIn[2], 4, 5)
        
        vS = ' '.join([str(elem) for k,elem in enumerate(vBytes)]) # make string from list
    elif type == 'vt':
        vBytes = [] 
        # u: 
        vBytes[0:1] = searchList(dataIn[0], 0, 1)
        # v:
        vBytes[2:3] = searchList(dataIn[1], 2, 3)
    
    return vBytes

def listToString(listin):
    strOut = ' '.join(i for i in listin)
    return strOut

outputSTRM = open('test1_out_STRM.txt','w', newline='')
outputINDX = open('test1_out_INDX.txt','w', newline='')
wSTRM = csv.writer(outputSTRM)
wINDX = csv.writer(outputINDX)

posDic, negDic = buildTable()         
            
objF = openOBJ('revospeedQB_reangled2.obj')
#print(objF)

vList = sortOBJ(objF, 'v')
fList = sortOBJ(objF, 'f')

#print(vList)

for i in vList:
    print('getting vertices...')
    vOut = getVerts(vList)
    print(vOut)
    
for i in fList:
    print(f'converting {i}')
    fBytes = getFaces(i)
    print(fBytes)
    

#### steps to do

# iterate thru .obj file and find all vertices denoted by V, VT, VN
# read into list of lists DONE
#

# read in each vertex - getVerts
# convert to hex
# export to STRM format
# packager for this

# read in indices and convert
# Export to INDX format


