function [NODE, KIND]=Relem(fid2,NNODE,NELEM,EREC,NODEI,NODEL,NUMBER,KINDI)
NODE=zeros(max(KINDI),sum(NUMBER));
NE=1-NUMBER(1);
for NR=1:EREC
    if NR==1
        HH=1;
    else
        HH=NR-1;
    end
    NE=NE+NUMBER(HH);
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    %                                                                      %
    %     NELEM =NUMBER OF ELEMENTS                                        %
    %     NREC =NUMBER OF ELEMENT DATA RECORDS                             %
    %     NODEI =NODAL POINT NUMBER FOR THE FIRST NODE IN CURRENT RECORD   %
    %     NODEL =NODAL POINT NUMBER FOR THE LAST NODE IN CURRENT RECORD    %
    %     NUMBER =NUMBER OF ELEMENTS TO BE GENERATED IN THIS RECORD        %
    %     KINDI =1     LINEAR ELEMENTS                                     %
    %           =2     QUADRATIC ELEMENTS                                  %
    %           =3     CUBIC ELEMENTS                                      %
    %                                                                      %
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    if (KINDI(NR) < 1) || (KINDI(NR) > 3)
        disp( '----ERROR IN ELEMENT DATA-----');
        return
    end
    if (NODEI(NR) < 1) || (NODEI(NR) > NNODE)
        disp( '----ERROR IN ELEMENT DATA-----');
        return
    end
    if (NUMBER(NR) < 1) || ((NE+NUMBER(NR)-1) > 200)
        disp( '----ERROR IN ELEMENT DATA-----');
        return
    end
    INCREM=0;
    for I=NE:NE+NUMBER(NR)-1
        KIND(I)=KINDI(NR);
        n1=NODEI(NR)+INCREM;
        for J=1:KINDI(NR)+1
            NODE(J,I)=n1+J-1;
            if NODE(J,I)>NNODE
                NODE(J,I)=1;
            end
        end
        INCREM=INCREM+KINDI(NR);
    end
    if(NODEI(NR) > NODEL(NR))
        NODE(KINDI(NR)+1,NE+NUMBER(NR)-1)=NODEL(NR);
    end
end
fprintf(fid2,'\n %s  \n \n', 'ELEMENT CONNECTIVITY:');
for I=1:NELEM
    if KIND(I)==1
        fprintf(fid2,'%s %i  \t %s %i \t %s %i  %i \n', 'ELEMENT # ',I ,'DEGREE=', KIND(I), 'NODES=', NODE(1,I), NODE(2,I));
    end
    if KIND(I)==2
        fprintf(fid2,'%s %i  \t %s %i \t %s %i  %i  %i \n', 'ELEMENT # ',I ,'DEGREE=', KIND(I), 'NODES=', NODE(1,I), NODE(2,I), NODE(3,I));
    end
    if KIND(I)==3
        fprintf(fid2,'%s %i  \t %s %i \t %s %i  %i  %i  %i \n', 'ELEMENT # ',I ,'DEGREE=', KIND(I), 'NODES=', NODE(1,I), NODE(2,I), NODE(3,I), NODE(4,I));
    end
end
end

