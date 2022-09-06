#rumble donwload video :)
#use beatifulsoup
# and or... chromedrive (selenium)
import requests

#url = "https://google.com/"
url = "https://rumble.com/v1iraap-diretores-do-datafolha-e-vox-populi-dizem-que-eleio-j-est-decidida-s-falta-.html"
r = requests.get(url)

# TARGET exemple -> Local video: <video muted playsinline [...] src="https://sp.rmbl.ws/s8/2/H/l/2/E/Hl2Ef.caa.mp4?u=3&b=0"

#print(r.text) #print request

##save request in file 'request.txt'2
#with open('request.txt', 'w') as f:
#    f.write(r.text)
#f.close()
