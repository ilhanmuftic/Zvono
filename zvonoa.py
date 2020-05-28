import pymsteams
from datetime import datetime
from time import sleep


#Raspored Zvonjenja
vrijeme = ['12:00','12:30','12:40','13:10','13:15', '13:45', '13:50','14:20', '14:30','15:00', '15:05','15:35']
zvono = 'Zvoni' #Poruka
# WebHook URL
WebHook = "https://outlook.office.com/webhook/025d3db2-7005-4c93-91f7-48218cbfc4f8@2194bc3d-8d31-4be3-8546-6f385ff8f390/IncomingWebhook/6be93c2a7bc649a69bdb214b5b1219c1/fcf3be0c-94d4-4ab5-8f40-168cbc707a6d"



z = input("Koristi Zvonku? (y/n) * u slucaju n potrebno je unjeti WebHook URL * ")
if z == 'n':
    WebHook = input('Unesi WebHook URL: ')

myTeamsMessage = pymsteams.connectorcard(WebHook) #Spaja se na webhook


now = datetime.now()
current_time = now.strftime("%H:%M:%S") #Uzima trenutno vrijeme

print("Spojio se!",current_time)

def Zvono(poruka,sad):
    myTeamsMessage.text(poruka)
    myTeamsMessage.send()
    print('Zvoni: ',sad)

while True:
    now = datetime.now()
    current_time = now.strftime("%H:%M") #Uzima vrijeme

    for x in range(12): #U rasporedu ima 12 definisanih vremena
        if vrijeme[x] == current_time:
            Zvono(zvono,current_time) #Salje poruku
            sleep(60) #Da ne bi poslao dva puta u minuti