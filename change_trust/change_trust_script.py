import change_trust

source = input("Insert the source secret: ") #the account that wants to receive the asset
asset_issuer = input("Insert the issuer public key: ")
asset_code = input("Insert the asset code: ") #your asset code

change_trust.change_trust(asset_issuer, asset_code,source,"100") #100 is a test limit
