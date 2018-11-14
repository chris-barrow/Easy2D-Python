function easy2D
clc
clear
inputfilename=input('Specify input file name. ', 's');
%inputfilename='test3.dat';
[XI, W]=SETINT();
XIPMAP= SETMAP();
[fid2,NNODE, NELEM, X, Y, NODE, KIND, TEMP, CA, CB, CC, FREC,Field, Exterior,Px,Py,VINF]=PREP(inputfilename);
[CP,DTDN,TEMP,XS,A,B,PhiP,dPhidPX,dPhidPY,QN]=PROC(fid2,XI, W, NNODE, NELEM, X, Y, NODE, KIND, TEMP, XIPMAP, CA,CB, CC, FREC,Field, Exterior,Px,Py,VINF);
fclose(fid2);
end