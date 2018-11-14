function [X,Y]= Rnode(fid2,NNODE,NREC,N1,N2,X1,Y1,X2,Y2)
X=zeros(4,1);
Y=zeros(4,1);
for NR=1:NREC
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    %                                                                      %
    %     NNODE =NUMBER OF NODES                                           %
    %     NREC =NUMBER OF NODAL POINT DATA RECORDS                         %
    %     N1,N2 =NODAL POINT NUMBERS FOR THE FIRST AND THE LAST NODES      %
    %     X1,Y1 =COORDINATES OF NODE #N1(NREC)                             %
    %     X2,Y2 =COORDINATES OF NODE #N2(NREC)                             %
    %                                                                      %
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    if(N1(NR)==N2(NR))
        X(N1(NR))=X1(NR);
        Y(N1(NR))=Y1(NR);
    else
        DN=N2(NR)-N1(NR);
        DX=(X2(NR)-X1(NR))/DN;
        DY=(Y2(NR)-Y1(NR))/DN;
        XX=X1(NR)-DX;
        YY=Y1(NR)-DY;
        for I=N1(NR):N2(NR)
            XX=XX+DX;
            YY=YY+DY;
            X(I)=XX;
            Y(I)=YY;
        end
    end
end
fprintf(fid2,'%s  \n \n', 'NODAL POINT COORDINATES:');
for I=1:NNODE
    fprintf(fid2,'%s %i \t %s %3.3f \t %s %3.3f  \n', 'NODE # ',I ,'X=', X(I), 'Y=', Y(I));
end
end

