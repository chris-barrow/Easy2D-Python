clc;
clear;
[XI,W]= SETINT();
n=10;
out=0;
a=0;
b=3;

for i=1:n
    x= (a+b)/2+(b-a)/2*(XI(i,n/2));
    fun = log(x);
    out = out + (b-a)/2*W(i,n/2)*fun;
end

syms y; 
ExactOut= double(int(log(y),0,3));
