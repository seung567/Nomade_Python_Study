import requests
import os
 
 
 
url = input()

try : 
    url_staurs = requests.get(url)
    url_val = url_staurs.status_code
except:
    pass


print(url_staurs)
print(url_val)