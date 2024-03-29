'''
Definite Workable test cases: 
CUO+H2SO4->CUSO4+H2O
AGNO3+NACL->AGCL+NANO3
(NA)2CO3 + 2HCL --> 2NACL + H2O + CO2
CACO3 + 2HCL --> CA(CL)2 + H2O + CO2
3HCL + AL(OH)3 --> AL(CL)3 + 3H2O
CUO + 2HCL --> CU(CL)2 + H2O
MG+H2SO4-->MGSO4+H2
CA+HCL --> CA(CL)2+H2




'''
import math
print("Dear user, please use () for reactants with numbers affecting 2 letters. For example CACL2 as CA(CL)2")
a = str(input("1st reactant: ")).upper()
d = str(input("2nd reactant: ")).upper()
c = str(input("wanted salt: ")).upper()
m = input("mass of wanted salt: ")
if a.find("H2SO4")!= -1 or a.find("H2CO3")!= -1 or a.find("HNO3")!= -1 or a.find("HCL") != -1:
  pass
elif d.find("H2SO4")!= -1 or d.find("H2CO3")!= -1 or d.find("HNO3")!= -1 or d.find("HCL")!= -1:
  a,d = d, a
else:
  p = a
  q = d
x = a
y = d
b = c

H = 1
LI = 7
BE = 9
O = 16
NA = 23
MG = 24
AL = 27
S = 32
CL = 35.5
HCL = 36.5
K = 39
CA = 40
FE = 55
H2CO3 = 62
CU = 64
ZN = 65
GA = 70
H2SO3 = 82
PO = 84
RB = 85
SR = 88
SO4 = 96
H2SO4 = 98
SN = 119
SB = 122
CS = 133
BA = 137
IN = 155
TL = 204
PB = 207
BI = 209




#let index value be the relative atomic number 
RMA = [0,'H',2,3,4,5,6,'LI',8,'BE',10,11,12,13,14,15,'O',17,18,19,20,21,22,'NA','MG',25,26,'AL',28,29,30,31,'S',33,34,'CL','HCL',37,38,'K','CA',41,42,43,44,45,46,47,48,49,50,51,52,53,54,'FE',56,57,58,59,60,61,'H2CO3',63,'CU','ZN',66,67,68,69,'GA',71,72,73,74,75,76,77,78,79,80,81,'H2SO3',83,'PO','RB',86,87,'SR',89,90,91,92,93,94,95,'SO4',97,'H2SO4',99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,'SN',120,121,'SB',123,124,125,126,127,128,129,130,131,132,'CS',134,135,136,'BA',138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,'IN',156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,178,179,180,181,182,183,184,185,186,187,188,189,190,191,192,193,194,195,196,197,198,199,200,201,202,203,'TL',205,206,'PB',208,'BI']

bmolarmass = 0
xmolarmass = 0
Noofmoles = 0
newReplaced = 0
def Acid(x):
#byproduct salt is wanted salt
 def ByProductSalt(b):
    if len(b)>2:
      pass
      #print('{}'.format(list(b)))
    else:
      return "Invalid input"
      
    def MassofByProductSalt(m):
    
      
      def Second(y):

        #(('{}'.format(list(y)))
        #It doesn't works for CACO3+H2SO4-> CASO4+H2O+CO2
        if len(y)>3 and y.find('CO3')!=-1:
          
          #double check on H2S03
          if x.find('H2SO4')!=-1 or x.find('H2CO3')!=-1 or x.find('H2SO3')!=-1:
            
            if (x+y+"H").count('H')==(b+"HHO"+"CO2").count('H'):
              #mole ratio 1:1
              if len(b)==5:
                #identifying RAM of b
                bmolarmass = (RMA.index(str(b[:2])))+(RMA.index(str(b[2:5])))
                #no.of.moles
                Noofmoles = float(m)/bmolarmass
                if (x.count('H'))==1 and x.find('H2SO4') or x.find('H2CO3') or x.find('H2SO3')!=-1 and len(x)==5:
                  xmolarmass = (RMA.index(str(x[:5])))
                  return "\n" + str(y+' + '+x+" --> "+b+" + "+'H2O'+" + "+"CO2") + "\nNo.of.Moles of ByProductSalt = " + str(float(m)/bmolarmass) + "\nAmount of "+x+" minimumly needed is" + str(math.ceil(float(xmolarmass*Noofmoles))) + " grams"
                else:
                  return "\nSorry I havent taken that case into account yet"
          
              

          elif x.find('HCL')!=-1 or x.find('HNO2')!=-1 or x.find('HNO3')!=-1 or x.find('CH3COOH')!=-1 and (x+y).count('H')==(b+"HHO"+"CO2").count('H'):
            
          
          #works for (NA)2CO3 + 2HCL --> NACL + H2O + CO2

            if (x+y).count('H')<(b+'HHO'+"CO2").count('H'):
              if (x*2+y).count('H')==(b+'HHO'+'CO2').count('H'):              
                #works for CACO3 + 2HCL --> CA(CL)2 + H2O +CO2
                if len(b)>=4 and b.find('(')!=-1:
                  bmolarmass = RMA.index(str(b[:2]))+RMA.index(str(b[3:5]))*2
                  Noofmoles = float(m)/bmolarmass
                  xmolarmass = RMA.index(str(x[:5]))
                  return "\n"+ str(y+" + "+"2"+x+" --> "+b+" + "+"H2O"+" + "+"CO2") + "\nNo.of.Moles of ByProductSalt = " + str(float(m)/bmolarmass) + "\nAmount of "+x+" minimumly needed is " + str(math.ceil(float(xmolarmass*Noofmoles))) + " grams"
                  #used math ceil to make sure that there is enough reactant for reaction to take place
                 
            
                elif len(b)>=4:
                  bmolarmass = RMA.index(str(b[:2]))+RMA.index(str(b[2:5]))
                  Noofmoles = float(m)/bmolarmass
                  xmolarmass = RMA.index(str(x[:5]))
                  return "\n"+ str(y+" + "+"2"+x+" --> " + "2"+b+" + "+"H2O"+" + "+"CO2") + "\nNo.of.Moles of ByProductSalt = " + str(float(m)/bmolarmass) + "\nAmount of "+x+" minimumly needed is "+str(math.ceil(float(xmolarmass*Noofmoles)))+ " grams"
                else:
                  return "\nSorry I havent taken that case into account yet"

        #use index function
        #check if its a base, eg CUO, NAOH
        #works for CUO+H2SO4, when all mole ratio is 1:1, and NAOH+HCL
        elif len(y) >= 3 and y.find('O') == 2 and len((sorted(list(b+'HHO') )))==len(sorted(list(x+y))):
            #print(sorted(list(b+'HHO') )) 
            
            bmolarmass = RMA.index(str(b[:2]))+RMA.index(str(b[2:5]))
            Noofmoles =  float(m)/bmolarmass
            xmolarmass = RMA.index(str(x[:5]))
            
            if (x.count('H'))==1 and x.find('H2SO4' or 'H2CO3' or ' H2SO3' or 'H2SO4')!=-1 and len(x)==5:
              
              return "\n" + str(y+' + '+x+ " --> "+b+' + '+'H2O') + "\nNo.of.Moles of ByProductSalt = " + str(float(m)/bmolarmass) + "\nAmount of "+x+" minimumly needed is " + str(math.ceil(float(xmolarmass*Noofmoles))) + "grams"
            
        
        elif len(y)>=4 and y.find('O') == 3:
          if len(x+y)==len(b+"H2O") and (x.count('H')+y.count('H'))==(b.count('H')+('H2O').count('H')):
            
            bmolarmass = RMA.index(str(b[:2]))+RMA.index(str(b[2:5]))
            xmolarmass = RMA.index(x[:5])
            
            return "\n"+ str(y+' + '+x+' + '+'-->'+b+" + "+"H2O") + "No.of.Moles of ByProductSalt = " + str(float(m)/bmolarmass) + "\nAmount of "+x+" minimumly needed is " +str(math.ceil(float(xmolarmass*Noofmoles))) + "grams"            

          elif len(x+y)==len(b+"H2O") and (x.count('H')+y.count('H'))>(b.count('H')+('H2O').count('H')):
            
            #works for HCL+AL(OH)3-->AL(CL)3+(H2O)
            if (x.count('H')*3+y.count('H'))>(b.count('H')+('H2O'*3).count('H')) and  b.find('(') and b.find('3'):
              
              bmolarmass = RMA.index(str(b[:2]))+RMA.index(str(b[3:5]))*3
              Noofmoles = float(m)/bmolarmass
              xmolarmass = RMA.index(x[:5])
              
              return"\n" + str("3"+x+" + "+y+" --> "+b+ " + "+"3"+"H2O") + "\nNo.of.Moles of ByProductSalt = " + str(float(m)/bmolarmass) + "\nAmount of "+x+" minimumly needed is " +str(math.ceil(float(xmolarmass*Noofmoles))) + 'grams'
        
          
          #not sure if need to do one if count H on leftside< number of H on right side, cant think of such an exception

        #works for CuO+HCL, when all mole ratio is 1:2 -> 1:1, and when b = CU(Cl)2
        #((x+y)).find('H')<((b+'HHO').find('H') )
        elif len(y) >= 3 and y.find('O') == 2 and len(x+y)<len(b+"H2O"):
         
          #if len(sorted(list((x*2+(y))))) > len(sorted(list(b+'H2O'))):
          # to detect if ( ) is present    
          if b.find('(')!=-1 and len(x*2+y) == (len((b+'H2O'))-1):
            
            
            if b.find('(')!=-1:
              bmolarmass = RMA.index(str(b[:2]))+RMA.index(str(b[3:5]))*2
              Noofmoles = float(m)/bmolarmass
              xmolarmass = RMA.index(x[:5])
              
              return "\n" + str(y+" + "+"2"+(x) + " --> " +  b +" + "+"H2O") + "\nNo.of.Moles of ByProductSalt = " + str(float(m)/bmolarmass) + "\nAmount of "+x+" minimumly needed is " +str(math.ceil(float(xmolarmass*Noofmoles))) + 'grams' 
            else:
              return "\nSorry I haven't accounted for that case yet"
                    
          elif b.find('(')!=-1 and len(x+y)<len(b+"H2O"):
            
            bmolarmass = RMA.index(str(b[:2]))+RMA.index(str(b[3:5]))
            Noofmoles = float(m)/bmolarmass
            xmolarmass = RMA.index(x[:5])
            
            return "\n" + str('2'+y+" + "+x+' --> '+b+ " + "+"2"+"H2O") + "\nNo.of.Moles of ByProductSalt = " + str(float(m)/bmolarmass) + "\nAmount of "+x+" minimumly needed is " +str(math.ceil(float(xmolarmass*Noofmoles))) + 'grams' 



            #right side
            #if u want to double check use this --> print(Counter(sorted(list((x*2+(y)))))) to make sure number of types of alphabets on both sides are equal
            

          #check if its a metal
          #works for MG+H2SO4-->MGSO4+H2
        elif len(y)<=2 and 'B,SI,AS,TE,AT,C,P,SE,I,RN,N,S,BR,XE,O,Cl,KR,F,AR,NE,HE,H,CU,AG,AU'.find(y) == -1 and len((sorted(list(b+'HH') )))==len(sorted(list(x+y))):
         
          
          #return(sorted(list(b+"HH")))
          
          bmolarmass = RMA.index(b[:2])+RMA.index(b[2:5])
          Noofmoles = float(m)/bmolarmass
          xmolarmass = RMA.index(x[:5])
          
          return "\n" + str(y+" + "+ x + " --> " + b + " + " + "H2") + "\nNo.of.Moles of ByProductSalt = " + str(float(m)/bmolarmass) + "\nAmount of "+x+" minimumly needed is " + str(math.ceil(float(xmolarmass*Noofmoles))) + 'grams' 


        
        #works for CA+HCL --> CA(CL)2+H2
        elif len(y)<=2 and 'B,SI,AS,TE,AT,C,P,SE,I,RN,N,S,BR,XE,O,Cl,KR,F,AR,NE,HE,H,CU,AG,AU'.find(y) == -1 and len(sorted(list(x+y)))<len((sorted(list(b+'HH') ))) :
          
          # ( also counts as index
          if b.find('(')!=-1 and b.index('2')==6:

            bmolarmass = RMA.index(b[:2])+RMA.index(b[3:5])*2
            Noofmoles = float(m)/bmolarmass
            xmolarmass = RMA.index(x[:5])
            
            return "\n" +str(y+" + "+ "2" + x+" --> "+b+" + "+"H2") + "\nNo.of.Moles of ByProductSalt = " + str(float(m)/bmolarmass) + "\nAmount of "+x+" minimumly needed is " + str(math.ceil(float(xmolarmass*Noofmoles))) + 'grams'    
          else:
            return"\nSorry I haven't accounted for that case yet"
        else:
          return "\nInvalid input"

 


        

        
          
      return Second(y)
    return MassofByProductSalt(m)  
 return ByProductSalt(b)


  


def pq():
  if c.find("CL") != -1:
    if a.find("CL") != -1:
      p = a
      q = d
    else:
      q = a
      p = d
  if c.find("SO4") != -1:
    if a.find("SO4") != -1:
      p = a
      q = d
    else:
      q = a
      p = d
  if c.find("NO3") != -1:
    if a.find("NO3") != -1:
      p = a
      q = d
    else:
      q = a
      p = d
  if c.find("CO3") != -1:
    if a.find("CO3") != -1:
      p = a
      q = d
    else:
      q = a
      p = d
  count = 0
  P = p
  Q = q
  

  z = p+q
  RMA = [0,'H',2,3,4,5,6,'LI',8,'BE',10,11,12,13,14,15,'O',17,18,19,20,21,22,'NA','MG',25,26,'AL',28,29,30,31,'S',33,34,'CL','HCL',37,38,'K','CA',41,42,43,44,45,46,47,48,49,50,51,52,53,54,'FE',56,57,58,59,'CO3',61,'NO3',63,'CU','ZN',66,67,68,69,'GA',71,72,73,74,75,76,77,78,79,80,81,'H2SO3',83,'PO','RB',86,87,'SR',89,90,91,92,93,94,95,'SO4',97,'H2SO4',99,100,101,102,103,104,105,106,"AG",108,109,110,111,112,113,114,115,116,117,118,'SN',120,121,'SB',123,124,125,126,127,128,129,130,131,132,'CS',134,135,136,'BA',138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,'IN',156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,178,179,180,181,182,183,184,185,186,187,188,189,190,191,192,193,194,195,196,197,198,199,200,201,202,203,'TL',205,206,'PB',208,'BI']

  #To exculde the part that I haven't encountered, which is usually the exceptions
  if c.find("(") == -1 and p.find("(") ==-1 and q.find("(") == -1:
    pass
  else:
    return "\nSorry, I haven't accounted for that case. "
  
  #to check if it is a sulfate,chloride or carbonate
  if c.find('SO4') != -1:
      if c.find(")") != -1:
          Z = z.replace("(SO4)3","")
          C = c.replace("(SO4)3","")
          F = Z.replace(C,"")
          
      else:
          Z = z.replace("SO4","")
          C = c.replace("SO4","")
          F = Z.replace(C,"") 

  elif c.find('CL')  != -1:
      if c.find("(") == -1:
          Z = z.replace("CL","")
          C = c.replace("CL","")
          F = Z.replace(C,"")

      else:
          pass
      

  elif c.find('CO3') != -1:
      if c.find("(") != -1:
          Z = z.replace("(CO3)3","")
          C = c.replace("(CO3)3","")
          F = Z.replace(C,"")
          
      else:
          Z = z.replace("CO3","")
          C = c.replace("CO3","")
          F = Z.replace(C,"")     
            





  
  cmolarmass = (RMA.index(str(c[:2])))+(RMA.index(str(c[2:5])))
  Noofmoles = float(m)/cmolarmass
  pmolarmass = (RMA.index(str(p[:2])))
  qmolarmass = (RMA.index(str(q[:2])))
  pneed = str(math.ceil(pmolarmass*Noofmoles))
  qneed = str(math.ceil(qmolarmass*Noofmoles))
  
  
  
  return "\n" + P + " + " + Q + " ---> " + c + " + " + F + "\n" + "Number of moles: " + str(Noofmoles) + "\nAmount of " + p +" need: " + pneed + "grams" + "\nAmount of " + q + " need: " + qneed + "grams"




 

def titration():
  return "\n\nSTEP 1.Use a pipette to place 25.0cm^3 of reactant one into conical flask. Add three drops of methyl orange as indicator. \n\nSTEP 2.Set up a burette filled with second reactant。 Record the initial reading of burette in your table of results.\n\nSTEP 3.Tirate the second reactant solution in the conical falsk against the first reactant solution.\n\nSTEP 4.Continue adding the second reactant from the burette until there is a colour change to orange. Record the final burette reading.\n\nSTEP 5 Repeat the experiment using a clean conical flaskbut without adding indicator. Add the same volume of second reactant to neutralise the first reactant.\n\nSTEP 6.Obtain the dry salt using evaperation or crystallisation.\n" + Acid(x)

def Excess_insoluble_reactant():
  return "\n\nSTEP 1.Mix the excess insoluble reactant with acid to ensure that all the acid is reacted.\n\nSTEP 2.The mixture is then carefully poured into a funnel holding a filter paper.The salt will be the filtrate.\n\nSTEP3.Using evaperation or crystallisation to obtain dry salt\n" + Acid(x)
def precipitation():
  return "\n\nSTEP 1.The two solutions of SOLUBLE compounds must be thoroughly mixed together to ensure all the reactants are used up, so the maximum amount of INSOLUBLE salt precipitate is formed.You see the two original clear solutions on mixing forming a cloudy mixture as the insoluble compound is formed, known as the precipitate.\n\nSTEP 2.The mixture is then carefully poured into a funnel holding a filter paper.The precipitated salt can then be filtered off with the filter funnel and paper.\n\nSTEP 3.While still in the filter paper and funnel, the collected solid precipitate is washed with deionised water to remove any remaining soluble salt impurities and just the damp, but otherwise pure, insoluble salt is left.\n\nSTEP 4.The precipitate is then carefully removed from the filter paper into a clean dish or basin to be dried e.g. left out in a dry room or warmed in a pre–heated oven.\n" + pq()

def soluble():
  if d.find("LI") or d.find("NA") or d.find("K") or d.find("RB") or d.find("CS") or d.find("FR") != -1:
      return "soluble reactant\nTitration" + "        " + titration()
  else:
    return "insoluble reactant\nExcess insoluble reactant" + "        " + Excess_insoluble_reactant()

def Cl():
  if c.find("AG") != -1 or c.find("PB") != -1:
    return "insoluble\nPrecipitation" + "        " + precipitation()
  else:
    return soluble()

def CO3():
  if c.find("NA") != -1 or c.find("NH4") != -1 or c.find("K") != -1:
    return soluble()
  else:
    return "insoluble\nPrecipitation" + "        " + precipitation()

def SO4():
  if c.find("CA") != -1 or c.find("PB") != -1 or c.find("BA") != -1:
    return "insoluble\nPrecipitation" + "        " + precipitation()
  else:
    return soluble()
while True:
    if c.find("CL") != -1:
      print(Cl())
      break
    elif c.find("CO3") != -1:
      print(CO3())
      break
    elif c.find("SO4") != -1:
      print(SO4())
      break
    elif c.find("NO3") != -1:
      print(soluble())
      break
    else:
      print("PLs input valid salt")
      c = input("wanted salt")
    


 #print('Right Side is ', (RightSide))
#check if the list with more elements contains the input
  


#Dictionary section
#Metals = ["Li, Na, K, Rb, Cs, Fr, Be, Mg, Ca, Sr, Ba, Ra, B, Al, Ga, In, Tl, C" ]

#figure out 3 chem equations first 
#Acid+Base = Salt+Water
#Acid+Metal = Salt+Hydrogen
#Acid+Carbonate = Salt+H2o+Water
