price = int(input("What's the price? "))
discount_percent = int(input("What's the discount percent? "))  
def calculate_discount(price,discount_percent):
  if discount_percent >= 20:
    price = ((100-discount_percent)/100)*price
    print(price)
  else:
    print (f"The price of your item is {price}")
    
calculate_discount(price,discount_percent)