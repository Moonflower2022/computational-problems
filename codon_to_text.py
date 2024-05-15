lookup = {
'A' : 'AGG',

'B' : 'AGT',

'C' : 'ATA',

'D' : 'ATC',

'E' : 'ATG',

'F' : 'ATT',

'G' : 'CAA',

'H' : 'CAC',

'I' : 'CAG',

'J' : 'CAT',

'K' : 'CCA',

'L' : 'CCC',

'M' : 'CCG',

'N' : 'CCT',

'O' : 'CGA',

'P' : 'CGC',

'Q' : 'CGG',

'R' : 'CGT',

'S' : 'CTA',

'T' : 'CTC',

'U' : 'CTG',

'V' : 'CTT',

'W' : 'GAA',

'X' : 'GAC',

'Y' : 'GAG',

'Z' : 'GAT',

' '  : 'GCA',

':' : 'GCC',

',' : 'GCG',

"-" : 'GCT',

'.' : 'GGA',

'!' : 'GGC'
}

lookup1 = {
 'AGG':'A' ,

 'AGT':'B' ,

 'ATA':'C' ,

 'ATC':'D' ,

 'ATG':'E' ,

 'ATT':'F' ,

 'CAA':'G' ,

 'CAC':'H' ,

 'CAG':'I' ,

 'CAT':'J' ,

 'CCA':'K' ,

 'CCC':'L' ,

 'CCG':'M' ,

 'CCT':'N' ,

 'CGA':'O' ,

 'CGC':'P' ,

 'CGG':'Q' ,

 'CGT':'R' ,

 'CTA':'S' ,

 'CTC':'T' ,

 'CTG':'U' ,

 'CTT':'V' ,

 'GAA':'W' ,

 'GAC':'X' ,

 'GAG':'Y' ,

 'GAT':'Z' ,

 'GCA': ' ', 

 'GCC': ',',

 'GCG':',' ,

 'GCT':'-' ,

 'GGA':'.' ,

 'GGC':'!' 
}



def textToCodon(textstring):
  product = ""
  errorList = ""
  for letter in textstring.upper():
    if letter in lookup:
      product = product + lookup[letter]
    else:
      product = product + "%$@"
      errorList = errorList + letter + ", "
    
  
  return [product, errorList]

def textToCodonWithStuffInBetween(textstring, stuff):
  product = ""
  errorList = ""
  for letter in textstring.upper():
    if letter in lookup:
      product = product + lookup[letter]+stuff
    else:
      product = product + "%$@ "
      errorList = errorList + letter + ", "
    
  
  return [product, errorList]

def codonToText(codonString):
  product = ""
  counter = 2
  codon = ""
  errorList = ""
  for i in range(len(codonString)):
    if i < counter:
      codon = codon + codonString[i]
    elif i == counter:
      codon = codon + codonString[i]
      if codon in lookup1:
        product = product + lookup1[codon]
      else:
        product = product + "%"
        errorList = errorList + codon + ", "
      counter = counter + 3
      codon = ""
  return [product, errorList]

def codonWithStuffInBetweenToText(codonString, stuff):
  product = ""
  counter = 2
  codon = ""
  errorList = ""
  for i in range(len(codonString)):
    if codonString[i] != stuff:
      if i < counter:
        codon = codon + codonString[i]
      elif i == counter:
        codon = codon + codonString[i]
        if codon in lookup1:
          product = product + lookup1[codon]
        else:
          product = product + "%"
          errorList = errorList + codon + ", "
        counter = counter + 4
        codon = ""
    
  return [product, errorList]

def show (text, errorList):
  print("string:")
  print(text)
  if errorList != "":
    print("error list (in order):")
    print(errorList)


def userInput ():
    print("What mode? (1: text to codon, 2: text to codon with stuff [specified later], 3: codon to text, 4: codon stuff [specified later] to text) ", end = "")
    userMode = input()
    print("Text (copy paste or type)(no quotes): ")
    userString = input()
    print("Stuff in between (for 2 and 4)(enter whatever if not one of those modes): ", end = "")
    userStuff = input()
    #print("Ignore list (type a list of things to ignore)(for 3 and 4)(enter whatever if not one of those modes): ", end = "")
    #userIgnore = input()
    if userMode == "1":
        show(*textToCodon(userString))
    elif userMode == "2":
        show(*textToCodonWithStuffInBetween(userString, userStuff))
    elif userMode == "3":
        show(*codonToText(userString))
        print("Characters: " + str(len(userString)/3))
    elif userMode == "4":
        show(*codonWithStuffInBetweenToText(userString, userStuff))
        print("Characters: " + str(len(userString)/3))
    else:
        print("ERROR: INVALID USER MODE")
    userInput()

# examples 

"Jefferson. When Tante Lou told him to go to see Mr. Henri"
"CATATGATTATTATGCGTCTACGACCTGGAGCAGAACACATGCCTGCACTCAGGCCTCTCATGGCACCCCGACTGGCACTCCGACCCATCGCACACCAGCCGGCACTCCGAGCACAACGAGCACTCCGAGCACTAATGATGGCACCGCGTGGAGCACACATGCCTCGTCAG"

print("EXAMPLES:")
print("Mode 1 [text to codon]: Positively contributing to a community ---> CGCCGACTACAGCTCCAGCTTATGCCCGAGGCAATACGACCTCTCCGTCAGAGTCTGCTCCAGCCTCAAGCACTCCGAGCAAGGGCAATACGACCGCCGCTGCCTCAGCTCGAG")
print("Mode 2 [text to codon with stuff in between](- entered for stuff in between): Self awareness and responsible decision making ---> CTA-ATG-CCC-ATT-GCA-AGG-GAA-AGG-CGT-ATG-CCT-ATG-CTA-CTA-GCA-AGG-CCT-ATC-GCA-CGT-ATG-CTA-CGC-CGA-CCT-CTA-CAG-AGT-CCC-ATG-GCA-ATC-ATG-ATA-CAG-CTA-CAG-CGA-CCT-GCA-CCG-AGG-CCA-CAG-CCT-CAA-")
print("Mode 3 [codon to text]: CTACGAATACAGAGGCCCGCAAGGGAAAGGCGTATGCCTATGCTACTAGCAAGGCCTATCGCACTAATGCCCATTGCACCGAGGCCTAGGCAAATGCCGATGCCTCTC ---> SOCIAL AWARENESS AND SELF MANAGEMENT")
print("Mode 4 [codon with stuff in between to text](= entered for stuff in between): ATA=CAC=ATG=ATA=CCA=GCA=CTC=CAC=ATG=GCA=ATT=CGT=ATG=CGG=CTG=ATG=CCT=ATA=GAG=GCA=CTC=ATG=CGT=CCG= ---> CHECK THE FREQUENCY TERM")
print("-------------INPUT-------------")
userInput()
