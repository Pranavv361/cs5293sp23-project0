import urllib.request

#Replicating the User inputs to download the pdf
def fetchIncidents(url):
    headers = {}
    headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"                          

    data = urllib.request.urlopen(urllib.request.Request(url, headers=headers)).read()
    try:
        with open('incidents.pdf', 'wb') as f:
            f.write(data)
            #print('PDF downloaded and saved as incidents.pdf')
    except:
        print(f'Error downloading PDF at ',url)

          
