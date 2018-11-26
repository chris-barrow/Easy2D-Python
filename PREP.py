import numpy as np
from Rnode import Rnode
from Relem import Relem
from BC import BC


def PREP(inputfilename):
    """
    PREPROCESSOR
    """

    # inputfilename='TestCase2_2.dat';
    inputText = ""
    with open(inputfilename, 'r') as inputFile:
        inputText = inputFile.read().splitlines()
    outputFile = open('output.dat', 'w')

    # Check for required commands and grab index
    try:
        NODES_idx = inputText.index('NODES')
        # Grabs number of nodes and records from input file
        NNN = np.fromstring(inputText[NODES_idx+1], dtype=int, sep=',')
        NNODE = NNN[0]  # Gets number of nodes
        NREC = NNN[1]  # Gets number of records
    except Exception:
        print('Error on NODES Command')
        return

    try:
        ELEM_idx = inputText.index('ELEMENTS')
        # Gets number of elements and records
        EEE = np.fromstring(inputText[ELEM_idx+1], dtype=int, sep=',')
        NELEM = EEE[0]  # Number of elements
        EREC = EEE[1]   # Number of element records
    except Exception:
        print('Error on ELEMENTS Command')
        return

    try:
        BC_idx = inputText.index('BOUNDARY CONDITIONS')
        # Gets number of records for BCs
        BREC = np.fromstring(inputText[BC_idx+1], dtype=int, sep=',')[0]
    except Exception:
        print('Error on BOUNDARY CONDITIONS Command')
        return

    try:
        SOLVE_idx = inputText.index('SOLVE')
    except Exception:
        print('Error on SOLVE Command')
        return

    Field = 0
    Exterior = 0
    FREC = 0
    try:
        FIELD_idx = inputText.index('FIELD')
        FREC = np.fromstring(inputText[FIELD_idx+1], dtype=int, sep=',')[0]
        Field = 2
    except Exception:
        pass

    if 'EXTERIOR' in inputText:
        Exterior = 3
        if 'VINF' in inputText:
            VINF = np.fromstring(inputText[inputText.index('VINF')+1],
                                 dtype=int, sep=',')[0]

    outputFile.write('{}\n\n'.format(inputText[0]))
    nodes = np.zeros((NREC, 6))
    for i, node in enumerate(inputText[NODES_idx+2:NODES_idx+NREC+2]):
        nodes[i, :] = np.fromstring(node, sep=',')

    N1 = nodes[:, 0]
    N2 = nodes[:, 1]
    X1 = nodes[:, 2]
    Y1 = nodes[:, 3]
    X2 = nodes[:, 4]
    Y2 = nodes[:, 5]
    [X, Y] = Rnode(outputFile, NNODE, NREC, N1, N2, X1, Y1, X2, Y2)

    elements = np.zeros((EREC, 4))
    for j, elem in enumerate(inputText[ELEM_idx+2:ELEM_idx+EREC+2]):
        elements[j, :] = np.fromstring(elem, sep=',')

    NODEI = elements[:, 0].astype(int)
    NODEL = elements[:, 1].astype(int)
    NUMBER = elements[:, 2].astype(int)
    KINDI = elements[:, 3].astype(int)
    [NODE, KIND] = Relem(outputFile, NNODE, NELEM, EREC, NODEI, NODEL, NUMBER,
                         KINDI)

    bcs = np.zeros((BREC, 6))
    for k, bc in enumerate(inputText[BC_idx + 2:BC_idx+BREC+2]):
        bcs[k, :] = np.fromstring(bc, sep=',')

    K1 = bcs[:, 0].astype(int) - 1
    K2 = bcs[:, 1].astype(int) - 1
    NOD = bcs[:, 2].astype(int)
    CA1 = bcs[:, 3]
    CB1 = bcs[:, 4]
    CC1 = bcs[:, 5]
    [TEMP, CA, CB, CC] = BC(outputFile, NNODE, NELEM, NODE, KIND, BREC, K1, K2,
                            NOD, CA1, CB1, CC1)

    if Field == 2:
        FIELDS = np.zeros((FREC, 2))
        for l, FIELD in enumerate(inputText[FIELD_idx+2:FIELD_idx+FREC+2]):
            FIELDS[l, :] = np.fromstring(FIELD, sep=',')

        Px = FIELDS[:, 0]
        Py = FIELDS[:, 1]

    return [outputFile, NNODE, NELEM, X, Y, NODE, KIND, TEMP, CA, CB, CC, FREC,
            Field, Exterior, Px, Py, VINF]
