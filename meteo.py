#!/usr/bin/env python3

import requests
import re

def getMeteoULaval():
    '''Returns a dict containing the info from Météo-Laval's website.
       This function does not get the average and extreme values.'''
    page = requests.get('http://meteo-laval-web.gel.ulaval.ca')
    donnees = re.findall('id="([_a-z\d]*)" class="data">', page.text)
    donnees2 = re.findall('span id="([a-z_]*)">', page.text) 
    valeurs = re.findall('data"\>(-?[\.\d]*) .*\<', page.text)
    valeurs2 = re.findall('\</span\>\<span id=".*\>(.*)\</span\>', page.text) 
    valeurs = list(float(i) for i in valeurs)
    theDict = dict(zip(donnees, valeurs))
    theDict2 = dict(zip(donnees2, valeurs2))
    theDictComplete = {**theDict, **theDict2}
    return theDictComplete

if __name__ == '__main__':
    donnees = getMeteoULaval()
    print(donnees)
