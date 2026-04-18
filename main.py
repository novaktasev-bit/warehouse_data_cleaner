import csv

class Product:
    def __init__(self, name, sku, price, qty):
        self.name = name
        self.sku = sku
        try:
            self.price = float(price)
        except:
            self.price = 0.1

        try:
            self.qty = int(qty)
        except:
            self.qty = 0

    
    def error_checker(self):
        errors = []

        if self.name == "":
            errors.append("Name should not be blank.")
        
        if len(self.sku) != 6:
            errors.append("SKU should have 6 characters.")

        if self.price <= 0:
            errors.append("Price should be a positive number")

        if self.qty <0:
            errors.append("Quantity should not be a negative number")

        return errors
    
    def clean_data(self):
        if self.name == "":
            self.name = "UNKNOWN PART"

        if len(self.sku) != 6:
            self.sku = f"FIX_{self.sku}"
        
        if self.price <= 0:
            self.price = 0.1

        if self.qty <0:
            self.qty = 0
    

import os
base_dir = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(base_dir, "warehouse.csv")
output_file = os.path.join(base_dir, "warehouse_fixed.csv")
log_file = os.path.join(base_dir, "error_log.txt")

clean_list = []
total_items = 0
errors_fixed = 0

with open(input_file, mode="r", encoding="utf-8-sig") as file, \
     open(log_file,mode = "w",encoding="utf-8") as log:

    reader = csv.DictReader(file, delimiter=',')
    log.write ("---BUG REPORT---\n\n")
    
    for row in reader:
        try: 
            part = Product(
                name = row['NAME'],
                sku = row['SKU'],
                price =  (row['PRICE']),
                qty = (row['QTY'])
            )

            error = part.error_checker()
            total_items +=1

            if error:
                print(f"Part {part.name} with {part.sku} has error {error}")
                log.write(f"PART: {part.name} | SKU: {part.sku} | PRICE: {part.price} | ERROR: {error}\n")
                part.clean_data()
                errors_fixed +=1

            else:
                print(f"Part {part.name} with SKU {part.sku} is OK.")
                

            clean_list.append({
                    'NAME': part.name,
                    'SKU': part.sku,
                    'PRICE': part.price,
                    'QTY': part.qty
                })

            

        except KeyError as e:
            print(f"The column {e} has an error!")
            break

            

with open (output_file,mode="w",encoding="utf-8-sig",newline='') as file:
    fields = ['NAME','SKU','PRICE','QTY']
    writer = csv.DictWriter(file,fieldnames=fields)

    writer.writeheader()
    writer.writerows(clean_list)

print(f"Total number of items: {total_items}")
print(f"Total number of fixed errors: {errors_fixed}")   

