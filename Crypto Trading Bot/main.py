from typing import Sized
import API_KEY
import cbpro

public=API_KEY.PUBLIC
passphrase=API_KEY.PASSPHRASE
secret=API_KEY.SECRET


auth_client=cbpro.AuthenticatedClient(public,secret,passphrase)

# print(auth_client.get_accounts())

# auth_client.buy(price="10.0",size="0.1",order_type="limit",product_id="ETH-EUR")
# print(auth_client.buy(size="10",order_type="market",product_id="ETH-EUR"))

# print(auth_client.sell(price="20000000000.0",size="10",order_type="limit",product_id="BTC-EUR"))


# auth_client.sell(size="10",order_type="market",product_id="BTC-EUR")


# auth_client.place_limit_order(product_id="BTC-EUR",side="buy",price="100.0",size=2)

# auth_client.cancel_all(product_id="BTC-EUR")

# auth_client.get_orders()


import time

sell_price=30000
sell_amount=0.3

buy_price=250000
buy_amount=0.2



while True:
    price=float(auth_client.get_product_ticker(product_id="BTC-EUR")["price"])
    if price <= buy_price:
        price("Buying BTC")
        auth_client.buy(size=buy_amount,order_type="market",product_id="BTC-EUR")
    elif price >= sell_price:
        print("selling BTC")
        auth_client.sell(size=sell_amount,order_type="market",product_id="BTC-EUR")
    else:
        print("Nothing..")
    time.sleep(100)