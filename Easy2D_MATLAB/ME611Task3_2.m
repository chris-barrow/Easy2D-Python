clc
clear
R=2;
B=0;
NNODE=6;
NELEM=3;
NODE(1,1)=1;
NODE(2,1)=2;
NODE(3,1)=3;
NODE(1,2)=3;
NODE(2,2)=4;
NODE(3,2)=5;
NODE(1,3)=5;
NODE(2,3)=6;
NODE(3,3)=1;
X=[0,R*sqrt(2)/2,R,R*sqrt(2)/2,0,0]';
Y=[-R,-R*sqrt(2)/2,0,R*sqrt(2)/2,R,0]';
KIND=[2,2,2];
[XI,W]=SETINT();
DETJ=0;
QN=zeros(2,1);
CP=0;
XP=1;
YP=0;
C1=-(2*pi)^(-1);
for K=1:3
    KINDI=KIND(K);
    NL=KINDI+1;
    for J=1:NL
        IQ=NODE(J,K);
        XQ(J)=X(IQ);
        YQ(J)=Y(IQ);
    end
    [NINP, XII, WT] = Getint(KINDI,XI,W);
    for INP=1:NINP
        [PSI,DPSI]=Shape(XII(INP),KINDI);
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
        DETJ=sqrt(DXDS^2+DYDS^2);
        QN(1)=DYDS/DETJ;
        QN(2)=-DXDS/DETJ;
        RX=XX-XP;
        RY=YY-YP;
        R=sqrt(RX^2+RY^2);
        DRDN=(QN(1)*RX+QN(2)*RY)/R;
        DGDN=C1*DRDN/R*DETJ*WT(INP);
        CP=CP-DGDN;        
    end
    N(:,K)=[QN(1),QN(2)];
    B=B+DETJ;
end
Exact=R*(pi+2)
Boundary=2*B
N
CP

