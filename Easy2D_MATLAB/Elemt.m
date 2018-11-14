function [CP,G,H,QN]= Elemt(XP,YP,NL,KINDI,XQ,YQ,XI,W,CP,Exterior)
%
%  Formulate element coefficient matrices
%
C1=-1/(2*pi);
H=zeros(1,NL);
G=zeros(1,NL);
[NINP, XII, WT] = Getint(KINDI,XI,W);
%
%  Integration loop
%
for INP=1:NINP
    [PSI,DPSI]=Shape(XII(INP),KINDI);
    XX=0.0;
    YY=0.0;
    DXDS=0.0;
    DYDS=0.0;
    for I=1:NL
        XX=XX+XQ(I)*PSI(I);
        YY=YY+YQ(I)*PSI(I);
        DXDS=DXDS+XQ(I)*DPSI(I);
        DYDS=DYDS+YQ(I)*DPSI(I);
    end
    DETJ=sqrt(DXDS^2+DYDS^2);
    QN(1)=(-1)^(Exterior)*DYDS/DETJ;
    QN(2)=-(-1)^(Exterior)*DXDS/DETJ;
    RX=XX-XP;
    RY=YY-YP;
    R=sqrt(RX^2+RY^2);
    DRDN=(QN(1)*RX+QN(2)*RY)/R;
    ALOGR=log(R);
    GREEN=C1*ALOGR*DETJ*WT(INP);
    DGDN=C1*DRDN/R*DETJ*WT(INP);
    for I=1:NL
        H(I)=H(I)+PSI(I)*DGDN;
        G(I)=G(I)+PSI(I)*GREEN;
    end
    CP=CP-DGDN;
end
end

