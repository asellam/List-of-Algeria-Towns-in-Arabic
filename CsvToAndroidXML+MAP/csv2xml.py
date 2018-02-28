#-------------------------------------------
#- CSV TO ANDROID XML + JAVA MAP Converter -
#-------------------------------------------
#- BY: SELLAM ABDELLAH                     -
#-------------------------------------------
#- 2018 Feb 28                             -
#-------------------------------------------

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

#Make Provences' xml resource file
wxml=open("wilayas.xml","w",encoding="utf8")
wxml.write('<?xml version="1.0" encoding="utf-8"?>\n')
wxml.write('<resources>\n')
wxml.write('    <string-array name="Wilaya">\n')
wxml.write('        <item>@string/WilayaDef</item>\n')
wid=1
for wilaya in wilayas:
    wxml.write('        <item>%d. '%(wid)+wilaya[0]+'</item>\n')
    wid=wid+1
wxml.write('    </string-array>\n')
wxml.write('</resources>\n')
wxml.close()

#Make Towns' xml resource file
wxml=open("communes.xml","w",encoding="utf8")
wxml.write('<?xml version="1.0" encoding="utf-8"?>\n')
wxml.write('<resources>\n')
wxml.write('    <string-array name="wilayaZero">\n')
wxml.write('        <item>@string/CommuneDef</item>\n')
wxml.write('    </string-array>\n')
wid=1
for wilaya in wilayas:
    wxml.write('    <string-array name="W%02d">\n'%(wid))
    for commune in communes:
        if(commune[1]==wilaya[1]):
            wxml.write('        <item>'+commune[0]+'</item>\n')
    wxml.write('    </string-array>\n')
    wid=wid+1
wxml.write('</resources>\n')
wxml.close()

#Make a java Provence->TownList HashMap initialisation function
jFile=open("mapmake-ar.java","w",encoding="utf8")
jFile.write('    HashMap getWilayaMap()\n')
jFile.write('    {\n')
jFile.write('        HashMap wMap = new HashMap<String,Integer>();\n')
wid=1
for wilaya in wilayas:
    jFile.write('        wMap.put("%d. '%(wid)+wilaya[0]+'",R.array.W%02d);\n'%(wid))
    wid=wid+1
jFile.write('        return wMap;\n')
jFile.write('    }\n')
jFile.close()
