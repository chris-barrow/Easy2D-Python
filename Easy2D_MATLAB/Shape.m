function [PSI,DPSI]=Shape(XI,KINDI)
%
%---- SHAPE FUNCTIONS FOR BOUNDARY ELEMENTS
%
%
%     Linear elements
%
if KINDI==1
    PSI(1)=0.5*(1.0-XI);
    PSI(2)=0.5*(1.0+XI);
    DPSI(1)=-0.5;
    DPSI(2)=0.5;
end
%
%     Quadratic elements
%
if KINDI==2
    PSI(1)=0.5*XI*(XI-1.0);
    PSI(2)=1.0-XI^2;
    PSI(3)=0.5*XI*(XI+1.0);
    DPSI(1)=XI-0.5;
    DPSI(2)=-2.0*XI;
    DPSI(3)=XI+0.5;
end
%
%     Cubic elements
%
if KINDI==3
    
    PSI(1)=9./16.*(1./9.-XI^2)*(XI-1.0);
    PSI(2)=27./16.*(1.0-XI^2)*(1./3.-XI);
    PSI(3)=27./16.*(1.0-XI^2)*(1./3.+XI);
    PSI(4)=-9./16.*(1./9.-XI^2)*(XI+1.0);
    DPSI(1)=-9./16.*(3.*XI^2-2.*XI-1./9.);
    DPSI(2)=27./16.*(3.*XI^2-2./3.*XI-1.);
    DPSI(3)=27./16.*(-3.*XI^2-2./3.*XI+1.);
    DPSI(4)=-9./16.*(-3.*XI^2-2.*XI+1./9.);
end
end