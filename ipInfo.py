
# pip install ip2geotools

from distutils.command.clean import clean
from time import sleep
import requests
from bs4 import BeautifulSoup
import os
from ip2geotools.databases.noncommercial import DbIpCity

print("""
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠁⠀⠀⠀⠀⠈⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀⢠⠀⢠⣤⣤⣀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⢸⠀⢸⡇⠀⣸⠆⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⢸⠀⢸⡟⠛⠉⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠸⠀⠸⠇⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⠀⠀⠀⠀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡀⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿

""")

userChoice = input("1) Check what's your ip\n2) Different ip\n\n:$") 
while True:
  if userChoice == "1":
    
    os.system('cls' if os.name == 'nt' else 'clear')
    #site
    ip = 'https://www.myip.com/'        # адрес мобильной версии
    headers = {'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'}

    r = requests.get(ip, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')

    ipGet = soup.find('div', class_='texto_1').text
    countryGet = soup.find('div', class_='info_2').text  # не span, как в десктопной
    correctIP = ipGet[1:16]
    print("\n---------------------------")
    print("\nYour ip is: " + correctIP)
    print("Country: " + countryGet)
    print("\n---------------------------") 
    break

  elif userChoice == "2":
    try:
      os.system('cls' if os.name == 'nt' else 'clear')
      ip = input("Put IP: ")
      if ip == "exit": break
      else:
        response = DbIpCity.get(ip, api_key='free')
        print("\n---------------------------")
        print("Country: " + str(response.country))
        print("Region: " + str(response.region))
        print("City: " + str(response.city))
        print("\nlatitude: "+str(response.latitude) + " longitude: "+str(response.longitude))
        print("\n---------------------------")
        break
      

    except:
      print("IP not found")
      sleep(1)
  elif userChoice == "exit":
    break
  else:
    userChoice = input(":$") 