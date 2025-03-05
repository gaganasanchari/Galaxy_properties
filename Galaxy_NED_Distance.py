from bs4 import BeautifulSoup
import requests

class Myexception(Exception):
    def __str__(self) :
        return 'not found'
#function to returns the distance to the galaxy from the name iof the galaxy in Mpc.
def Gal_Dist(nm):
    try:
        name=nm
        url='https://ned.ipac.caltech.edu/cgi-bin/gmd?uplist='+str(name)+'&delimiter=bar&nondb=user_objname&position=z&distance_CON=dmpc&gphotoms=q_value&gphotoms=q_unc&gphotoms=ned_value&gphotoms=ned_unc&distance=avg'
        html_content = requests.get(url).text

        # Parse the html content
        soup = BeautifulSoup(html_content, "lxml")
        #print(soup.prettify()) # print the parsed data of html

        tr = soup.find("table",attrs={'cellspacing':"1"})
        tr_text=tr.text.replace('\n','')
        tr_text=list(tr_text.split('|'))
        
        dist=tr_text[-1].strip()
        
        if(len(dist)==0):
            raise Myexception        
        
        dist=float(dist.strip())
                
        return dist
    
        
    except Exception as e:
        print(e)


