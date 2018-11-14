function [TEMP,CA,CB,CC]=BC(fid2, NNODE, NELEM, NODE, KIND, BREC,K1,K2,NOD,CA1,CB1,CC1)
BIG=1.0e15;
TEMP=zeros(1,NNODE);
DTDN=zeros(4,NELEM);
CA=zeros(4,NELEM);
CB=zeros(4,NELEM);
CC=zeros(4,NELEM);
for I=1:NNODE
    TEMP(I)=BIG;
end
for J=1:4
    for K=1:NELEM
        DTDN(J,K)=BIG;
        CA(J,K)=BIG;
        CB(J,K)=BIG;
        CC(J,K)=BIG;
    end
end
[CA, CB, CC]= Rbc(BREC,KIND,K1,K2,NOD,CA1,CB1,CC1);
%ALARM='FALSE';
for K=1:NELEM
    KINDI=KIND(K);
    for J=1:KINDI+1
        NOD=NODE(J,K);
        if(CA(J,K)==BIG) && (CB(J,K)==BIG)
            fprintf(fid2,'%s  %i \n', 'B.C. NOT SPECIFIED ON ELEMENT #',K);
            %ALARM='TRUE';
        end
        if(CA(J,K)==0) && (CB(J,K)==0)
            fprintf(fid2,'%s  %i \n', 'CA=0 AND CB=0 ON ELEMENT #',K);
            %ALARM='TRUE';
        end
        if(CB(J,K)==0)
            TM=TEMP(NOD);
            TP=CC(J,K)/CA(J,K);
            TEMP(NOD)=TP;
            if(TM~=BIG) && (TP~=TM)
                fprintf(fid2,'%s  %i \n', 'MORE THAN ONE TEMP. AT NODE #',K);
                %ALARM='TRUE';
            end
        end
    end
end
fprintf(fid2,'\n %s  \n \n', 'BOUNDARY CONDITIONS:');
for K=1:NELEM
    KINDI=KIND(K);
    fprintf(fid2,'%s  %i \n', 'ELEMENT #', K);
    for J=1:KINDI+1
        fprintf(fid2,'%s %i \t %s  %3.3f  %s  %3.3f  %s %3.3f \n', 'LOCAL NODE # ',J ,'CA=', CA(J,K), 'CB=', CB(J,K), 'CC=', CC(J,K));
    end
end
end

