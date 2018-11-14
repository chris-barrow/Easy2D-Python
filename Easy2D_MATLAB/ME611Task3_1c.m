clc;
clear;
[XI,W]= SETINT();
n=12;
out=0;
a=0;
b=3;

for i=1:n
    x= (a+sqrt(b))/2+(sqrt(b)-a)/2*(XI(i,n/2));
    fun = x*log(x);
    out = out + 4*(sqrt(b)-a)/2*W(i,n/2)*fun;
end

syms z; 
ExactOut= double(int(4*log(z)*z,a,sqrt(b)));
