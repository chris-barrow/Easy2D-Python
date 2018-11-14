clc;
clear;
[XI,W]= SETINT();
n=4;
out=0;
a=0;
b=2;

for i=1:n
    x= (a+b)/2+(b-a)/2*(XI(i,n/2));
    fun =4*x^7-x^6+8;
    out = out + (b-a)/2*W(i,n/2)*fun;
end

syms y; 
ExactOut= double(int(4*y^7-y^6+8,0,2));
