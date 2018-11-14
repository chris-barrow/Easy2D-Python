function [CP,DTDN,TEMP,XS,A,B,PhiP,dPhidPX,dPhidPY,QN]=PROC(fid2,XI, W, NNODE, NELEM, X, Y, NODE, KIND, TEMP, XIPMAP, CA, CB, CC,FREC,Field,Exterior,Px,Py,VINF)
%
%---- PROCESSOR
%
if Exterior==3
    PhiI=EXT(fid2,NNODE,X,VINF);
else
    PhiI=zeros(1,NNODE);
end
    
[CP,A,B,QN]=Form(NNODE, NELEM, NODE, KIND, X, Y, TEMP,XI,W, XIPMAP, CA, CB, CC,Exterior,PhiI);
[XS,A,B]=Solve(A,B);
[DTDN,TEMP]=Solout(fid2,NNODE, NELEM, KIND, NODE,CP, TEMP, CA, CB, CC, XS,Exterior);
if Field==2
    [PhiP,dPhidPX,dPhidPY,QN]=FIELD(fid2,Px,Py,FREC,NNODE,NELEM,KIND,NODE,X,Y,TEMP,DTDN,XI,W,Exterior,VINF,PhiI);
else
    [PhiP,dPhidPX,dPhidPY]=zeros(1,3);
end

    
end