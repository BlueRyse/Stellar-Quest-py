from stellar_sdk import Keypair, Network, Server, TransactionBuilder
import hashlib, base64

server = Server("https://horizon-testnet.stellar.org")

source_secr = 'your source secret'
source_keypair = Keypair.from_secret(source_secr)
source_acc = server.load_account(source_keypair.public_key)

base64_message = b'S2FuYXllTmV0' #Quest base64 clue
signer_string = base64.b64decode(base64_message).decode('utf-8')

str = signer_string.encode('utf-8')
sha256_signer = hashlib.sha256(str).hexdigest()

add_hash_signer_transaction = (
    TransactionBuilder(
        source_account = source_acc,
        network_passphrase = Network.TESTNET_NETWORK_PASSPHRASE,
        base_fee = 100
    )
    .add_text_memo("Added hash signer")
    .append_hashx_signer(
        sha256_hash = sha256_signer,
        weight = 1
    )
    .set_timeout(30)
    .build()
)

add_hash_signer_transaction.sign(source_keypair)
response = server.submit_transaction(add_hash_signer_transaction)

hex_signer = str.hex()

remove_hash_signer_transaction = (
    TransactionBuilder(
        source_account = source_acc,
        network_passphrase = Network.TESTNET_NETWORK_PASSPHRASE,
        base_fee = 100
    )
    .append_hashx_signer(
        sha256_hash = sha256_signer,
        weight = 0
    )
    .set_timeout(30)
    .build()
)

remove_hash_signer_transaction.sign_hashx(hex_signer)
response1 = server.submit_transaction(remove_hash_signer_transaction)
