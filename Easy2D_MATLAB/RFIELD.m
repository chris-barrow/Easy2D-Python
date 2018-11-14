function RFIELD(Px,Py,FREC,fid2)


fprintf(fid2,'\n %s  \n \n', 'FIELD POINTS COORDINATES AND SOLUTIONS:');
for K=1:FREC  
   fprintf(fid2,'%s %i \t %s  %f3.3  %s  %f3.3 \n', 'FIELD POINT # ',K ,'X=', Px(K), 'Y', Py(K));
end


end
