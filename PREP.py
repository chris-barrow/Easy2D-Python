def PREP(inputfilename):
    """
    PREPROCESSOR
    """

    # inputfilename='TestCase2_2.dat';
    InputText = ""
    with open(inputfilename, 'r') as inputFile:
        InputText = inputFile.read().splitlines()
    outputFile = open('output.dat','w')
#    BLOCK = InputText{1}
#    NNN = str2num(BLOCK{3}) # Grabs number of nodes and records from input file
    NNN = list(map(int, inputText[2].split(','))) # Grabs number of nodes and records from input file
    NNODE = NNN[1] # Gets number of nodes
    NREC = NNN[2] # Gets number of records
#    EEE = str2num(BLOCK{5+NREC}) # Gets number of elements and records
    EEE = list(map(int, inputText[5+NREC].split(','))) # Gets number of elements and records
    NELEM = EEE[1] # Number of elements
    EREC = EEE[2] # Number of element records
#    BREC = str2num(BLOCK{7+NREC+EREC}) # Gets number of records for BCs
    BREC = list(map(int, inputText[7+NREC+EREC].split(','))) # Gets number of records for BCs
    Field = 0
    Exterior = 0
    FREC = 0
    if strcmp(BLOCK{2},'NODES')  == 0
        disp('Error on NODES Command')
        return

    if strcmp(BLOCK{4+NREC},'ELEMENTS') == 0
        disp('Error on ELEMENTS Command')
        return

    if strcmp(BLOCK{6+NREC+EREC},'BOUNDARY CONDITIONS')==0
        disp('Error on BOUNDARY CONDITIONS Command')
        return

    if strcmp(BLOCK{8+NREC+EREC+BREC},'SOLVE') == 0
        if strcmp(BLOCK{8+NREC+EREC+BREC},'FIELD') == 1
            FREC = str2num(BLOCK{9+NREC+EREC+BREC})
            Field = 2
            Exterior = 0
            if (strcmp(BLOCK{10+NREC+EREC+BREC+FREC},'EXTERIOR')==1)
                if(strcmp(BLOCK{11+NREC+EREC+BREC+FREC},'VINF')==1)
                    VINF =  str2num(BLOCK{12+NREC+EREC+BREC+FREC})

                Exterior = 3

        else
            if (strcmp(BLOCK{8+NREC+EREC+BREC},'EXTERIOR')==1)
                if (strcmp(BLOCK{9+NREC+EREC+BREC},'VINF')==1)
                    VINF=str2num(BLOCK{10+NREC+EREC+BREC})

                Field=0
                Exterior=3

    if Exterior==0
        VINF=0

    if strcmp(BLOCK{8+NREC+EREC+BREC+FREC+Field+Exterior},'SOLVE')==0
        disp('Couldnt Catch SOLVE Command, Solution Terminated')
        return

    fprintf(outputFile,'%s \n \n', BLOCK{1})
    nodes=zeros(NNN(2),6)
    for i=4:NREC+3
        nodes(i-3,:)= str2num(BLOCK{i})

    N1=nodes(:,1)
    N2=nodes(:,2)
    X1=nodes(:,3)
    Y1=nodes(:,4)
    X2=nodes(:,5)
    Y2=nodes(:,6)
    [X,Y]=Rnode(outputFile,NNODE,NREC,N1,N2,X1,Y1,X2,Y2)
    elements=zeros(EREC,4)
    for j=6+NREC:6+NREC+EREC-1
        elements(j-5-NREC,:)=str2num(BLOCK{j})

    NODEI=elements(:,1)
    NODEL=elements(:,2)
    NUMBER=elements(:,3)
    KINDI=elements(:,4)
    [NODE, KIND]=Relem(outputFile,NNODE,NELEM,EREC,NODEI,NODEL,NUMBER,KINDI)
    bcs=zeros(BREC,6)
    for k=8+NREC+EREC:8+NREC+EREC+BREC-1
        bcs(k-7-NREC-EREC,:)=str2num(BLOCK{k})

    K1=bcs(:,1)
    K2=bcs(:,2)
    NOD=bcs(:,3)
    CA1=bcs(:,4)
    CB1=bcs(:,5)
    CC1=bcs(:,6)
    [TEMP,CA,CB,CC]= BC(outputFile, NNODE, NELEM, NODE, KIND, BREC,K1,K2,NOD,CA1,CB1,CC1)
    if Field==2
        FIELDS=zeros(FREC,2)
        for l=10+NREC+EREC+BREC:10+NREC+EREC+BREC+FREC-1
            FIELDS(l-9-NREC-EREC-BREC,:)=str2num(BLOCK{l})

        Px=FIELDS(:,1)
        Py=FIELDS(:,2)

    return [outputFile,NNODE, NELEM, X, Y, NODE, KIND, TEMP, CA, CB, CC,FREC,Field, Exterior,Px,Py,VINF]
