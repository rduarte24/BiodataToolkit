#We import from biopython library the SeqIO tool
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
import time
import xlsxwriter

#Var definitions
globalcount=0    
cdsList=[]
fullFastas={'Complete Fasta':[]}
renamedFastas={'Renamed Fastas':[]}
init = False

#We define the class to define the data estructure that we are going to use.
class DataSet:
    
    #Constructor Method    
    def __init__(self,keys):
        self.data={}
        for i in keys:
            self.data[i]=[]
        self.initialized = True

#Due the different types of sequence that we can get from the NCBI GenBank database,
#We define an specific class to get all the codon sequences corresponding to the sequence.
class Cdstype:
    
    #Contructor method
    def __init__(self,tipo,keys):
        self.type = str(tipo)
        self.data = {}
        for i in keys:
            self.data[i]=[]
        self.data['CDS']=[]
        self.data['Fasta'] = []

        
def createNewName(country,sequence,segment,counter):
    newName=">"
    countries={"Afghanistan":["A","AF"],"Aland Islands":["E","AX"],"Albania":["E","AL"],"Algeria":["F","DZ"],"American Samoa":["O","AS"],"Andorra":["E","AD"],"Angola":["F","AO"],"Anguilla":["L","AI"],"Antarctica":["S","AQ"],"Antigua and Barbuda":["L","AG"],"Argentina":["L","AR"],"Armenia":["A","AM"],"Aruba":["L","AW"],"Australia":["O","AU"],"Austria":["E","AT"],"Azerbaijan":["A","AZ"],"Bahamas":["L","BS"],"Bahrain":["A","BH"],"Bangladesh":["A","BD"],"Barbados":["L","BB"],"Belarus":["E","BY"],"Belgium":["E","BE"],"Belize":["L","BZ"],"Benin":["F","BJ"],"Bermuda":["L","BM"],"Bhutan":["A","BT"],"Bolivia":["L","BO"],"Bosnia and Herzegovina":["E","BA"],"Botswana":["F","BW"],"Bouvet Island":["E","BV"],"Brazil":["L","BR"],"British Indian Ocean Territory":["A","IO"],"Brunei Darussalam":["A","BN"],"Bulgaria":["E","BG"],"Burkina Faso":["F","BF"],"Burundi":["F","BI"],"Cambodia":["A","KH"],"Cameroon":["F","CM"],"Canada":["N","CA"],"Cape Verde":["F","CV"],"Cayman Islands":["L","KY"],"Central African Republic":["F","CF"],"Chad":["F","TD"],"Chile":["L","CL"],"China":["A","CN"],"Christmas Island":["O","CX"],"Cocos (Keeling) Islands":["A","CC"],"Colombia":["L","CO"],"Comoros":["F","KM"],"Congo":["F","CG"],"Congo":["F","CD"],"Cook Islands":["O","CK"],"Costa Rica":["L","CR"],"Cote d'Ivoire":["F","CI"],"Croatia":["E","HR"],"Cuba":["L","CU"],"Cyprus":["E","CY"],"Czech Republic":["E","CZ"],"Denmark":["E","DK"],"Djibouti":["F","DJ"],"Dominica":["L","DM"],"Dominican Republic":["L","DO"],"Ecuador":["L","EC"],"Egypt":["F","EG"],"El Salvador":["L","SV"],"Equatorial Guinea":["F","GQ"],"Eritrea":["F","ER"],"Estonia":["E","EE"],"Ethiopia":["F","ET"],"Falkland Islands (Malvinas)":["L","FK"],"Faroe Islands":["E","FO"],"Fiji":["O","FJ"],"Finland":["E","FI"],"France":["E","FR"],"French Guiana":["L","GF"],"French Polynesia":["O","PF"],"French Southern Territories":["E","TF"],"Gabon":["F","GA"],"Gambia":["F","GM"],"Georgia":["E","GE"],"Germany":["E","DE"],"Ghana":["F","GH"],"Gibraltar":["E","GI"],"Greece":["E","GR"],"Greenland":["L","GL"],"Grenada":["L","GD"],"Guadeloupe":["L","GP"],"Guam":["O","GU"],"Guatemala":["L","GT"],"Guernsey":["E","GG"],"Guinea":["F","GN"],"Guinea-Bissau":["F","GW"],"Guyana":["L","GY"],"Haiti":["L","HT"],"Heard Island and McDonald Islands":["O","HM"],"Holy See (Vatican City State)":["E","VA"],"Honduras":["L","HN"],"Hong Kong":["A","HK"],"Hungary":["E","HU"],"Iceland":["E","IS"],"India":["A","IN"],"Indonesia":["A","ID"],"Iran":["A","IR"],"Iraq":["A","IQ"],"Ireland":["E","IE"],"Isle of Man":["E","IM"],"Israel":["A","IL"],"Italy":["E","IT"],"Jamaica":["L","JM"],"Japan":["A","JP"],"Jersey":["E","JE"],"Jordan":["A","JO"],"Kazakhstan":["A","KZ"],"Kenya":["F","KE"],"Kiribati":["O","KI"],"Korea":["A","KP"],"South Korea":["A","KR"],"Kuwait":["A","KW"],"Kyrgyzstan":["A","KG"],"Lao People's Democratic Republic":["A","LA"],"Latvia":["E","LV"],"Lebanon":["A","LB"],"Lesotho":["F","LS"],"Liberia":["F","LR"],"Libyan Arab Jamahiriya":["F","LY"],"Liechtenstein":["E","LI"],"Lithuania":["E","LT"],"Luxembourg":["E","LU"],"Macao":["A","MO"],"Macedonia, the former Yugoslav Republic of":["E","MK"],"Madagascar":["F","MG"],"Malawi":["F","MW"],"Malaysia":["A","MY"],"Maldives":["A","MV"],"Mali":["F","ML"],"Malta":["E","MT"],"Marshall Islands":["O","MH"],"Martinique":["L","MQ"],"Mauritania":["F","MR"],"Mauritius":["F","MU"],"Mayotte":["F","YT"],"Mexico":["N","MX"],"Micronesia, Federated States of":["O","FM"],"Moldova, Republic of":["E","MD"],"Monaco":["E","MC"],"Mongolia":["A","MN"],"Montenegro":["E","ME"],"Montserrat":["L","MS"],"Morocco":["F","MA"],"Mozambique":["F","MZ"],"Myanmar":["A","MM"],"Namibia":["F","NA"],"Nauru":["O","NR"],"Nepal":["A","NP"],"Netherlands":["E","NL"],"Netherlands Antilles":["E","AN"],"New Caledonia":["O","NC"],"New Zealand":["O","NZ"],"Nicaragua":["L","NI"],"Niger":["F","NE"],"Nigeria":["F","NG"],"Niue":["O","NU"],"Norfolk Island":["O","NF"],"Northern Mariana Islands":["O","MP"],"Norway":["E","NO"],"Oman":["A","OM"],"Pakistan":["A","PK"],"Palau":["O","PW"],"Palestinian Territory, Occupied":["A","PS"],"Panama":["L","PA"],"Papua New Guinea":["O","PG"],"Paraguay":["L","PY"],"Peru":["L","PE"],"Philippines":["A","PH"],"Pitcairn":["O","PN"],"Poland":["E","PL"],"Portugal":["E","PT"],"Puerto Rico":["L","PR"],"Qatar":["A","QA"],"Reunion  Réunion":["F","RE"],"Romania":["E","RO"],"Russia":["A","RU"],"Rwanda":["F","RW"],"Saint Barthélemy":["L","BL"],"Saint Helena":["F","SH"],"Saint Kitts and Nevis":["L","KN"],"Saint Lucia":["L","LC"],"Saint Martin (French part)":["L","MF"],"Saint Pierre and Miquelon":["L","PM"],"Saint Vincent and the Grenadines":["L","VC"],"Samoa":["O","WS"],"San Marino":["E","SM"],"Sao Tome and Principe":["F","ST"],"Saudi Arabia":["A","SA"],"Senegal":["F","SN"],"Serbia":["E","RS"],"Seychelles":["F","SC"],"Sierra Leone":["F","SL"],"Singapore":["A","SG"],"Slovakia":["E","SK"],"Slovenia":["E","SI"],"Solomon Islands":["O","SB"],"Somalia":["F","SO"],"South Africa":["F","ZA"],"South Georgia and the South Sandwich Islands":["E","GS"],"Spain":["E","ES"],"Sri Lanka":["A","LK"],"Sudan":["F","SD"],"Suriname":["L","SR"],"Svalbard and Jan Mayen":["E","SJ"],"Swaziland":["F","SZ"],"Sweden":["E","SE"],"Switzerland":["E","CH"],"Syrian Arab Republic":["A","SY"],"Taiwan":["A","TW"],"Tajikistan":["A","TJ"],"Tanzania":["F","TZ"],"Thailand":["A","TH"],"Timor-Leste":["A","TL"],"Togo":["F","TG"],"Tokelau":["O","TK"],"Tonga":["O","TO"],"Trinidad and Tobago":["L","TT"],"Tunisia":["F","TN"],"Turkey":["A","TR"],"Turkmenistan":["A","TM"],"Turks and Caicos Islands":["L","TC"],"Tuvalu":["O","TV"],"Uganda":["F","UG"],"Ukraine":["E","UA"],"United Arab Emirates":["A","AE"],"United Kingdom":["E","GB"],"United States":["N","US"],"United States Minor Outlying Islands":["L","UM"],"Uruguay":["L","UY"],"USA":["N","US"],"Uzbekistan":["A","UZ"],"Vanuatu":["O","VU"],"Venezuela":["L","VE"],"Viet Nam":["A","VN"],"Virgin Islands, British":["L","VG"],"Virgin Islands, U.S.":["L","VI"],"Wallis and Futuna":["O","WF"],"Western Sahara":["F","EH"],"Yemen":["A","YE"],"Zambia":["F","ZM"],"Zimbabwe":["F","ZW"]}
    states={"Alabama":"AL","Alaska":"AK","Arizona":"AZ","Arkansas":"AR","California":"CA","Colorado":"CO","Connecticut":"CT","Delaware":"DE","District of Columbia":"DC","Florida":"FL","Georgia":"GA","Hawaii":"HI","Idaho":"ID","Illinois":"IL","Indiana":"IN","Iowa":"IA","Kansas":"KS","Kentucky":"KY","Louisiana":"LA","Maine":"ME","Maryland":"MD","Massachusetts":"MA","Michigan":"MI","Minnesota":"MN","Mississippi":"MS","Missouri":"MO","Montana":"MT","Nebraska":"NE","Nevada":"NV","New Hampshire":"NH","New Jersey":"NJ","New Mexico":"NM","New York":"NY","North Carolina":"NC","North Dakota":"ND","Ohio":"OH","Oklahoma":"OK","Oregon":"OR","Pennsylvania":"PA","RhodeIsland":"RI","South Carolina":"SC","South Dakota":"SD","Tennessee":"TN","Texas":"TX","Utah":"UT","Vermont":"VT","Virginia":"VA","Washington":"WA","West Virginia":"WV","Wisconsin":"WI","Wyoming":"WY"}
    
    if ':'in country:
        country=country[0:country.index(':')]
    if country in countries.keys():
        newName=newName+str(segment)+countries[country][0] + countries[country][1]
        if country == "United States"or "USA":
            for i in states.keys():
                if i in sequence:
                    newName=newName + states[i] 
    else:
        for y in countries.keys():
            if y in sequence:
                newName=newName+str(segment)+countries[y][0] + countries[y][1]
                break
            else:
                newName=newName+str(segment)+'XX'
                break
    newName=newName+str(counter)+'\n'
    return newName


def parser(filename,outFile):
    start = time.time()
    init = False
    globalcount = 0
    #We read the sequence genbank file
    for seq_record in SeqIO.parse(filename, "genbank"):
        
        fullFastas['Complete Fasta'].append(seq_record.format('fasta'))
        
        #first we are going to initialize our data structures
        if init != True:
            #We pull out the keys that we're going to use for the data structure
            for feature in seq_record.features:
                #Verify the type of feature
                if feature.type == 'source':
                    #Create the main Dataset usign the DataSet class
                    dataSet=DataSet(feature.qualifiers.keys())
                #Verify the type of the feature for Codon Sequences
                if feature.type == "CDS":
                    try:
                        cds=Cdstype(feature.qualifiers['gene'][0],feature.qualifiers.keys())
                        cdsList.append(cds)
                    except:
                        cds=Cdstype(feature.qualifiers['product'][0],feature.qualifiers.keys())
                        cdsList.append(cds)
            #Initialization Validation
            init = True
        #Collect all the features selected in the first file as the set of interest
        for feature in seq_record.features:
            #First we go for the Codon Sequence feature in the file.
            if feature.type == "CDS":
                for item in cdsList:
                    try:
                        if item.type == feature.qualifiers['gene'][0]:
                            for y in feature.qualifiers.keys():
                                if y in item.data.keys():
                                    item.data[y].append(feature.qualifiers[y][0])
                            #We save the location of the codon Sequence        
                            item.data['CDS'].append(str(feature.location))
                            #We pull out the sequence as string to join the string with the new
                            myseq2 = str(feature.location.extract(seq_record.seq))
                            #We pull out the sequence in fasta format to keep the original name
                            myseq=feature.location.extract(seq_record).format('fasta')
                            #We save the original fasta format sequence
                            item.data['Fasta'].append(myseq)
                            #We trimm the sequence for the creation of the new name
                            myseq=myseq[0:myseq.index('\n')]
                    except:
                        try:
                            item.data['CDS'].append('empty')
                            item.data['Fasta'].append('empty')
                        except:
                            print('Fatal Error')
                            continue
            if feature.type =='source':
                            for y in dataSet.data.keys():
                                if y in feature.qualifiers.keys():
                                    dataSet.data[y].append(feature.qualifiers[y][0])
                                else:
                                    dataSet.data[y].append('empty')
        #We pull the country for the rename process if the sequence has the country feature
        if 'country' in dataSet.data.keys():
            tempCountry=dataSet.data['country'][-1]
            if ':' in tempCountry:
                tempCountry=tempCountry[0:tempCountry.index(':')]
        else:
            tempCountry = 'NA'
        #We pull the segment for the rename process if the sequence has the segment feature
        if 'segment' in dataSet.data.keys():
            tempSegment=dataSet.data['segment'][-1]
        else:
            tempSegment = 'NA'
        #We rename the sequence according to GCL nomenclature
        nombre = createNewName(tempCountry,myseq,tempSegment,globalcount)
        #nombre = nombre +'\n' se implementa en la función new name
        #print ('new name :',nombre)
        fasta_format_string = nombre + myseq2
        renamedFastas['Renamed Fastas'].append(fasta_format_string)
        globalcount = globalcount+1


    end = time.time()
    for i in dataSet.data.keys():
        print(i,' = ',len(dataSet.data[i]))

    #Now we pack everything in a new excel table

    workbook = xlsxwriter.Workbook(outFile)
    # workbook = xlsxwriter.Workbook('Segment_4_2017_all_renamed_final.xlsx') ORIGINAL
    worksheet = workbook.add_worksheet()
    #Input dicts
    inputList=[dataSet.data]
    for i in cdsList:
        inputList.append(i.data)
    inputList.append(fullFastas)
    inputList.append(renamedFastas)
    #print (inputList)

    row = 0
    col = 0

    for dicc in inputList:
        print (dicc.keys())
        for head in dicc.keys():
            worksheet.write(row,col,head)
            worksheet.write_column(row+1,col,dicc[head])
            col += 1

    workbook.close()
    print ("Runtime: "+str(int(end-start)))                            

#parser("/Users/rduarte/Documents/Projects/GCL/Biodata Toolkit/S4-1999.gb","1999.xlsx")
                            


    
