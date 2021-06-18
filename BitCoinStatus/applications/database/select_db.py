from ...models import BitCoinData


def pprint(product_data):
    print('=' * 40)

    print(f"product_code        {product_data['product_code']}")
    print(f"price               {product_data['price']}")
    print(f"created_time        {product_data['created_time']}")

    print('=' * 40 + '\n')


def select_data():
    selected_data = BitCoinData.objects.all().values().filter(product_code='BTC_JPY').values('product_code', 'price', 'created_time')

    # for i in selected_data:
    #     print(i)
    #     pprint(i)
