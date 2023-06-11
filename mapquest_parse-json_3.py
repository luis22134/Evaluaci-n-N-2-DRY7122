import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "gT0KyynGju8cjZ7HOsfQt7stWD5jZ8bk" 

while True:
   orig = input("Lugar de Inicio: ")
   if orig == "quit" or orig == "q":
        break
   dest = input("Destino: ")
   if dest == "quit" or dest == "q":
        break
   url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})
   print("URL: " + (url))
   json_data = requests.get(url).json()
   json_status = json_data["info"]["statuscode"]
   if json_status == 0:
       print("API Status: " + str(json_status) + " = A successful route call.\n")
       print("=============================================")
       print("Directions from " + (orig) + " to " + (dest))
       print("Trip Duration:   " + (json_data["route"]["formattedTime"]))
       print("Kilometers:      " + str((json_data["route"]["distance"])*1.61))
       print("=============================================")


       

      









