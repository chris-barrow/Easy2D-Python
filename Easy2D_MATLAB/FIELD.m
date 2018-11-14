function [PhiP,dPhidPX,dPhidPY,QN]=FIELD(fid2,Px,Py,FREC,NNODE,NELEM,KIND,NODE,X,Y,TEMP,DTDN,XI,W,Exterior,VINF,PhiI)

PhiP=zeros(1,FREC);
dPhidPX=zeros(1,FREC);
dPhidPY=zeros(1,FREC);
PhiPI=zeros(1,FREC);
DPhidPXI=zeros(1,FREC);
DPhidPYI=zeros(1,FREC);

for IP=1:FREC
    
    XP=Px(IP);
    YP=Py(IP);
    
    CP=0;
    FPT=0;
    FPDX=0;
    FPDY=0;
    if Exterior==3
        CP=ones(1,NNODE);
%        TEMP=PhiI;
    end
    %
    %       ELEMENT LOOP
    %
    for K=1:NELEM
        KINDI=KIND(K);
        NL=KINDI+1;
        for J=1:NL
            IQ=NODE(J,K);
            XQ(J)=X(IQ);
            YQ(J)=Y(IQ);
            TEMQ(J)=TEMP(IQ);
            DTDQ(J)=DTDN(J,K);
        end
        
        %
        %      INTERPOLATION
        %
        
        C1=-1/(2*pi);
        [NINP, XII, WT] = Getint(KINDI,XI,W);
        for INP=1:NINP
            [PSI,DPSI]=Shape(XII(INP),KINDI);
            XX=0;
            YY=0;
            DXDS=0;
            DYDS=0;
            TEM=0;
            DTN=0;
            for I=1:NL
                XX=XX+XQ(I)*PSI(I);
                YY=YY+YQ(I)*PSI(I);
                DXDS=DXDS+XQ(I)*DPSI(I);
                DYDS=DYDS+YQ(I)*DPSI(I);
                TEM=TEM+TEMQ(I)*PSI(I);
                DTN=DTN+DTDQ(I)*PSI(I);
            end
            DETJ=sqrt(DXDS^2+DYDS^2);
            QN(1)=(-1)^(Exterior)*DYDS/DETJ;
            QN(2)=-(-1)^(Exterior)*DXDS/DETJ;
            RX=(XX-XP);
            RY=(YY-YP);
            R=sqrt(RX^2+RY^2);
            DRDN=(QN(1)*RX+QN(2)*RY)/R;
            ALOGR=log(R);
            GREEN=C1*ALOGR*DETJ*WT(INP);
            DGDN=C1*DRDN/R*DETJ*WT(INP);
            DRDX=RX/R;
            DRDY=RY/R;
            DGDX=-C1*DRDX/R*DETJ*WT(INP);
            DGDY=-C1*DRDY/R*DETJ*WT(INP);
            DXDGDN=C1/(R^2)*(2*DRDX*DRDN-QN(1))*DETJ*WT(INP);
            DYDGDN=C1/(R^2)*(2*DRDY*DRDN-QN(2))*DETJ*WT(INP);
            FPT=FPT+(GREEN*DTN-TEM*DGDN);
            FPDX=FPDX+(DGDX*DTN-TEM*DXDGDN);
            FPDY=FPDY+(DGDY*DTN-TEM*DYDGDN);
            CP=CP-DGDN;
        end
    end
    if Exterior~=3
        PhiP(IP)=FPT;
        dPhidPX(IP)=FPDX;
        dPhidPY(IP)=FPDY;
    else
        
        PhiPI(IP)=VINF*XP;
        DPhidPXI(IP)=VINF;
        DPhidPYI(IP)=0;
        PhiP(IP)=FPT+PhiPI(IP);
        dPhidPX(IP)=FPDX+DPhidPXI(IP);
        dPhidPY(IP)=FPDY+DPhidPYI(IP);
    end
        
   
end

    fprintf(fid2,'\n %s  \n \n', 'FIELD POINTS COORDINATES AND SOLUTIONS:');
    if Exterior~=3
    for K=1:FREC
        fprintf(fid2,'%s %i \t %s  %3.3f  %s  %3.3f   %s  %3.3f   %s  %3.3f   %s  %3.3f \n', 'FIELD POINT # ',K ,'X=', Px(K), 'Y', Py(K), 'Temperature=', PhiP(K), 'Flux(X)=', dPhidPX(K), 'Flux(Y)=', dPhidPY(K));
    end
    else
        for K=1:FREC
        fprintf(fid2,'%s %i \t %s  %3.3f  %s  %3.3f   %s  %3.3f   %s  %3.3f   %s  %3.3f \n', 'FIELD POINT # ',K ,'X=', Px(K), 'Y', Py(K), 'Phi=', PhiP(K), 'Velocity(X)=', dPhidPX(K), 'Velocity(Y)=', dPhidPY(K));
        end
    end
    
end