amazon_cart = [
    'notebooks',
    'sunglasses',
    'toys',
    'grapes'
]

amazon_cart[0] = 'laptop'
# create a partial copy of the list
# new_cart = amazon_cart[0:3]
# create a full copy of the list
# new_cart = amazon_cart[:]
# create a reference to the original list
new_cart = amazon_cart
new_cart[0] = 'gum'
print(amazon_cart)
print(new_cart)
