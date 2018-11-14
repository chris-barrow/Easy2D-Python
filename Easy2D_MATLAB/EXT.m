function PhiI=EXT(fid2,NNODE,X,VINF)
PhiI=zeros(1,NNODE); 
for i=1:NNODE
     PhiI(i)=VINF*X(i);
end
 
fprintf(fid2,'\n %s  \n \n', '==============EXTERIOR PROBLEM:=====================');

fprintf(fid2,'%s %3.3f \n', 'V infiniti=',VINF);


end
