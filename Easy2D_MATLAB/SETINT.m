function [XI,W]=SETINT()
%
%-----1-D STANDARD GAUSSIAN QUADRATURE
%
%     2 POINTS
%
XI(1,1)=-1/sqrt(3);
XI(2,1)=-XI(1,1);
W(1,1)=1.0;
W(2,1)=W(1,1);
%
%     4 POINTS
%
XI(1,2)=-0.86113631159405257522;
XI(2,2)=-0.33998104358485626480;
XI(3,2)=-XI(2,2);
XI(4,2)=-XI(1,2);
W(1,2)=0.34785484513745385737;
W(2,2)=0.65214515486254614263;
W(3,2)=W(2,2);
W(4,2)=W(1,2);
%
%     6 POINTS
%
XI(1,3)=-0.93246951420315202781;
XI(2,3)=-0.66120938646626451366;
XI(3,3)=-0.23861918608319690863;
XI(4,3)=-XI(3,3);
XI(5,3)=-XI(2,3);
XI(6,3)=-XI(1,3);
W(1,3)=0.17132449237917034504;
W(2,3)=0.36076157304813860757;
W(3,3)=0.46791393457269104739;
W(4,3)=W(3,3);
W(5,3)=W(2,3);
W(6,3)=W(1,3);
%
%     8 POINTS
%
XI(1,4)=-0.96028985649753623168;
XI(2,4)=-0.79666647741362673959;
XI(3,4)=-0.52553240991632898582;
XI(4,4)=-0.18343464249564980494;
XI(5,4)=-XI(4,4);
XI(6,4)=-XI(3,4);
XI(7,4)=-XI(2,4);
XI(8,4)=-XI(1,4);
W(1,4)=0.10122853629037625915;
W(2,4)=0.22238103445337447054;
W(3,4)=0.31370664587788728734;
W(4,4)=0.36268378337836198297;
W(5,4)=W(4,4);
W(6,4)=W(3,4);
W(7,4)=W(2,4);
W(8,4)=W(1,4);
%
%     10 POINTS
%
XI(1,5)=-0.97390652851717172008;
XI(2,5)=-0.86506336668898451073;
XI(3,5)=-0.67940956829902440623;
XI(4,5)=-0.43339539412924719080;
XI(5,5)=-0.14887433898163121088;
XI(6,5)=-XI(5,5);
XI(7,5)=-XI(4,5);
XI(8,5)=-XI(3,5);
XI(9,5)=-XI(2,5);
XI(10,5)=-XI(1,5);
W(1,5)=0.066671344308688137594;
W(2,5)=0.14945134915058059315;
W(3,5)=0.21908636251598204400;
W(4,5)=0.26926671930999635509;
W(5,5)=0.29552422471475287017;
W(6,5)=W(5,5);
W(7,5)=W(4,5);
W(8,5)=W(3,5);
W(9,5)=W(2,5);
W(10,5)=W(1,5);
%
%     12 POINTS
%
XI(1,6)=-0.981560634246719;
XI(2,6)=-0.904117256370475;
XI(3,6)=-0.769902674194305;
XI(4,6)=-0.587317954286617;
XI(5,6)=-0.367831498998180;
XI(6,6)=-0.125233408511469;
XI(7,6)=-XI(6,6);
XI(8,6)=-XI(5,6);
XI(9,6)=-XI(4,6);
XI(10,6)=-XI(3,6);
XI(11,6)=-XI(2,6);
XI(12,6)=-XI(1,6);
W(1,6)=0.047175336386512;
W(2,6)=0.106939325995318;
W(3,6)=0.160078328543346;
W(4,6)=0.203167426723066;
W(5,6)=0.233492536538355;
W(6,6)=0.249147045813403;
W(7,6)=W(6,6);
W(8,6)=W(5,6);
W(9,6)=W(4,6);
W(10,6)=W(3,6);
W(11,6)=W(2,6);
W(12,6)=W(1,6);
end