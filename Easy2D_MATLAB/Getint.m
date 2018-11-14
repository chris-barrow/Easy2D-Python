function [NINP, XII, WT] = Getint(KINDI,XI,W)
%
%-----SELECT GAUSSIAN INTEGRATION POINTS
%
if(KINDI==1)
    NINP=4;
else
    if(KINDI==2)
        NINP=6;
    else
        NINP=8;
    end
end
NARRAY=NINP/2;
XII=zeros(NINP,NARRAY);
WT=zeros(NINP,NARRAY);
for I=1:NINP
    XII(I)=XI(I,NARRAY);
    WT(I)=W(I,NARRAY);
end
end

