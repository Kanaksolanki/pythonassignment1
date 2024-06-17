import csv
with open("C:/Users/kanak solanki/OneDrive/Desktop/Book1.csv",'r')as csvfile:
  csvFile = csv.reader(csvfile)
  for lines in csvFile:
        print(lines)