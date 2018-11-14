function [DTDN,TEMP]=Solout(fid2,NNODE, NELEM, KIND, NODE, CP, TEMP, CA, CB, CC, XS,Exterior)
%
%   IDENTIFY THE SOLUTION VECTOR
%
BIG=1.0e15;
DTDN=zeros(4,NELEM);
for I=1:NNODE
    if (TEMP(I)==BIG)
        TEMP(I)=XS(I);
    end
end
for K=1:NELEM
    NL=KIND(K)+1;
    for J=1:NL
        NOD=NODE(J,K);
        if(CB(J,K)==0.0)
            DTDN(J,K)=XS(NOD);
        else
            DTDN(J,K)=(CC(J,K)-CA(J,K)*TEMP(NOD))/CB(J,K);
        end
    end
end
fprintf(fid2,'\n %s \n \n', 'CP ON THE NODES:');
for I=1:NNODE
    fprintf(fid2,'%s  %i  %s   %15.3f \n', 'NODE #', I, 'CP=', CP(I));
end
if Exterior~=3
    fprintf(fid2,'\n %s  \n \n', 'TEMPERATURE ON THE BOUNDARY:');
    ss='TEMP=';
else
    fprintf(fid2,'\n %s  \n \n', 'PHI ON THE BOUNDARY:');
    ss='PHI=';
end
for I=1:NNODE
    fprintf(fid2,'%s  %i  %s   %15.3f \n', 'NODE #', I, ss, TEMP(I));
end
if Exterior~=3
fprintf(fid2,'\n %s \n \n','DTDN ON THE BOUNDARY:');
hh='DTDN=';
else
    fprintf(fid2,'\n %s \n \n','VELOCITY ON THE BOUNDARY:');
    hh='V=';
end
for K=1:NELEM
    if KIND(K)==1
        fprintf(fid2,'%s %i  \t %s  %15.3f  %15.3f \n', 'ELEMENT # ',K ,hh,DTDN(1,K), DTDN(2,K));
    end
    if KIND(K)==2
        fprintf(fid2,'%s %i  \t %s  %15.3f  %15.3f  %15.3f \n', 'ELEMENT # ',K ,hh,DTDN(1,K), DTDN(2,K), DTDN(3,K) );
    end
    if KIND(K)==3
        fprintf(fid2,'%s %i  \t %s  %15.3f  %15.3f  %15.3f  %15.3f \n', 'ELEMENT # ',K ,hh,DTDN(1,K), DTDN(2,K),DTDN(3,K),DTDN(4,K) );
    end
end
end