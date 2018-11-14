function [CP,A,B,QN]=Form(NNODE,NELEM,NODE,KIND,X,Y,TEMP,XI,W,XIPMAP,CA,CB,CC,Exterior,PhiI)
BIG=1.0e15;
B=zeros(1,NNODE);
A=zeros(NNODE);
%
%  P LOOP
%
CP=zeros(1,NNODE);
if Exterior==3
    CP=ones(1,NNODE);
end
for IP=1:NNODE
    XP=X(IP);
    YP=Y(IP);
    %
    %  ELEMENT LOOP
    %
    for K=1:NELEM
        KINDI=KIND(K);
        NL=KINDI+1;
        ISING=0;
        for J=1:NL
            IQ=NODE(J,K);
            if(IQ==IP)
                ISING=J;
            end
            XQ(J)=X(IQ);
            YQ(J)=Y(IQ);
        end
        if(ISING==0)
            [CP(IP),G,H,QN]= Elemt(XP,YP,NL,KINDI,XQ,YQ,XI,W,CP(IP),Exterior);
        else
            [CP(IP),G,H,QN]= Sing(XP,YP,NL,KINDI,XQ,YQ,XI,W,ISING,XIPMAP,CP(IP),Exterior);
        end
        [A,B]= Assmb(K,NL,H,G,IP,NODE,TEMP,CA,CB,CC,A,B);
    end
    %
    %   Contribution from C(P)
    %
    if(TEMP(IP)==BIG)
        A(IP,IP)=A(IP,IP)+CP(IP);
    else
        B(IP)=B(IP)-CP(IP)*TEMP(IP);
    end
    B(IP)=B(IP)+PhiI(IP);
end
end

