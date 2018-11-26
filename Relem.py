import numpy as np


def Relem(fid2, NNODE, NELEM, EREC, NODEI, NODEL, NUMBER, KINDI):
    ########################################################################
    #     INPUT:                                                           #
    #     NELEM =NUMBER OF ELEMENTS                                        #
    #     NREC =NUMBER OF ELEMENT DATA RECORDS                             #
    #     NODEI =NODAL POINT NUMBER FOR THE FIRST NODE IN CURRENT RECORD   #
    #     NODEL =NODAL POINT NUMBER FOR THE LAST NODE IN CURRENT RECORD    #
    #     NUMBER =NUMBER OF ELEMENTS TO BE GENERATED IN THIS RECORD        #
    #     KINDI =1     LINEAR ELEMENTS                                     #
    #           =2     QUADRATIC ELEMENTS                                  #
    #           =3     CUBIC ELEMENTS                                      #
    #                                                                      #
    #     OUTPUT:                                                          #
    #     KIND = 1xNELEM matrix with order of each element                 #
    #     NODE = max(KIND)xNELEM matrix that gives nodes for each element  #
    #     NODE ex: For a set of alternating linear and quadratic elements: #
    #     [ 1  2  4  5  7  8  ]                                            #
    #     [ 2  3  5  6  8  9  ]                                            #
    #     [ 0  4  0  7  0  10 ]                                            #
    #     KIND ex:                                                         #
    #     [ 1  2  1  2  1  2  ]                                            #
    ########################################################################

    NODE = np.zeros((max(KINDI)+1, sum(NUMBER)))
    NE = 1 - NUMBER[0]
    for NR in range(0, EREC):
        if NR == 0:
            HH = 0
        else:
            HH = NR - 1

        NE = NE + NUMBER[HH]

        # Checks to make sure the element order is valid
        if (KINDI[NR] < 1) or (KINDI[NR] > 3):
            print('----ERROR IN ELEMENT DATA-----')
            return

        # Checks for node numbers out of range
        if (NODEI[NR] < 1) or (NODEI[NR] > NNODE):
            print('----ERROR IN ELEMENT DATA-----')
            return

        #
        if (NUMBER[NR] < 1) or ((NE+NUMBER[NR]-1) > 200):
            print('----ERROR IN ELEMENT DATA-----')
            return

        INCREM = 0
        KIND = np.zeros(sum(NUMBER))
        for I in range(NE-1, NE+NUMBER[NR]-1):
            KIND[I] = KINDI[NR]
            n1 = NODEI[NR] + INCREM
            for J in range(0, KINDI[NR]+1):
                NODE[J, I] = n1 + J - 1
                if NODE[J, I] > NNODE-1:
                    NODE[J, I] = 0

            INCREM = INCREM + KINDI[NR]

        if NODEI[NR] > NODEL[NR]:
            NODE[KINDI[NR]+1, NE+NUMBER[NR]-1] = NODEL[NR]

    KIND = KIND.astype(int)
    fid2.write('\n {}  \n \n'.format('ELEMENT CONNECTIVITY:'))
    for I in range(0, NELEM):
        if KIND[I] == 1:
            fid2.write('{} {}  \t {} {} \t {} {} {} '
                       '\n'.format('ELEMENT #', I+1, 'DEGREE=', KIND[I],
                                   'NODES=', NODE[0, I], NODE[1, I]))

        if KIND[I] == 2:
            fid2.write('{} {} \t {} {} \t'
                       '{} {}  {}  {} \n'.format('ELEMENT #', I+1, 'DEGREE=',
                                                 KIND[I], 'NODES=', NODE[0, I],
                                                 NODE[1, I], NODE[2, I]))

        if KIND[I] == 3:
            fid2.write('{} {}  \t {} {} \t {} {}'
                       '{}  {}  {} \n'.format('ELEMENT #', I+1, 'DEGREE=',
                                              KIND[I], 'NODES=',
                                              NODE[0, I], NODE[1, I],
                                              NODE[2, I], NODE[3, I]))

    return [NODE, KIND]
