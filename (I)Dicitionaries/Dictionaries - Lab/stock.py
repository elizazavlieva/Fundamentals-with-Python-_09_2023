
def dictionary(item_list):
    keys = [item_list[item] for item in range(len(item_list)) if item % 2 == 0]
    values = [int(item_list[item]) for item in range(len(item_list)) if item % 2 != 0]
    product_dict = dict(zip(keys, values))
    return product_dict


def solution(list_items, searched_items):
    product = dictionary(list_items)
    for item in searched_items:
        if item in product.keys():
            print(f'We have {product.get(item)} of {item} left')
        else:
            print(f'Sorry, we don\'t have {item}')


user_input = input().split()
items = input().split()

solution(user_input, items)
