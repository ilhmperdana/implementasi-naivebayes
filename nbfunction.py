from csv import reader
from math import sqrt
from math import exp
from math import pi

# Load CSV dataset
def load_csv(filename):
	dataset = list()
	with open(filename, 'r') as file:
		csv_read = reader(file)
		for row in csv_read:
			if not row:
				continue
			dataset.append(row)
	return dataset

# Memisahkan dataset menjadi urut berdasarkan class
# separate dataset based on class	
def separate_by_class(dataset):
	separated = dict()
	for i in range(len(dataset)):
		vector = dataset[i]
		
		#class anggap paling belakang pada dataset
		#class value always on last row
		class_value = vector[-1]
		
		if (class_value not in separated):
			separated[class_value] = list()
			
		separated[class_value].append(vector)
		#print(separated[class_value])
	return separated
filename = 'iris.csv'
dataset = load_csv(filename)
separated = separate_by_class(dataset)
print(separated)