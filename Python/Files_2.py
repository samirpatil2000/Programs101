import csv
file_='/Users/samir/Documents/Contacts.csv'

dict_={
    
}
with open(file_, 'r') as file:
    reader = csv.reader(file)
    file_info = []
    for row in reader:
        file_info.append(["+" + row[0]])
    file_info.sort(key=lambda x: x[0])
    with open("contacts2.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Phone Number"])
        writer.writerows(file_info)
        