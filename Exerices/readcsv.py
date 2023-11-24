import csv

try:

    with open('file.csv', 'r') as csvfile:
        csvreader = csv.reader(csvfile)
  
        next(csvreader)

        for line in csvreader:
            name, age, gender = line
            age = int(age)

            print(f"Name: {name}, Age: {age}, Gender: {gender}")

except Exception as e:
    print(f"An error occurred: {e}")