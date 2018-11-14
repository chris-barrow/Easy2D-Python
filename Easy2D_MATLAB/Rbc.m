function [CA, CB, CC]=Rbc(BREC,KIND,K1,K2,NOD,CA1,CB1,CC1)
for I=1:BREC
    JS=NOD(I);
    JE=NOD(I);
    for K=K1(I):K2(I)
        KINDI=KIND(K);
        if(NOD(I)==0)
            JS=1;
            JE=KINDI+1;
        end
        for J=JS:JE
            CA(J,K)=CA1(I);
            CB(J,K)=CB1(I);
            CC(J,K)=CC1(I);
        end
    end
end
end

