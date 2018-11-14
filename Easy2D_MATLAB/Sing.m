function [CP,G,H,QN]=Sing(XP,YP,NL,KINDI,XQ,YQ,XI,W,ISING,XIPMAP,CP,Exterior)
%
%---- CALL SETMAP in the EASY2D to set up XIPMAP(4,3) first
%
C1=-1/(2*pi);
H=zeros(1,NL);
G=zeros(1,NL);
[NINP, ETA, WT] = Getint(KINDI,XI,W);
XIP=XIPMAP(ISING, KINDI);
%
%---- THIS LOOP IS FOR THE PURPOSE OF INTEGRATING TO THE RIGHT OF P
%
if(XIP~=1)
    for INP=1:NINP
        A=sqrt(1-XIP)/2;
        Z=A+A*ETA(INP);
        XII=Z^2+XIP;
        [PSI,DPSI]=Shape(XII,KINDI);
        XX=0;
        YY=0;
        DXDS=0;
        DYDS=0;
        for I=1:NL
            XX=XX+XQ(I)*PSI(I);
            YY=YY+YQ(I)*PSI(I);
            DXDS=DXDS+XQ(I)*DPSI(I);
            DYDS=DYDS+YQ(I)*DPSI(I);
        end
        JAC=sqrt(DXDS^2+DYDS^2);
        RX=XX-XP;
        RY=YY-YP;
        R=sqrt(RX^2+RY^2);
        QN(1)=(-1)^(Exterior)*DYDS/JAC;
        QN(2)=-(-1)^(Exterior)*DXDS/JAC;
        DRDN=(QN(1)*RX+QN(2)*RY)/R;
        DZDE=(sqrt(1-XIP))/2;
        GREEN=C1*log(R)*JAC*2*Z*DZDE*WT(INP);
        DGDN=C1*DRDN/R*JAC*2*Z*DZDE*WT(INP);
        for I=1:NL
            G(I)=G(I)+PSI(I)*GREEN;
            H(I)=H(I)+PSI(I)*DGDN;
        end
        CP=CP-DGDN;
    end
end
%
%*** THIS LOOP IS FOR THE PURPOSE OF INTEGRATING TO THE LEFT OF P
%
if(XIP~=(-1))
    for INP=1:NINP
        A=sqrt(1+XIP)/2;
        Z=A+A*ETA(INP);
        XII=XIP-Z^2;
        [PSI,DPSI]=Shape(XII,KINDI);
        XX=0;
        YY=0;
        DXDS=0;
        DYDS=0;
        for I=1:NL
            XX=XX+XQ(I)*PSI(I);
            YY=YY+YQ(I)*PSI(I);
            DXDS=DXDS+XQ(I)*DPSI(I);
            DYDS=DYDS+YQ(I)*DPSI(I);
        end
        JAC=sqrt(DXDS^2+DYDS^2);
        RX=XX-XP;
        RY=YY-YP;
        R=sqrt(RX^2+RY^2);
        QN(1)=(-1)^(Exterior)*DYDS/JAC;
        QN(2)=-(-1)^(Exterior)*DXDS/JAC;
        DRDN=(QN(1)*RX+QN(2)*RY)/R;
        DZDE=(sqrt(1+XIP))/2;
        GREEN=C1*log(R)*JAC*2*Z*DZDE*WT(INP);
        DGDN=C1*DRDN/R*JAC*2*Z*DZDE*WT(INP);
        for I=1:NL
            G(I)=G(I)+PSI(I)*GREEN;
            H(I)=H(I)+PSI(I)*DGDN;
        end
        CP=CP-DGDN;
    end
end
end

