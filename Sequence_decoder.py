import xlsxwriter

#Main Function
def sequenceDecoder(seq):
    code={'B':['C','G','T'],'D':['A','G','T'],'H':['A','C','T'],'K':['G','T'],'M':['A','C'],'N':['A','C','T','G'],'R':['A','G'],'S':['C','G'],'V':['A','C','G'],'W':['A','T'],'Y':['C','T']}
    normal=['A','C','T','G']
    alternative=['B','D','H','K','M','N','R','S','V','W','Y']
    outsequences=['']
    tempsequences=[]
    for z in seq:
        #We verify nucleotide
        if z in normal:
            for i in range(0,len(outsequences)):
                outsequences[i]=outsequences[i]+z
        elif z in alternative:
            for i in outsequences:
                for y in code[z]:
                    tempsequences.append(i+y)
            outsequences=tempsequences.copy()
            tempsequences=[]
    #print (outsequences)
    # outFileName=outFileName+'.xlsx'
    # workbook = xlsxwriter.Workbook(outFileName)
    # workbook = xlsxwriter.Workbook('Segment_4_2017_all_renamed_final.xlsx') ORIGINAL
    # worksheet = workbook.add_worksheet()
    # row = 0
    # col = 0

    #for i in outsequences:
    # worksheet.write(row,col,seq)
    # worksheet.write_column(row+1,col,outsequences)
    # workbook.close()
    print(len(outsequences)) 

#Old call
#sequenceDecoder('YYRCMRCCKCAAATKCAGACACATTRTG','primer1')           

#Sequence Decoder counter returns the amount of possible sequences from an input consensus

def sequenceDecoderCount(seq):
    code={'B':['C','G','T'],'D':['A','G','T'],'H':['A','C','T'],'K':['G','T'],'M':['A','C'],'N':['A','C','T','G'],'R':['A','G'],'S':['C','G'],'V':['A','C','G'],'W':['A','T'],'Y':['C','T']}
    prob=1
    for z in seq:
        if z in code.keys():
            prob=prob*len(code[z])
    print (prob)

#New Call
sequenceDecoderCount('BYAMRRCCRCMRATGCAGACAYRBTATG')  


    


