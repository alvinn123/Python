# Alvin Nguyen 2055636
from datetime import datetime

# Import of file ManufacturerList.csv and creation of dictionaries

infile_1 = open("ManufacturerList.csv", "r").readlines()

for i in range(0, len(infile_1)):
    infile_1[i] = infile_1[i].replace('\n', '')

item_id_1 = []
manufacturer_name = []
item_type = []
damaged_indicator = []
for elem in infile_1:
    item_id_1.append(elem.split(",")[0])
    manufacturer_name.append(elem.split(",")[1])
    item_type.append(elem.split(",")[2])
    damaged_indicator.append(elem.split(",")[3])

manufacturer_name_dict = {}
for i in range(0, len(item_id_1)):
    manufacturer_name_dict[item_id_1[i]] = manufacturer_name[i]

item_type_dict = {}
for i in range(0, len(item_id_1)):
    item_type_dict[item_id_1[i]] = item_type[i]

damaged_indicator_dict = {}
for i in range(0, len(item_id_1)):
    damaged_indicator_dict[item_id_1[i]] = damaged_indicator[i]

# Import of file PriceList.csv and creation of dictionaries

infile_2 = open("PriceList.csv", "r").readlines()

for i in range(0, len(infile_2)):
    infile_2[i] = infile_2[i].replace('\n', '')

item_id_2 = []
price = []
for elem in infile_2:
    item_id_2.append(elem.split(",")[0])
    price.append(int(elem.split(",")[1]))

price_dict = {}
for i in range(0, len(item_id_2)):
    price_dict[item_id_2[i]] = price[i]

# Import of file ServiceDatesList.csv and creation of dictionaries

infile_3 = open("ServiceDatesList.csv", "r").readlines()

for i in range(0, len(infile_3)):
    infile_3[i] = infile_3[i].replace('\n', '')

item_id_3 = []
service_date = []
service_date_formatted = []
for elem in infile_3:
    item_id_3.append(elem.split(",")[0])
    service_date.append(elem.split(",")[1])
    service_date_formatted.append(datetime.strptime(elem.split(",")[1], '%m/%d/%Y'))

service_date_dict = {}
for i in range(0, len(item_id_3)):
    service_date_dict[item_id_3[i]] = service_date[i]

service_date_formatted_dict = {}
for i in range(0, len(item_id_3)):
    service_date_formatted_dict[item_id_3[i]] = service_date_formatted[i]

# Part a

# Getting of order of id values when manufacturers are sorted:
id_sorted_by_manufacturer = dict(sorted(manufacturer_name_dict.items(), key=lambda item: item[1])).keys()

# Writing values to file FullInventory.csv:
output = open("FullInventory.csv", "a")
for i in id_sorted_by_manufacturer:
    output.write(i + "," + manufacturer_name_dict[i] + "," + item_type_dict[i] + "," +
                 str(price_dict[i]) + "," + service_date_dict[i] + "," + damaged_indicator_dict[i] + "\n")
output.close()

# Part b

# Getting of order of id values when id values are sorted:
id_sorted = sorted(item_id_1)

# Creation of list with unique types:

item_type_unique = []
for i in item_type:
    if i not in item_type_unique:
        item_type_unique.append(i)

# Writing values to files Inventory.csv:

for i in item_type_unique:
    output = open(i[0].upper() + i[1:] + "Inventory.csv", "a")
    for j in id_sorted:
        if i == item_type_dict[j]:
            output.write(j + "," + manufacturer_name_dict[j] + "," +
                         str(price_dict[j]) + "," + service_date_dict[j] + "," + damaged_indicator_dict[j] + "\n")
    output.close()

# Part c

# Getting of order of id values when prices are sorted:
id_sorted_by_date = dict(sorted(service_date_formatted_dict.items(), key=lambda item: item[1])).keys()

# Writing values to file DamagedInventory.csv:
output = open("PastServiceDateInventory.csv", "a")
for i in id_sorted_by_date:
    if datetime.now() > service_date_formatted_dict[i]:
        output.write(i + "," + manufacturer_name_dict[i] + "," + item_type_dict[i] + "," +
                     str(price_dict[i]) + "," + service_date_dict[i] + "," + damaged_indicator_dict[i] + "\n")
output.close()

# Part d

# Getting of order of id values when prices are sorted:
id_sorted_by_price = dict(sorted(price_dict.items(), reverse=True, key=lambda item: item[1])).keys()

# Writing values to file DamagedInventory.csv:
output = open("DamagedInventory.csv", "a")
for i in id_sorted_by_price:
    if damaged_indicator_dict[i] == "damaged":
        output.write(i + "," + manufacturer_name_dict[i] + "," + item_type_dict[i] + "," +
                     str(price_dict[i]) + "," + service_date_dict[i] + "\n")
output.close()
