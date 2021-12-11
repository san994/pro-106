import numpy as np
import csv

def getDataSource(data_path):
    ice_creamSales = []
    temperature = [] 
    with open(data_path) as f:
        reader = csv.DictReader(f)
        for row in reader:
            temperature.append(float(row['Days Present']))
            ice_creamSales.append(float(row['Marks In Percentage']))

    return {'x':temperature,'y':ice_creamSales}

def findCorrelation(data_source):
    correlation = np.corrcoef(data_source['x'],data_source['y'])

    print("correlation is ",correlation[0,1])

def setup():
    data_path = 'marks vs attend.csv'
    data_source = getDataSource(data_path)
    findCorrelation(data_source)

setup()