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

#Query

while True:
    
    query = input("Enter manufacturer and item type or press q to quit: ").lower()

    if query != "q":

        #Part i

        infile_query = open("FullInventory.csv", "r").readlines()

        id_of_inventories = []
        brand_query_lower = []
        type_query_lower = []
        prices_of_inventories = []
        dates_query = []
        condition = []
        for i in infile_query:
            id_of_inventories.append(i.split(",")[0]) 
            brand_query_lower.append(i.split(",")[1].lower().replace(" ", ""))
            type_query_lower.append(i.split(",")[2].lower())
            prices_of_inventories.append(float(i.split(",")[3]))
            dates_query.append(datetime.strptime(i.split(",")[4], '%m/%d/%Y'))
            condition.append(i.split(",")[5].replace("\n", ""))

        query_words = query.split()

        brand_words = []
        type_words = []

        for i in query_words:
            if i in brand_query_lower:
                brand_words.append(i)
            if i in type_query_lower:
                type_words.append(i)

        is_combination_in_database = False

        for i in range(0, len(brand_query_lower)):
            if brand_words != [] and type_words != []:
                if brand_query_lower[i] == brand_words[0] and type_query_lower[i] == type_words[0]:
                    is_combination_in_database = True
                    break

        

        if len(brand_words) != 1 or len(type_words) != 1 or is_combination_in_database == False or brand_words == [] or type_words == []:
            print("No such item in inventory")
            
        else:
            
            

            #Part ii

            prices_query = []

            for i in range(0, len(brand_query_lower)):
                if brand_query_lower[i] == brand_words[0] and type_query_lower[i] == type_words[0]:
                    prices_query.append(prices_of_inventories[i])

            max_price = max(prices_query)

            for i in range(0, len(brand_query_lower)):
                if brand_query_lower[i] == brand_words[0] and type_query_lower[i] == type_words[0] and prices_of_inventories[i] == max_price:
                    if dates_query[i] > datetime.now() and condition[i] != "damaged":
                        print("Your item is: " + id_of_inventories[i] + " " + brand_query_lower[i][0].upper() +
                                brand_query_lower[i][1:] + " " + type_query_lower[i] + " " + str(prices_of_inventories[i]))

            #Part iii

            for i in range(0, len(brand_query_lower)):
                if brand_query_lower[i] != brand_words[0] and type_query_lower[i] == type_words[0] and condition[i] != "damaged" :
                    if dates_query[i] > datetime.now() and prices_of_inventories[i] >= max_price * 0.75 and prices_of_inventories[i] <= max_price * 1.25:
                        print("You may, also, consider: " + id_of_inventories[i] + " " + brand_query_lower[i][0].upper() +
                                brand_query_lower[i][1:] + " " + type_query_lower[i] + " " + str(prices_of_inventories[i]))

    else:
        break


    










    
