import numpy as np


def BC(fid2, NNODE, NELEM, NODE, KIND, BREC, K1, K2, NOD, CA1, CB1, CC1):
    BIG = 1.0e15
    TEMP = np.zeros((1, NNODE))
    DTDN = np.zeros((4, NELEM))
    CA = np.zeros((4, NELEM))
    CB = np.zeros((4, NELEM))
    CC = np.zeros((4, NELEM))
    for I in range(1, NNODE):
        TEMP[I] = BIG

    for J in range(0, 3):
        for K in range(0, NELEM):
            DTDN[J, K] = BIG
            CA[J, K] = BIG
            CB[J, K] = BIG
            CC[J, K] = BIG

    [CA, CB, CC] = Rbc(BREC, KIND, K1, K2, NOD, CA1, CB1, CC1, CA, CB, CC)
    # ALARM='FALSE'
    for K in range(1, NELEM):
        KINDI = KIND[K]
        for J in range(1, KINDI+1):
            NOD = NODE[J, K]
            if CA[J, K] == BIG and CB[J, K] == BIG:
                fid2.write('{} {} \n'.format('B.C. NOT SPECIFIED ON ELEMENT #',
                                             K))
                # ALARM='TRUE'

            if CA[J, K] == 0 and CB[J, K] == 0:
                fid2.write('{}  {} \n'.format('CA=0 AND CB=0 ON ELEMENT #', K))
                # ALARM='TRUE'

            if CB[J, K] == 0:
                TM = TEMP[NOD]
                TP = CC[J, K]/CA[J, K]
                TEMP[NOD] = TP
                if TM != BIG and TP != TM:
                    fid2.write('{}  {} \n'.format('MORE THAN ONE TEMP. '
                                                  'AT NODE #', K))
                    # ALARM='TRUE'

    fid2.write('\n {}  \n \n'.format('BOUNDARY CONDITIONS:'))
    for K in range(0, NELEM):
        KINDI = KIND[K]
        fid2.write('{}  {} \n'.format('ELEMENT #', K))
        for J in range(0, KINDI+1):
            fid2.write('{} {} \t {}  {3.3f}  {}  {3.3f}  {} {3.3f} \n'.format(
                'LOCAL NODE # ', J, 'CA=', CA[J, K], 'CB=', CB[J, K], 'CC=',
                CC[J, K]))

    return [TEMP, CA, CB, CC]


def Rbc(BREC, KIND, K1, K2, NOD, CA1, CB1, CC1, CA, CB, CC):
    for I in range(1, BREC):
        JS = NOD[I]
        JE = NOD[I]
        for K in range(K1[I], K2[I]):
            KINDI = KIND[K]
            if NOD[I] == 0:
                JS = 1
                JE = KINDI + 1

            # CA = np.zeros(
            for J in range(JS, JE):
                CA[J, K] = CA1[I]
                CB[J, K] = CB1[I]
                CC[J, K] = CC1[I]

    return [CA, CB, CC]
