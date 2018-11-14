function [A,B]=Assmb(K,NL,H,G,IP,NODE,TEMP,CA,CB,CC,A,B)
BIG=1.0e15;
for J=1:NL
    IQ=NODE(J,K);
    if(TEMP(IQ)~=BIG)
        B(IP)=B(IP)-H(J)*TEMP(IQ);
        if(CB(J,K)~=0)
            B(IP)=B(IP)+G(J)*(CC(J,K)-CA(J,K)*TEMP(IQ))/CB(J,K);
        else
            A(IP,IQ)=A(IP,IQ)-G(J);
        end
    else
        A(IP,IQ)=A(IP,IQ)+H(J)+G(J)*CA(J,K)/CB(J,K);
        B(IP)=B(IP)+G(J)*CC(J,K)/CB(J,K);
    end
end
end
