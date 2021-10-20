import add_signer
from stellar_sdk import Signer

source_account = "your source secret seed"

signer_pb = input("Insert the new signer public key: ") #you need to know the secret seed of this account,
signer = Signer.ed25519_public_key(signer_pb, 1)        #if you want to use it to sign
add_signer.add_signer(source_account, signer)
