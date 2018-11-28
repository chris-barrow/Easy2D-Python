import numpy as np


def Rnode(outputFile, NNODE, NREC, N1, N2, X1, Y1, X2, Y2):
    X = np.zeros((NNODE, 1))
    Y = np.zeros((NNODE, 1))
    for NR in range(0, NREC):
        #######################################################################
        #                                                                     #
        #     NNODE =NUMBER OF NODES                                          #
        #     NREC =NUMBER OF NODAL POINT DATA RECORDS                        #
        #     N1,N2 =NODAL POINT NUMBERS FOR THE FIRST AND THE LAST NODES     #
        #     X1,Y1 =COORDINATES OF NODE #N1(NREC)                            #
        #     X2,Y2 =COORDINATES OF NODE #N2(NREC)                            #
        #                                                                     #
        #######################################################################
        if N1[NR] == N2[NR]:
            X[int(N1[NR])-1] = X1[NR]
            Y[int(N1[NR])-1] = Y1[NR]
        else:
            DN = N2[NR] - N1[NR]
            DX = (X2[NR] - X1[NR])/DN
            DY = (Y2[NR] - Y1[NR])/DN
            XX = X1[NR] - DX
            YY = Y1[NR] - DY
            for I in range(int(N1[NR]) - 1, int(N2[NR])):
                XX = XX+DX
                YY = YY+DY
                X[I] = XX
                Y[I] = YY

    outputFile.write('{}\n\n'.format('NODAL POINT COORDINATES:'))
    for I in range(0, NNODE):
        outputFile.write('{} {:d} \t {} {:3.3f} \t {} {:3.3f} \n'.format(
            'NODE # ', I+1, 'X=', float(X[I]), 'Y=', float(Y[I])))

    return [X, Y]
