import csv
import itertools

#------------------------------------
def csv_reader(file_obj):
	"""
	Read a csv file
	"""
	reader = csv.reader(file_obj)
	# data = list(reader)
	# row_count = len(data)
	# print(row_count)

	for row in itertools.islice(reader,2):
		print(row)

		#row1 = row.split('\t');
		print(row.__len__())
		#print(" ".join(row))  #row


	reader1=csv.reader(file_obj, delimiter = ",")
	data = list(reader1)
	row_count = len(data)
	print(row_count)


	#for i in range (2):
		#print next(reader)
		#print(i)

	#for row in reader:
	#	print(" ".join(row))

#------------------------------------
if __name__ == "__main__":
	csv_path = "cap_innov_data_sp16.csv"
	with open(csv_path, "r", encoding="utf8") as f_obj:
		csv_reader(f_obj)