from selenium import webdriver 
from time import sleep 
from random import randrange


class Instabot:

    message = """
            Ciao! Il nostro Supremo Leader sta dormendo o si trova al cesso 😂, risponderà il prima possibile.
            Nel frattempo puoi dialogare con me, io sono Cassandra, una IA molto semplice. Ecco cosa puoi fare con me:

            -- scrivi '#meme' per ricevere un meme
            -- scrivi '#link' per ricevere il link 
                al nostro account tellonym
            -- scrivi '#address' per 
                ricevere l'indirizzo 
                del nostro wallet di bitcoin 
                per effettuare donazioni 
            -- scrivi '#scrivounospot' per 
                scrivere uno spot che
                pubblicheremo come tell
                nelle storie (in totale
                anonimato, quest'ultimo è
                garantito al 100%
                da tellonym)
            
            #teamSpotted #WeloveYou #AveSupremoLeader 
             
              """


    requests = ['#meme','#link','#address','#scrivounospot']
    memelist = ['/MEME/meme1.jfif', '/MEME/meme2.png', '/MEME/meme3.jpg', '/MEME/meme4.jpeg', '/MEME/meme5.jpg', '/MEME/meme6.jpg', '/MEME/meme7.jpg']
    tellonym_link = 'tellonym.me/Siracusa_spotted_official'
    address = '₿ donazioni: 38rGrsBvZ4BytUdJXFPokujWRDtM7D2zwc'
    sendmeaspot = '''scrivici il tuo spot sotto 
                    questo messaggio, noi lo
                    posteremo come tell nelle
                    storie!

                    *** Ricorda! lo spot deve
                    terminare con '#spot', 
                    altrimenti il programma
                    non riuscirà a riconoscere
                    lo spot! *** 
                    #facciattenzione 

                    #storie #abombazza #dope
                    #spottacomesenoncifosseundomani
                    #lottaallultimospot
                    #grazieperlospot
                '''
    spotregistered = """
                        Grazie, il tuo spot è stato
                        inoltrato con successo.
                        Verrà pubblicato il prima
                        possibile.
                        
                     """

    def __init__(self, username, password):
        self.driver = webdriver.Chrome()
        self.username =  username
        
        self.driver.get("https://instagram.com")
        sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div/button[1]').click()
        login_field = self.driver.find_element_by_xpath("//input[@name=\"username\"]").send_keys(username)
        password_field = self.driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(password)
        sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button/div').click()
        sleep(2)
        code = input("insert code: \n")
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div[1]/div/form/div[1]/div/label/input').send_keys(code)
        sleep(3)
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div[1]/div/form/div[2]/button').click()
        sleep(5)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/section/div/button').click()
        sleep(5)
        try:
            self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]').click() 
            sleep(2)
        except:
            sleep(2)
            self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]').click() 
            sleep(2)
    
    def AutoAnswer(self):

        while True:
            sleep(1)
            
            try:
                ChatNum = self.driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[2]/a/div/div/div[@class=\"bqXJH\"]').get_attribute("/div[@class=\"bqXJH\"]")
                ChatNum_var = str(ChatNum)
                var_int = int()

                while (ChatNum_var == "{var_int}" and var_int > 0):
                    self.driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[2]/a/svg').click()

                    for i in range(1,ChatNum+1):
                        LastMex = self.driver.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[3]/div/div/div/div/div[{ChatNum}]/a/div/div[2]/div[2]/div/div/span[1]/span[@class=\"_7UhW9   xLCgt       qyrsm KV-D4           se6yk        \"]').get_attribute("/span[@class=\"_7UhW9   xLCgt       qyrsm KV-D4           se6yk        \"]")
                        if (LastMex == Instabot.message):
                            pass
                        elif (LastMex == meme_pic or LastMex == Instabot.tellonym_link or LastMex == Instabot.address or LastMex == Instabot.sendmeaspot):
                            pass
                        elif (Instabot.requests in LastMex and LastMex != Instabot.message and LastMex != Instabot.sendmeaspot):
                            if (LastMex == '#meme' or ("#meme" in LastMex) ):
                                self.driver.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[3]/div/div/div/div/div[{ChatNum}]/a/div/div[2]/div[1]/div/div').click()
                                random_meme = randrange(0,7,1)
                                meme_pic = open(Instabot.memelist[random_meme],'r')
                                self.driver.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea').send_keys(meme_pic)
                                self.driver.find_element_by_xpath('/html/body/div[7]/div/div/div/div[2]/div[2]/button').click()
                            elif (LastMex == '#link' or ("#link" in LastMex) ):
                                self.driver.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[3]/div/div/div/div/div[{ChatNum}]/a/div/div[2]/div[1]/div/div').click()
                                self.driver.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea').click()
                                self.driver.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea').send_keys(Instabot.tellonym_link)
                                self.driver.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()
                            elif (LastMex == '#address' or ("#address" in LastMex) ):
                                self.driver.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[3]/div/div/div/div/div[{ChatNum}]/a/div/div[2]/div[1]/div/div').click()
                                self.driver.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea').click()
                                self.driver.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea').send_keys(Instabot.address)
                                self.driver.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()
                            elif (LastMex == '#scrivounospot' or ("#scrivounospot" in LastMex) ):
                                self.driver.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[3]/div/div/div/div/div[{ChatNum}]/a/div/div[2]/div[1]/div/div').click()
                                self.driver.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea').click()
                                self.driver.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea').send_keys(Instabot.sendmeaspot)
                                self.driver.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()
                        else:
                            if ("#spot" in LastMex and ("#scrivounospot" not in LastMex) ):
                                try:
                                    self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/div[2]/a').click()
                                    self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div/button[2]').click()
                                    self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div[5]/div/div/div[1]/div[2]/div/div[4]/div[1]/div/textarea').click()
                                    self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div[5]/div/div/div[1]/div[2]/div/div[4]/div[1]/div/textarea').send_keys(LastMex)
                                    self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div[5]/div/div/div[1]/div[2]/div/div[4]/div[3]/div/div[2]/form/button/div/div').click()
                                except:
                                    self.driver.get("https://tellonym.me/Siracusa_spotted_official")
                                    self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div/button[2]').click()
                                    self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div[5]/div/div/div[1]/div[2]/div/div[4]/div[1]/div/textarea').click()
                                    self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div[5]/div/div/div[1]/div[2]/div/div[4]/div[1]/div/textarea').send_keys(LastMex)
                                    self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div[5]/div/div/div[1]/div[2]/div/div[4]/div[3]/div/div[2]/form/button/div/div').click()
                                finally:
                                    self.driver.get("https://www.instagram.com/siracusa_spotted_official/")
                                    self.driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[2]/a/svg').click()
                                    self.driver.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[3]/div/div/div/div/div[{ChatNum}]/a/div/div[2]/div[1]/div/div').click()
                                    self.driver.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea').click()
                                    self.driver.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea').send_keys(Instabot.spotregistered)
                                    self.driver.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()
                            else:
                                self.driver.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[3]/div/div/div/div/div[{ChatNum}]/a/div/div[2]/div[1]/div/div').click() 
                                self.driver.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea').click()
                                self.driver.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea').send_keys(Instabot.message)
                                self.driver.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()

                ChatNum = self.driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[2]/a/div/div/div[@class=\"bqXJH\"]').get_attribute("/div[@class=\"bqXJH\"]")
                ChatNum_var = str(ChatNum)
                var_int = int()
            
            except:
                print("No messages for the moment...")
                sleep(3)