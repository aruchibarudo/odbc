from django.shortcuts import render
from django.http import HttpResponse
from configparser import ConfigParser

ODBC_INI = 'odbc.ini'

def index(request):
    sections = []
    """ 
    config = ConfigParser()
    config.optionxform = str
    config.readfp(open(ODBC_INI))
    sections = config.sections
    """
    sections = get_ini(ODBC_INI)
    context = { 'list' : sections }
    return render(request,'list.html',context)

def get_ini(ODBC_INI):
    config = ConfigParser()
    config.optionxform = str
    config.readfp(open(ODBC_INI))
    return config.sections


