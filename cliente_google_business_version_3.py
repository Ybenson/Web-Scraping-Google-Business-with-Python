# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 11:28:18 2019

@author: ybenson.augustave

Columns:
CNPJ;NOME_FANTASIA;CEP;DDD_1;TEL_1;DDD_2;TEL2;DDD_3;TEL3

"""

from threading import Thread
import time
import random 
from threading import Thread
import requests
from flask import Flask
import numpy as np
import pandas as pd
app = Flask(__name__)


class Request(Thread):
        
    
    def __init__ (self, nome_fantasia, cnpj):
        Thread.__init__(self)
        self.nome_fantasia = nome_fantasia
        self.cnpj = str(cnpj)
        
    def run(self):

        ## Realiza consulta
        response = requests.get('http://192.168.1.11:5000/GB?nomefantasia={}'.format(self.nome_fantasia))
        print(response.text)
        dic=str(response.text)
        dic= dict(eval(dic))
        response='{};{};{}'.format(dic['Phone'],dic['Email'],dic['Site'])
        print (str(response)) 

        ## Salva resultado
        path = 'C:/Users/ybenson.augustave/Desktop/CAPTCHA_V10_20190605/CAPTCHA/'
        file_write = 'JOB_ENRIQUECIMENTO_PJ_2_3_5__ENR_CNPJ_CAIXA_200K__GB.txt'
        file = open(path+file_write,'a')
        file.writelines(self.cnpj+';'+self.nome_fantasia+';'+response+'\n')
    
   
            
def execPararelism():
    
    
    path = 'C:/Users/ybenson.augustave/Desktop/CAPTCHA_V10_20190605/CAPTCHA/'
    #file_read = 'IMPUT2_ENR_TICKET_2716.TXT'
    file_read = 'INPUT_ENR_TICKET_2716_PJ.txt'
   
    arquivo = pd.read_csv(path + file_read, sep = ';', encoding='utf8', dtype = {'CNPJ':str,'NOME_FANTASIA':str,'DDD_1':str, 'DDD_2':str, 'DDD_3':str, 'TEL_1':str, 'TEL_2':str, 'TEL_3':str})
    
    #print(arquivo)
    #arquivo.loc[6:10, ['CNPJ']]
    
    
    
    # arquivo = open(path + file_read, 'r',encoding='utf8')
    #arquivo_linhas = np.array(arquivo.readlines())
    #arquivo_linhas.shape
    #arquivo_linhas[1]
    
    #arquivo_linhas
    i = 0
    maximum = 120000
    number_batch = 1
    batch_size = 5
    
    # Envia requesições de tamanho 'maximum'
    while(i <= maximum):
        
        print('Lote {} '.format(number_batch))
        
        print(i)
    
        lista_requests = []        

        # Popula a lista
        #items = arquivo.loc[i+1:i+batch_size, ['CNPJ', 'NOME_FANTASIA'] ]
        items = arquivo.loc[i+1:i+batch_size,['CNPJ', 'NOME_FANTASIA'] ]
        arquivo.columns
        arquivo.loc[1:10, 'CNPJ']
          
        for _id, item in items.iterrows():
            #print("{} {}".format(_id, ))
            lista_requests.append(Request(item.get('NOME_FANTASIA'), item.get('CNPJ')))
        
        # Envia o lote
        for item in lista_requests:
            item.start() # run
            
        # Verifica se todas as requisições terminaram  
        try:
            print('Aguardando respostas..')
            while(True):
                if(     not lista_requests[0].isAlive()
                    and not lista_requests[1].isAlive()
                    and not lista_requests[2].isAlive()
                    and not lista_requests[3].isAlive()):
                        break
                else:
                    continue
        except IndexError as ex:
            print(ex)
            print('Finalizado')
             
        i += batch_size
        number_batch += 1
        
        print('\n\n')
        print('Prosseguindo...')
        print('==============================================')
        
    print('EXECUÇÃO FINALIZADA!')
    

execPararelism()





























    


        



       