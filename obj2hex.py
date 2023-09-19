import math
import os
import csv
import mmap
from swapExistSTRM import ogToNewStrm

blenderObj = 'revospeedQB_1.obj'
rsfName = 'HELMETFACEMASKSALL_base.RSF'

def fileStuff():
    dirID = 0
    currWD = os.getcwd()
    inputPath = os.path.join(currWD,'input')
    outputPath = os.path.join(currWD,'output')

    allOutDirs = [ f.name for f in os.scandir(outputPath) if f.is_dir() ]
    allOutDirs.sort()
    if allOutDirs != []:
        latest = allOutDirs[-1][-1]
        
        dirID = int(latest) + 1
    path = os.path.join(outputPath, f'output{dirID}')
    currOutputDir = path
    os.mkdir(path)

    outputIndx = open(os.path.join(path,'new_Indx.txt'),'w', newline='')
    outputStrm = open(os.path.join(path,'new_Strm.txt'),'w', newline='')
    return outputIndx, outputStrm, currWD, inputPath, currOutputDir

def buildTable():
    vals = range(0,256)
    posDic = [[i, '{:02X}'.format(i)] for i in vals]
    negDic = [[i-255, '{:02X}'.format(i)] for i in vals]
    return posDic, negDic

def openOBJ(obj):
    #print(currPath)
    fpath = os.path.join(currWD,'input',obj)
    # print(fpath)
    f = open(fpath,'r')
    fraw = f.read()
    print('OBJ file loaded')
    return fraw

def listToString(listin):
    strOut = ' '.join(i for i in listin)
    return strOut 

def sortVF(objIn): # sort OBJ into vertices and faces
    objInSpl = objIn.split('\n')
    verts = []
    faces = []

    for i in objInSpl:
        j = i.split(' ')
        if j[0] == 'v':
            j.pop(0)
            verts.append(j)
        elif j[0] == 'f':
            j.pop(0)
            faces.append(j)
    print(f'Vertices ({len(verts)}) and Faces ({len(faces)}) sorted')
    return verts, faces

def convVF(vIn, fIn): # convert verts and faces to hex format
    vOut = []
    fOut = []
    for i in vIn: 
        #print(i)
        vHex = []
        for j in i:
            #print(j)
            vBytes = vToHex(j)
            for k in vBytes:
                vHex.append(k)
        vOut.append(vHex)
        
    for i in fIn:
        fHex = []
        for j in i:
            fBytes = fToHex(j)
            for k in fBytes:
                fHex.append(k)
        fOut.append(fHex)
    print('Converted all vertices and faces to RSF-compatible hex values')
    return vOut, fOut

def vToHex(vIn): # convert vert values to hex "bytes"

    bytesOut = ['00']*2 # oo dd
    (dP, oP)= math.modf(float(vIn))
    oP = abs(int(oP))  
    dfull = math.floor(dP*256)
    if dP >= 0: # decimal place greater than zero means positive value for overall vertex
        for sublist in posDic:
            if sublist[0] == oP:
                bytesOut[0] = sublist[1]
            if sublist[0] == dfull:
                bytesOut[1] = sublist[1]
    elif dP < 0: #decimal place less than zero means negative value for overall vertex
        for sublist in negDic:
            if sublist[0] == int(oP*-1):
                bytesOut[0] = sublist[1]
            if sublist[0] == dfull:
                bytesOut[1] = sublist[1]
    
    return bytesOut
    
def fToHex(fIn): # convert face values to hex "bytes
    bytesOut = ['00']*2 # short for each face point
    p = int(fIn)-1
    #print(p)
    if p <= 255:   
        bytesOut[0] = '00'
        for sublist in posDic:
            if sublist[0] == p:
                    bytesOut[1] = sublist[1]
    else:
        f = divmod(p,256)
        #print(f'matching hex for {f[0]}')
        for sublist in posDic:
            if sublist[0] == f[0]:
                bytesOut[0] = sublist[1]
        #print(f'matching hex for {f[1]}')
        for sublist in posDic:
            if sublist[0] == f[1]:
                bytesOut[1] = sublist[1]
    return bytesOut
    
def fWrapper(fIn):
    fFull = []
    indHead = '49 4e 44 58 00 00 00 00 00 00 00' # fixed portion of INDX header
    indHeadid16 = '49 44 31 36' # 'ID16' end of INDX header
    
    # convert list of lists of faces into list of "bytes"
    for i in fIn:
        for j in i:
            fFull.append(j)
    
    ## build header
    indxLen = len(fIn) # get total number of faces
    iLenStr = '{0:04x}'.format(indxLen) # format total to 2 bytes
    indxLenBytes = f'{iLenStr[0]}{iLenStr[1]} {iLenStr[2]}{iLenStr[3]}' # format hex to 2 bytes (ugly but it works lol)
    indxHeader = f'{indHead} {indxLenBytes} {indHeadid16}' # concat header
    
    fFullStr = listToString(fFull) # convert list of "bytes" into string

    indxOut = f'{indxHeader} {fFullStr}' # concat with header
    
    return indxOut

def vWrapper(vIn):

    strmHead = '53 54 52 4D 00 00 00 00 00 00 00' # fixed portion of STRM header
    
    ## build header
    vCnt = len(vIn) # get total number of VB
    vCntStr = '{0:04x}'.format(vCnt) # format total to 2 bytes
    vCntBytes = f'{vCntStr[0]}{vCntStr[1]} {vCntStr[2]}{vCntStr[3]}' # format hex to 2 bytes (ugly but it works lol)
    vBLen = 24 # decimal length of STRM VB
    vBLenByte = '{0:02x}'.format(vBLen)
    stHeader = f'{strmHead} {vCntBytes} 00 00 00 {vBLenByte} 00 00 00 00' # concat header
    
    ## build individual STRM VBs
    newStrm = listToString(ogToNewStrm(vIn))
    strmOut = f'{stHeader} {newStrm}'
    return strmOut

def indexRSF(rsfIn, currOutputDir):
    indexNames = ['STRM', 'INDX']
    
    def printCSVout(data):
                # print(data)
                writer.writerow(data)
                
    for i in indexNames:

        outputPath = os.path.join(currOutputDir,f'index_{i}_t1.csv') 
        rsfPath = os.path.join(inputPath, rsfIn)

        outputFile = open(outputPath,'w', newline='')
        writer = csv.writer(outputFile)
        header = [f'{i} Number', 'First Byte','hex','STRM Length']
        writer.writerow(header) 

        with open(rsfPath, 'r+b') as f:
            mm = mmap.mmap(f.fileno(), 0)
            byteIndex = 0
            lastByteIndex = 0
            strmIndex = 1
            bytesstrm = bytes(i, 'utf-8')
            rsfsize = mm.size()

            while byteIndex < rsfsize and lastByteIndex >= 0 :
                
                byteIndex = mm.find(bytesstrm, byteIndex+4, rsfsize)
                lastLength = byteIndex-lastByteIndex
                lastData = [f'{i}{strmIndex-1}', lastByteIndex, hex(lastByteIndex), lastLength]

                printCSVout(lastData)        
                
                lastByteIndex = byteIndex
                strmIndex += 1
            
            mm.close
    
    
    
######   



outputIndx, outputStrm, currWD, inputPath, currOutputDir = fileStuff()
    
posDic, negDic = buildTable()    

objIn = openOBJ(os.path.join(inputPath,blenderObj))

vSorted, fSorted = sortVF(objIn)

vHex, fHex = convVF(vSorted, fSorted)

indxOut = fWrapper(fHex)
strmOut = vWrapper(vHex)
print('indx and strm wrapped')

outputIndx.write(indxOut)
outputStrm.write(strmOut)
print('indx and strm written out!')

#indexRSF(rsfName, currOutputDir)