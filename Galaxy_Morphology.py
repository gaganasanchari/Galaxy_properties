from bs4 import BeautifulSoup
import requests

class Myexception(Exception):
    def __str__(self) :
        return 'not found'
    

def Gal_Morph(nm):
    try:
        name=nm
        url='https://ned.ipac.caltech.edu/cgi-bin/gmd?uplist='+str(name)+'%0D%0A&delimiter=bar&nondb=user_objname&attdat_CON=M&attdat=attned'
        html_content = requests.get(url).text

        #Parse the html content
        soup = BeautifulSoup(html_content, "lxml")
        #print(soup.prettify()) # print the parsed data of html

        tr = soup.find("table",attrs={'cellspacing':"1"})
        tr_text=tr.text.replace('\n','')
        tr_text=list(tr_text.split('|'))
        
        dist=tr_text[-1].strip()
        
        if(len(dist)==0):
            raise Myexception        
        
        morph=dist.strip()
                
        return morph
    
        
    except Exception as e:
        print(e)

print(Gal_Morph('PGC 926'))
