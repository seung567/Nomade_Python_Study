import requests
import os


def restart() :

    restart_chk = str(input("Do you want to start over? Y/N : ").lower())

    if restart_chk == "y":

        
        os.system("cls")
        main()

    elif restart_chk == "n" :

        print("k bye")

    else :

        print("That's not a valid answer")
        restart()

def main() : 

    print("Welcome to IsItDown.py")
    print("Please write a URLs you want to check. (separated ba comma)")

    urllist = str(input()).lower().split(",")

    for url in urllist :

        url = url.strip()

        if "." not in url :

            print(f'{url} is not a valid URL.')

        else :

            if "https://" not in url :
                
                try :
                    url = f"https://{url}"

                    url_staurs = requests.get(url)
                    url_val = url_staurs.status_code

                except :

                    url_val = 0

                if url_val == 200 :

                    print(f'{url} is up!')

                else :

                    print(f'{url} is Down!')

            else :
                
                try :

                    url_staurs = requests.get(url)
                    url_val = url_staurs.status_code

                except :

                    url_val = 0

                if url_val == 200 :

                    print(f'{url} is up!')

                else :

                    print(f'{url} is Down!')               
    
    restart()

    

main()