function XIPMAP= SETMAP()
%
%-----Linear Elements
%
XIPMAP(1,1)=-1;
XIPMAP(2,1)=1;
%
%-----Quadratic Elements
%
XIPMAP(1,2)=-1;
XIPMAP(2,2)=0;
XIPMAP(3,2)=1;
%
%-----Cubic Elements
%
XIPMAP(1,3)=-1;
XIPMAP(2,3)=-1/3;
XIPMAP(3,3)=1/3;
XIPMAP(4,3)=1;
end
