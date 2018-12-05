import numpy as np


def BC(fid2, NNODE, NELEM, NODE, KIND, BREC, K1, K2, NOD, CA1, CB1, CC1):
    #############################################################
    #  K1  = FIRST ELEMENT TO CONSIDER                          #
    #  K2  = LAST ELEMENT TO CONSIDER                           #
    #  NOD = LOCAL NODE ON ELEMENT FOR BC TO BE APPLIED         #
    #        0 = ALL NODES                                      #
    #  CA1  = PHI COEFFICIENT                                   #
    #  CB1  = dPHI/dN COEFFICIENT                               #
    #  CC1  = CONSTANT COEFFICIENT                              #
    #                                                           #
    #  (CA)*PHI + (CB)*dPHI/dN = CC                             #
    #############################################################
    BIG = 1.0e15
#    rows = max(KIND) + 1
#    rows = max(KIND) 
    TEMP = np.full((1, NNODE), BIG)
    DTDN = np.full((4, NELEM), BIG)
    CA = np.full((4, NELEM), BIG)
    CB = np.full((4, NELEM), BIG)
    CC = np.full((4, NELEM), BIG)
#    CA = np.full((rows, NELEM), BIG)
#    CB = np.full((rows, NELEM), BIG)
#    CC = np.full((rows, NELEM), BIG)

    [CA, CB, CC] = Rbc(BREC, KIND, K1, K2, NOD, CA, CB, CC, CA1, CB1, CC1)
    # ALARM='FALSE'
    for K in range(NELEM):
        KINDI = KIND[K]
#        for J in range(KINDI+1):
        for J in range(KINDI):
            NOD = NODE[J, K]
            if CA[J, K] == BIG and CB[J, K] == BIG:
                fid2.write('{} {} \n'.format('B.C. NOT SPECIFIED ON ELEMENT #',
                                             K+1))
                # ALARM='TRUE'

            if CA[J, K] == 0 and CB[J, K] == 0:
                fid2.write('{}  {} \n'.format('CA=0 AND CB=0 ON ELEMENT #', K))
                # ALARM='TRUE'

            if CB[J, K] == 0:
                TM = TEMP[0,int(NOD)]
                TP = CC[J, K]/CA[J, K]
                TEMP[0,int(NOD)] = TP
                if TM != BIG and TP != TM:
                    fid2.write('{}  {} \n'.format('MORE THAN ONE TEMP. '
                                                  'AT NODE #', K))
                    # ALARM='TRUE'

    fid2.write('\n {}  \n \n'.format('BOUNDARY CONDITIONS:'))
    for K in range(NELEM):
        KINDI = KIND[K]
        fid2.write('{}  {} \n'.format('ELEMENT #', K+1))
        for J in range(KINDI+1):
            fid2.write('{} {} \t {} {:3.3f} {} {:3.3f} {} {:3.3f} \n'.format(
                'LOCAL NODE # ', J+1, 'CA=', CA[J, K], 'CB=', CB[J, K], 'CC=',
                CC[J, K]))

    return [TEMP, CA, CB, CC]


def Rbc(BREC, KIND, K1, K2, NOD, CA, CB, CC, CA1, CB1, CC1):
    for I in range(0, BREC):  # Indexing through each BC record
        JS = NOD[I]  # Start of node assignment per element
        JE = NOD[I]  # End of node assignment per element
        for K in range(K1[I], K2[I]+1):  # Indexing through each element
            KINDI = KIND[K]  # Get order of element
            if NOD[I] == 0:  # Checks to see if BC applies to all nodes
                JS = 1  # If so, specifies the start to be the first node
                JE = KINDI + 1  # Specifies end to be the last node of element
#                JE = KINDI  # Specifies end to be the last node of element

            for J in range(JS - 1, JE):  # Indexing through each node in elem
                CA[J, K] = CA1[I]  # Assigns input BCs to coefficient matrices
                CB[J, K] = CB1[I]
                CC[J, K] = CC1[I]

    return [CA, CB, CC]
