#-----------------------
#- CSV TO SQL          -
#-----------------------
#- BY: SELLAM ABDELLAH -
#-----------------------
#- 2018 Feb 28         -
#-----------------------

#Load Towns
#Load CSV file as text
ccsv=open("communes.csv","r",encoding="utf8")
cText=ccsv.read()
ccsv.close()

#Split CSV text into lines
cLines=cText.split("\n")

#Split CSV lines int columns
communes=[]
for cLine in cLines:
    communes.append(cLine.split(";"))

#Load Provences
#Load CSV file as text
wcsv=open("wilayas.csv","r",encoding="utf8")
wText=wcsv.read()
wcsv.close()

#Split CSV text into lines
wLines=wText.split("\n")

#Split CSV lines int columns
wilayas=[]
for wLine in wLines:
    wilayas.append(wLine.split(";"))

#Make Provences' sql insert
ProvTbl="Wilaya"#Name Of Provences' Table
ProvIdCol="id"#Name Of Provences' id Field (column)
ProvNmCol="Name"#Name Of Provences' name Field (column)
wsql=open("wilayas.sql","w",encoding="utf8")
wsql.write('INSERT INTO %s (%s,%s) VALUES\n'%(ProvTbl,ProvIdCol,ProvNmCol))
num=len(wilayas)
wsql.write('(%s,"%s")'%(wilayas[0][1],wilayas[0][0]))
for i in range(1,num):
    wsql.write(',\n(%s,"%s")'%(wilayas[i][1],wilayas[i][0]))
wsql.write(';\n')
wsql.close()

#Make Towns' sql insert
TownTbl="Commune"#Name Of Towns' Table
TownIdCol="id"#Name Of Towns' id Field (column)
TownNmCol="Name"#Name Of Towns' name Field (column)
TownPrCol="Wilaya"#Name Of Towns' provence Field (column)
csql=open("Commune.sql","w",encoding="utf8")
csql.write('INSERT INTO %s (%s,%s,%s) VALUES\n'%(TownTbl,TownIdCol,TownPrCol,TownNmCol))
num=len(communes)
csql.write('(1,%s,"%s")'%(communes[0][1],communes[0][0]))
for i in range(1,num):
    csql.write(',\n(%d,%s,"%s")'%(i+1,communes[i][1],communes[i][0]))
csql.write(';\n')
csql.close()
