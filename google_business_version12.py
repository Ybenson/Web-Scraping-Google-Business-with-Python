# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 16:15:38 2019

@author: ybenson.augustave
"""

import requests
from flask import request
import re
import time
from flask import Flask
import numpy as np
app = Flask(__name__)
import random
from bs4 import BeautifulSoup
from unidecode import unidecode

import winsound
#===================================================================================================================
# @app.route is a decorator used to match URLs to view functions in Flask apps.
#===================================================================================================================
@app.route("/GB",methods=['GET', 'POST'])

def consulta():  # A CLASS PRINCIPAL
    q=request.args.get('nomefantasia')
    
    tel_1 = request.args.get('tel_1')
    tel_2 = request.args.get('tel_2')
    tel_3 = request.args.get('tel_3')
    
    cep_1 = request.args.get('cep_1')
    cep_2 = request.args.get('cep_2')
    cep_3 = request.args.get('cep_3')
    
    
    q=q.lower()
    q=(unidecode(q))
    url1 = "{}{}".format("https://www.google.com/search?q=", q, "&oq=", q)    
    headers={ "Content-type": "application/x-www-form-urlencoded; charset=UTF-8",
                "Accept": "text/plain, */*; q=0.01",
                "Cache-Control": "no-cache",
                "Pragma": "no-cache",
                "x-wap-profile": "http://wap.samsungmobile.com/uaprof/GT-S7562.xml",
                "User-Agent": "Mozilla/5.0 (Linux; U; Android 4.1.4; pt-br; GT-S1162L Build/IMM76I) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"}
    
    headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3'
    ,'cache-control': 'max-age=0'
    ,'upgrade-insecure-requests': '1'
    ,'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36'
    ,'x-client-data': 'CIu2yQEIpLbJAQjEtskBCKmdygEIqKPKAQixp8oBCOKoygEI8anKAQ=='
     }

    
    while(True):
        
        response = 'NO REQUEST'
        
        try:
         
            response = requests.get(url1, headers = headers)
            
         
        except requests.exceptions.ConnectionError:
            print("Sem conexão com a internet...")
            continue
        if response.status_code == 200: # Si tudo está okay
            print('Conexão OK!')
            break
        else:
            print("ERRO DE 429 - Conexão perdida...")
            updateOnline()
            playSound()
            continue
    ########################################################################################################################
                                        # CHECA GOOGLE BUSSINESS
    ########################################################################################################################
    soup = BeautifulSoup(response.text)  
    selector = 'html > body > div > div > div > div > div > div > div > div > div > div > div'
    xpdopen = soup.select(selector)
    xpdopen = np.array(xpdopen) 
    print(xpdopen)
      
    
    if xpdopen.shape != (0,):
        ###################################################################################################################
                                        # NOME DA EMPRESA QUE ESTÁ NO GOOOGLE
        ###################################################################################################################
        soup = BeautifulSoup(response.text)
        selector = 'html > body > div > div > div > div > div > div >div > div > div > div > div > div'
        found = (soup.select(selector))
        if found!=[]:

            soup = BeautifulSoup(str(found[0]),)
            selector = 'html > body > span'
            found = soup.select(selector)
            name = soup.find('span').contents
            name= str(name).strip("['']")
            name=name.lower()
            name=(unidecode(name))
            

            soup = BeautifulSoup(response.text,)
            selector = 'html > body > div > div > div > div > div > div > div > div > div > div > div > div > div > div > div > div > div > .LrzXr'
            endereco_cep = (soup.select(selector))
            endereco_cep= soup.find("span", class_="LrzXr").contents
            endereco_cep= str(endereco_cep).strip("['']")
            endereco_cep = str(endereco_cep)
            endereco_cep  = endereco_cep.replace('-', '')
            confirma_cep = False
            if ( (cep_1 in endereco_cep) or (cep_2 in endereco_cep) or (cep_3 in endereco_cep) ):
                confirma_cep  = True
            ###################################################################################################################
                                            # PEGAR O TELEFONE DA EMPRESA QUE ESTÁ NO GOOGLE
            ###################################################################################################################
            soup = BeautifulSoup(response.text)
            selector = 'html > body > div > div > div > div > div > div > div > div > div > div > div > div > div > div > div > span > span > span'
            phones = (soup.select(selector))
            if phones!=[]:
                phones
                soup = BeautifulSoup(str(phones[0]))
                phones = soup.find('span').contents
                phones= str(phones).strip("['']")
                phones=phones.replace('(','')
                phones=phones.replace(')','')
                phones=phones.replace(' ','')
                phones=phones.replace('-','')
                phones
                confirma_phone = False
                if ( (tel_1 in phones) or (tel_2 in phones) or (tel_3 in phones) ):
                    confirma_phone  = True
              
                if (name == q or confirma_cep or confirma_phone):                
                    
                    soup = BeautifulSoup(response.text)
                    selector = 'html > body > div > div > div > div > div > div > div > div > div > div > div > div > div > div > div > div > div > div > a'
                    found = (soup.select(selector))
                    if found!=[]:
                        link=found[0]['href']
                        link=link.split('/')
                        link=link[2]
                        link= "http://{}".format(link)
                        
                        headers={ "Content-type": "application/x-www-form-urlencoded; charset=UTF-8",
                                    "Accept": "text/plain, */*; q=0.01",
                                    "Cache-Control": "no-cache",
                                    "Pragma": "no-cache",
                                    "x-wap-profile": "http://wap.samsungmobile.com/uaprof/GT-S7562.xml",
                                    "User-Agent": "Mozilla/5.0 (Linux; U; Android 4.1.4; pt-br; GT-S1162L Build/IMM76I) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"}
                        
                        headers = {
                        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3'
                        ,'cache-control': 'max-age=0'
                        ,'upgrade-insecure-requests': '1'
                        ,'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36'
                        ,'x-client-data': 'CIu2yQEIpLbJAQjEtskBCKmdygEIqKPKAQixp8oBCOKoygEI8anKAQ=='
                        }
                
                        
                        # Retorna vazio se o site encontrado for a pagina do facebook
                        black_list = ['facebook','>','wikipedia','gif','›', '...', 'mercadolivre', 'jusbrasil', 'wikiaves', 'vejasp', 'vivareal.com','facebook', 'apontador',
                                          'sexy', 'porno', '.adult','FLORDELOTUS', 'png','jpg', 'consultacnpj', 'dicio','sentry','significados']
                        analisa_black_list = [item in link for item in black_list]        
                        if(any(analisa_black_list)):
                            emails = ''
                            link=''
                            return str({'Empresa':q, 'Phone':phones, 'Email': '', 'Site': ''})
                        # Retorna vazio caso não consiga acessar o site da empresa
                        try:
                            response = requests.get(link, headers = headers)
                        except requests.exceptions.ConnectionError as ex:
                            print(ex)
                            response.status_code = 404
                        
                        except requests.exceptions.TooManyRedirects as ex:
                            response.status_code = 404
                            print(ex)
                        if response.status_code == 200:
                            emails = re.findall('([\d\w\.]+@[\d\w\.\-]+\.\w+)', response.text)
                        
            
                        # get Email 
                            if emails and phones:
                                emails = emails[0]
                                black_list = ['facebook','>','wikipedia','bluebird@3.5.5','loader@0.1.6','gif','›', '...', 'mercadolivre','html5shiv@3.7.3', 'jusbrasil', 'wikiaves', 'vejasp', 'vivareal.com', 'apontador',
                                      'sexy', 'porno', '.adult','FLORDELOTUS', 'png','jpg', 'consultacnpj', 'dicio','sentry','significados','shim@0.6.0']
                                analisa_black_list = [item in emails for item in black_list]        
                                if(any(analisa_black_list)):
                         
                                    emails = ''
                                    result=({'Empresa':q,'Phone':phones, 'Email':'', 'Site':link})
                                    return str(result)
                                else:
                                    result=({'Empresa':q,'Phone':phones, 'Email':emails, 'Site':link})
                                    return str(result)
                            elif link:
                                emails = ''
                                result=({'Empresa':q,'Phone':phones, 'Email':'', 'Site':link})
                                return str(result)
                            elif phones:
                                emails = ''
                                result=({'Empresa':q,'Phone':phones, 'Email':'', 'Site':link})
                                return str(result)
                            else:
                                emails = emails[0]
                                black_list = ['facebook','>','wikipedia','bluebird@3.5.5','gif','loader@0.1.6','›', '...', 'mercadolivre','html5shiv@3.7.3', 'jusbrasil', 'wikiaves', 'vejasp', 'vivareal.com', 'apontador',
                                      'sexy', 'porno', '.adult','FLORDELOTUS', 'png','jpg', 'consultacnpj', 'dicio','sentry','significados','shim@0.6.0']
                                analisa_black_list = [item in emails for item in black_list]        
                                if(any(analisa_black_list)):
                         
                                    emails = ''
                                    result=({'Empresa':q,'Phone':phones, 'Email':'', 'Site':link})
                                    return str(result)
                                else:
                                    result=({'Empresa':q,'Phone':phones, 'Email':emails, 'Site':link})
                                    return str(result)
                                
                            # get Telefone
                            if phones:
                                emails = emails[0]
                                result=({'Empresa':q,'Phone':phones, 'Email':emails, 'Site':link})
                                return str(result)
                                black_list = ['facebook','>','wikipedia','bluebird@3.5.5','gif','›', '...', 'mercadolivre','html5shiv@3.7.3', 'jusbrasil', 'wikiaves', 'vejasp', 'vivareal.com', 'apontador',
                                      'sexy', 'porno', '.adult','FLORDELOTUS','loader@0.1.6', 'png','jpg', 'consultacnpj', 'dicio','sentry','significados','shim@0.6.0']
                                analisa_black_list = [item in emails for item in black_list]        
                                if(any(analisa_black_list)):
                         
                                    emails = ''
                                    result=({'Empresa':q,'Phone':phones, 'Email':'', 'Site':link})
                                    return str(result)
                                else:
                                    result=({'Empresa':q,'Phone':phones, 'Email':emails, 'Site':link})
                                    return str(result)
                            else:
                                emails = ''
                                result=({'Empresa':q,'Phone':phones, 'Email':'', 'Site':link})
                                return str(result)
                        else:
                            emails = ''
                            
                            result=({'Empresa':q, 'Phone':phones, 'Email': '', 'Site':link})
                            return str(result)
                    else:
                        emails = ''
                            
                        result=({'Empresa':q, 'Phone':phones, 'Email': '', 'Site': ''})
                        return str(result)
                else:
                    result=({'Empresa':q, 'Phone':'', 'Email': '', 'Site': ''})
                    return str(result)
            else:
                result=({'Empresa':q, 'Phone':'', 'Email': '', 'Site': ''})
                return str(result)
        else:
            result=({'Empresa':q, 'Phone':'', 'Email': '', 'Site': ''})
            return str(result)
    else:
        result=({'Empresa':q, 'Phone':'', 'Email': '', 'Site': ''})
        return str(result)


# função responsavel por comunicar o robo do modem vivo de que o ip foi localizado e bloqueado (429 - Too Many Requests)
def updateOnline():
    f = open("T:\\ROBOTS\\GB.txt", "w")
    f.write("TRUE")
    f.close()
    print('Status atualizado')

def playSound():
    for i in range(0,10):
        time.sleep(0.130)
        duration = 800  # milliseconds
        freq = 2600  # Hz
        winsound.Beep(freq, duration)
    
app.run(host='192.168.1.11')




