import numpy as np


def Relem(fid2, NNODE, NELEM, EREC, NODEI, NODEL, NUMBER, KINDI):
    NODE = np.zeros(max(KINDI), sum(NUMBER))
    NE = 1 - NUMBER[1]
    for NR in range(0, EREC):
        if NR == 0:
            HH = 1
        else:
            HH = NR - 1

        NE = NE + NUMBER(HH)
        #######################################################################
        #                                                                     #
        #     NELEM =NUMBER OF ELEMENTS                                       #
        #     NREC =NUMBER OF ELEMENT DATA RECORDS                            #
        #     NODEI =NODAL POINT NUMBER FOR THE FIRST NODE IN CURRENT RECORD  #
        #     NODEL =NODAL POINT NUMBER FOR THE LAST NODE IN CURRENT RECORD   #
        #     NUMBER =NUMBER OF ELEMENTS TO BE GENERATED IN THIS RECORD       #
        #     KINDI =1     LINEAR ELEMENTS                                    #
        #           =2     QUADRATIC ELEMENTS                                 #
        #           =3     CUBIC ELEMENTS                                     #
        #                                                                     #
        #######################################################################
        if (KINDI(NR) < 1) or (KINDI(NR) > 3):
            print('----ERROR IN ELEMENT DATA-----')
            return

        if (NODEI(NR) < 1) or (NODEI(NR) > NNODE):
            print('----ERROR IN ELEMENT DATA-----')
            return

        if (NUMBER(NR) < 1) or ((NE+NUMBER(NR)-1) > 200):
            print('----ERROR IN ELEMENT DATA-----')
            return

        INCREM = 0
        KIND = []
        for I in range(NE, NE+NUMBER[NR]-1):
            KIND[I] = KINDI[NR]
            n1 = NODEI[NR] + INCREM
            for J in range(1, KINDI(NR)+1):
                NODE[J, I] = n1 + J - 1
                if NODE[J, I] > NNODE:
                    NODE[J, I] = 1

            INCREM = INCREM + KINDI[NR]

        if NODEI[NR] > NODEL[NR]:
            NODE[KINDI[NR]+1, NE+NUMBER[NR]-1] = NODEL[NR]

    fid2.write('\n {}  \n \n'.format('ELEMENT CONNECTIVITY:'))
    for I in range(0, NELEM):
        if KIND[I] == 1:
            fid2.write('{} {}  \t {} {} \t'
                       '{} {} {} \n'.format('ELEMENT #', I, 'DEGREE=', KIND(I),
                                            'NODES=', NODE(1, I), NODE(2, I)))

        if KIND[I] == 2:
            fid2.write('{} {} \t {} {} \t'
                       '{} {}  {}  {} \n'.format('ELEMENT #', I, 'DEGREE=',
                                                 KIND(I), 'NODES=', NODE(1, I),
                                                 NODE(2, I), NODE(3, I)))

        if KIND[I] == 3:
            fid2.write('{} {}  \t {} {} \t'
                       '{} {}  {}  {}  {} \n'.format('ELEMENT #', I, 'DEGREE=',
                                                     KIND(I), 'NODES=',
                                                     NODE(1, I), NODE(2, I),
                                                     NODE(3, I), NODE(4, I)))

    return [NODE, KIND]
