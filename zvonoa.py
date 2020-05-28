import pymsteams
from datetime import datetime
from time import sleep


#Raspored Zvonjenja
vrijeme = ['12:00','12:30','12:40','13:10','13:15', '13:45', '13:50','14:20', '14:30','15:00', '15:05','15:35']
zvono = 'Zvoni' #Poruka
# WebHook URL
WebHook = "<WebHook URL>"

myTeamsMessage = pymsteams.connectorcard(WebHook) #Spaja se na webhook


now = datetime.now()
current_time = now.strftime("%H:%M:%S") #Uzima trenutno vrijeme

print("Spojio se!",current_time)

def Zvono(poruka,sad):
    myTeamsMessage.text(poruka)
    myTeamsMessage.send()
   

while True:
    now = datetime.now()
    current_time = now.strftime("%H:%M") #Uzima vrijeme

    for x in range(12): #U rasporedu ima 12 definisanih vremena
        if vrijeme[x] == current_time:
            Zvono(zvono) #Salje poruku
            print('Zvoni: ',current_time)
            sleep(60) #Da ne bi poslao dva puta u minuti
