import numpy as np

def PREP(inputfilename):
    """
    PREPROCESSOR
    """

    # inputfilename='TestCase2_2.dat';
    InputText = ""
    with open(inputfilename, 'r') as inputFile:
        inputText = inputFile.read().splitlines()
    outputFile = open('output.dat','w')

    # Check for required commands and grab index
    try:
        NODES_idx = inputText.index('NODES')
        NNN = np.fromstring(inputText[NODES_idx+1], dtype=int, sep=',') # Grabs number of nodes and records from input file
        NNODE = NNN[1] # Gets number of nodes
        NREC = NNN[2] # Gets number of records
    except e:
        print('Error on NODES Command')
        return e

    try:
        ELEM_idx = inputText.index('ELEMENTS')
        EEE = np.fromstring(inputText[ELEM_idx+1], dtype=int, sep=',') # Gets number of elements and records
        NELEM = EEE[1] # Number of elements
        EREC = EEE[2] # Number of element records
    except e:
        print('Error on ELEMENTS Command')
        return e

    try:
        BC_idx = inputText.index('BOUNDARY CONDITIONS')
        BREC = np.fromstring(inputText[BC_idx+1], dtype=int, sep=',') # Gets number of records for BCs
    except e:
        print('Error on BOUNDARY CONDITIONS Command')
        return e

    try:
        SOLVE_idx = inputText.index('SOLVE')
    except e:
        print('Error on SOLVE Command')
        return e

    Field = 0
    Exterior = 0
    FREC = 0
    try:
        FIELD_idx = inputText.index('FIELD')
        FREC = np.fromstring(inputText[FIELD_idx+1], dtype=int, sep=',')
        Field = 2
    except e:
        pass

    if 'EXTERIOR' in inputText:
        Exterior = 3
        if 'VINF' in inputText:
            VINF = np.fromstring(inputText[inputText.index('VINF')+1],
                                 dtype=int, sep=',')

    outputFile.write('{}\n\n'.format(inputText[0]))
    nodes = np.zeros((NREC,6))
    for i, node in enumerate(inputText[NODES_idx:NODES_idx+NREC+2]):
        nodes[i,:] = np.fromstring(node, sep=',')

    N1=nodes[:,1]
    N2=nodes[:,2]
    X1=nodes[:,3]
    Y1=nodes[:,4]
    X2=nodes[:,5]
    Y2=nodes[:,6]
    [X,Y]=Rnode(outputFile,NNODE,NREC,N1,N2,X1,Y1,X2,Y2)

    elements=np.zeros((EREC,4))
    for j, elem in enumerate(inputText[ELEM_idx+2:EREC+2]):
        elements[j,:] = np.fromstring(elem, sep=',')

    NODEI = elements[:,1]
    NODEL = elements[:,2]
    NUMBER = elements[:,3]
    KINDI = elements[:,4]
    [NODE, KIND] = Relem(outputFile, NNODE, NELEM, EREC, NODEI, NODEL, NUMBER,
                         KINDI)

    bcs = np.zeros((BREC,6))
    for k, BC in enumerate(inputText[BC_idx + 2:BC_idx+BREC+1]):
        bcs[k,:] = np.fromstring(BC, sep=',')

    K1 = bcs[:, 1]
    K2 = bcs[:,2]
    NOD = bcs[:,3]
    CA1 = bcs[:,4]
    CB1 = bcs[:,5]
    CC1 = bcs[:,6]
    [TEMP, CA, CB, CC] = BC(outputFile, NNODE, NELEM, NODE, KIND, BREC, K1, K2,
                            NOD, CA1, CB1, CC1)
    if Field == 2:
        FIELDS = np.zeros(FREC, 2)
        for l=10+NREC+EREC+BREC:10+NREC+EREC+BREC+FREC-1
            FIELDS(l-9-NREC-EREC-BREC,:)=str2num(BLOCK{l})

        Px=FIELDS(:,1)
        Py=FIELDS(:,2)

    return [outputFile,NNODE, NELEM, X, Y, NODE, KIND, TEMP, CA, CB, CC,FREC,Field, Exterior,Px,Py,VINF]
