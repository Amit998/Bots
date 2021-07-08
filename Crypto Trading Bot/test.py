import API_KEY
import cbpro

public_client=cbpro.PublicClient()

# result=public_client.get_currencies()

# result=public_client.get_product_ticker('BTC-USD')

# print(result)

# for row in result:
#     print(row['id'])


eth_trades=public_client.get_product_trades('ETH-USD')

print(next(eth_trades))
print(next(eth_trades))
print(next(eth_trades))
print(next(eth_trades))