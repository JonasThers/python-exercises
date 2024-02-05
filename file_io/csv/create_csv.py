import csv

list_of_cars = [
    {
        "model": "Ford",
        "color": "Red",
        "fuel": "Diesel"
    },
    {
        "model": "Tesla",
        "color": "Black",
        "fuel": "Litium batteries"
    },
    {
        "model": "Mustang",
        "color": "Red",
        "fuel": "Premium"
    }
]

with open('cars.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['Model', 'Colour', 'Fuel'])
    for i in list_of_cars:
        writer.writerow([i['model'], i['color'], i['fuel']])
    f.close()
    
    
    