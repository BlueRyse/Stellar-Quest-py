import change_trust

source = "source secret seed" #the account that wants to receive the asset
asset_issuer = "issuer public key"
asset_code="testXLM" #your asset code

change_trust.change_trust(asset_issuer, asset_code,source,"100") #100 is a test limit
