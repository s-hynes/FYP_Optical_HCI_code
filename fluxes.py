import matplotlib.pyplot as plt
import csv

import csv
with open('fluxes.csv', mode ='r')as file:
  csvFile = csv.reader(file)
  for lines in csvFile:
        print(lines)

