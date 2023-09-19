import os

obj = 'revospeedrobot_base.obj'

def openOBJ(obj):
    currPath = os.getcwd()
    print(currPath)
    fpath = os.path.join(currPath,'input',obj)
    # print(fpath)
    f = open(fpath,'r')
    fraw = f.read()
    # print(f'fraw: {fraw}')
    return fraw

def interpSTRMOG(strmIn):
    fl = [s for s in strmIn if s != '\n' and s != ' ']
    fl2 = [''.join(x) for x in zip(fl[0::2], fl[1::2])]
    
    vBStartInd = []
    strmList = []
    strmHead = []

    startind = 21
    
    vBStartInd.append(startind-4) # get first vb
    
    for i in range(len(fl2)-3):
        if fl2[i] == '13': # find first of four bytes
            if fl2[i+1] == '13' and fl2[i+2] == '13' and fl2[i+3] == '13': # find rest of bytes
                vBStartInd.append(i)
            else:
                continue
        else:
            continue
    # print(vBStartInd)
    
    for i in vBStartInd:
        strmList.append(fl2[i+4:i+28])    
    strmList.pop()
    return strmList
    
def ogToNewStrm(strmListNew):
    newLen = len(strmListNew)
    
    objRead = openOBJ(obj)
    strmListOG = interpSTRMOG(objRead)

    newSTRM = []
    
    for i in range(newLen):
        vbOG = strmListOG[i]
        vbNW = strmListNew[i]
        #print(f'original: {vbOG}')
        #print(f'new verts: {vbNW}')
        for j in range(len(vbNW)):
            vbOG[j] = vbNW[j]
        #print(f'newvb: {vbOG}')
        for k in vbOG:
            newSTRM.append(k)
        
    #print(newSTRM)
    return(newSTRM)
    

    