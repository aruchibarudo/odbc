from django.shortcuts import render
from django.http import HttpResponse
from configparser import ConfigParser

ODBC_INI = 'odbc.ini'

def get_ini(ODBC_INI):
    config = ConfigParser()
    config.optionxform = str
    config.readfp(open(ODBC_INI))
    return config

def index(request):
    sections = []
    """ 
    config = ConfigParser()
    config.optionxform = str
    config.readfp(open(ODBC_INI))
    sections = config.sections
    """
    sections = ini.sections
    context = { 'list' : sections }
    return render(request,'list.html',context)

def get_section(request, section):
    options = ini[section]
    values = ini[section].values()
    context = { 'items' : options, 'values' : values }
    return render(request, 'section.html',context)

ini = get_ini(ODBC_INI)

