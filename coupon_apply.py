import unittest
coupon = { 'category': 'fruit',
   'percent_discount': 15,
   'amount_discount': None,
   'minimum_num_items_required': 2,
   'minimum_amount_required': 10.00
  }

item_list =  [ {'price': 2.00, 'category': 'fruit'},
   {'price': 20.00, 'category': 'toy'},
   {'price': 5.00, 'category': 'clothing'},
   {'price': 8.00, 'category': 'fruit'}
 ]

coupon_list = [ 
  { 'categories': ['clothing', 'toy'],
    'percent_discount': 10,
    'amount_discount': None,
    'minimum_num_items_required': None,
    'minimum_amount_required': None
  },
  { 'categories': ['fruit'],
    'percent_discount': 15,
    'amount_discount': None,
    'minimum_num_items_required': 2,
    'minimum_amount_required': 10.00
   }
]

def validate_coupon(coupon):
    if coupon['percent_discount'] is None and coupon['amount_discount'] is None:
        raise ValueError('Coupon must have a discount applied to it')
    elif coupon['percent_discount'] is not None and coupon['amount_discount'] is not None:
        raise ValueError('Coupon must have only one type of discount')

def consolidate_item_list(items):
    res = {}
    for item in items:
        cat, price = item['category'], item['price']
        if cat not in res:
            res[cat] = (price, 1)
        else:
            
            curr_price, curr_items = res[cat]
            res[cat] = (curr_price + price, curr_items + 1)
    return res

def get_coupon_list_price(items, coupons):
    item_list = consolidate_item_list(items)
    return apply_coupon_list(item_list, coupons)

# applys coupon which can have multiple categories
def apply_coupon_list(item_list, coupons):
    for coupon in coupons:
        categories = coupon['categories']
        if len(categories) > 1:
            discount_dict = {}
            # try applying the discount in that category store category -> price_after_discount
            # apply discount
            
            for element in categories:
                discount_dict[element] = item_list[element][0] - apply_coupon_discount(coupon, item_list[element])
            most_price_off = max(discount_dict, key=discount_dict.get)
            item_list[most_price_off] = item_list[most_price_off][0] - discount_dict[most_price_off], item_list[element][1]
        else:
            category = coupon['categories'][0]
            item_list[category] = (apply_coupon_discount(coupon, item_list[category]), item_list[element][1])
    total_price = 0
    for price, count in item_list.values():
        total_price += price
    return total_price



# applys a coupon with one category to the items
def apply_single_coupon(items, coupon, category):
    try:
        validate_coupon(coupon)
    except ValueError as ve:
        print(ve)
        return
    
    item_list = consolidate_item_list(items)
    coupon_price = apply_coupon_discount(coupon, item_list[category])
    total_price = 0
    for item in item_list:
        if item != category:   
            total_price += item_list[item][0]
    return coupon_price + total_price

# applys the actual discount based on coupon values
def apply_coupon_discount(coupon, item, p_discount=None, amt_discount=None, min_items=None, min_price=None):
    min_items = coupon['minimum_num_items_required']
    min_price = coupon['minimum_amount_required']
    p_discount = coupon['percent_discount']
    amt_discount = coupon['amount_discount']

    item_price, item_cnt = item[0], item[1]
    # not met the requirements
    if not min_items and not min_price:
        pass
    elif not min_items and item_price < min_price:
        return item_price
    elif item_cnt < min_items:
        return item_price

    
    # if only amt discount apply that 
    if not p_discount:   
        item_price -= amt_discount
    else: 
        item_price *= ((100 - p_discount) / 100)
    if item_price < 0:
        return 0
    return item_price

class CouponUnitTest(unittest.TestCase):
    def setUp(self):
        self.coupon = coupon
        self.coupon_list = coupon_list
        self.items = item_list

    def test_single_coupon(self):
        price = apply_single_coupon(self.items, self.coupon, self.coupon['category'])
        self.assertEqual(price, 33.5)

print(get_coupon_list_price(item_list, coupon_list))