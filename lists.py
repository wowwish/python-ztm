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

nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
print("nums1 : ", nums1)
print("nums2 : ", nums2)
print("nums1 + nums2 : ", nums1 + nums2)
