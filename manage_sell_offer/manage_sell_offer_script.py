import manage_sell_offer

source = "your source secret seed" #the account that wants to add a sell offer
asset_issuer = "asset issuer public key"
selling_code = "testXLM" #asset you are selling
amount = "1" #amount you want to sell
price = "2" #price per selling_code asset, in this case 1 testXLM sells for 2 XLM

manage_sell_offer.manage_sell_offer(source, selling_code, asset_issuer, amount, price, 1000)

print("Added sell offer: " + "selling " + amount + " " + selling_code
    +  "\nfor " + price + " XLM each")
