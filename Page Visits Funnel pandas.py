import codecademylib3
import pandas as pd

visits = pd.read_csv('visits.csv',
                     parse_dates=[1])
cart = pd.read_csv('cart.csv',
                   parse_dates=[1])
checkout = pd.read_csv('checkout.csv',
                       parse_dates=[1])
purchase = pd.read_csv('purchase.csv',
                       parse_dates=[1])
# we are analize all the files, looking  using .head) to the firts 10 and see what they have 
print(visits.head(10))
print(cart.head(10))   
print(checkout.head(10))   
print(purchase.head(10))     
# we merge visits files with cart left: use only keys from left frame, similar to a SQL left outer join; preserve key order.
visits_cart = visits.merge(cart, how="left")
print(visits_cart)
print("We have " + str(len(visits_cart)) + " rows.")

#were we are using len to count all the visit they have the cart null they dont put any thirt to buy
null_cart = len(visits_cart[visits_cart.cart_time.isnull()])
print("We have " + str(null_cart) + " null because they dont buy tshirt")

#now we going to do the percentages we have with null cart
null_cart_percent =float(null_cart)  / float(len(visits_cart.cart_time))
print("We have " + str(null_cart_percent) + "% of people dont put nothing at the cart")

# now we going to merge tabler cart with the checkout and next count the null similar process that before
cart_checkout = cart.merge(checkout, how="left")
print(cart_checkout)
#were a create a var to save the quantity of client that put t-shirts at the cart 
client_cart = len(cart)
print("We have " + str(client_cart) +" clients that put t-shirt in the cart")

#see how many null we have in checkout_time and next we do the percentes
null_checkout = len(cart_checkout[cart_checkout.checkout_time.isnull()])
null_checkout_percent =float(null_checkout)  / float(client_cart)
print("We have " + str(null_checkout_percent) + "% of people  did not proceed to checkout")

# merge all the data we have in only one var, a analize how is the finnaly table
all_data = visits.merge(cart_checkout, how ='left').merge(purchase, how ='left')
print(all_data.head(10))
#see how many null we have in checkout_time and next we do the percentes
#quantity of client that checkout
client_check_notNull = len(all_data[~all_data.checkout_time.isnull()])
#quantity of client that put the t shirt in cart but dont buy 
null_purchase = len(all_data[all_data.purchase_time.isnull()])
#now we need to see how many dont buy
dont_buy = len(all_data[(all_data.purchase_time.isnull()) & (~all_data.checkout_time.isnull())])

#percentages of client that put the t-shirt in cart but dont buy 
null_purchase_percentages = float(dont_buy)  / float(client_check_notNull)
print("We have " + str(null_purchase_percentages) + "% of people proceed to checkout but dont buy")

#now we use round and we do the convert to percent unit 
cart_time_per = round(null_cart_percent*100, 2)
print(str(cart_time_per) + '% dont put any t-shirt in cart')

checkout_time_per = round(null_checkout_percent*100, 2)
print(str(checkout_time_per) + '% dont checkout any t-shirt, they put in the cart')

purchase_time_per = round(null_purchase_percentages*100, 2)
print(str(purchase_time_per) + '% dont buy the t-shirt they checkout early')

#creat a new column and that calculate the difference between purchase_time and visit_time.

all_data['difference_purchase_visit'] = all_data.purchase_time - all_data.visit_time	
print(all_data.head(10))
#calculate the avg time from the last column 
avg_time_buy = all_data.difference_purchase_visit.mean()
print(avg_time_buy)








