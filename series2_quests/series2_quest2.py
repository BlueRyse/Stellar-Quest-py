from stellar_sdk import Keypair, Network, Server, TransactionBuilder

server = Server("https://horizon-testnet.stellar.org")
asset_iss = 'your asset issuer secret seed'
asset_cd = 'ser2Quest2' #asset code can be whatever
source_secret = 'your source account secret seed'
lim = '100'

source_keypair = Keypair.from_secret(source_secret)
asset_issuer_keypair = Keypair.from_secret(asset_iss)
source_acc = server.load_account(account_id = source_keypair.public_key)

transaction = (
    TransactionBuilder(
        source_account = source_acc,
        network_passphrase = Network.TESTNET_NETWORK_PASSPHRASE,
        base_fee = 100
    )
    .add_text_memo("Series 2 quest 2")
    .append_change_trust_op(
        asset_issuer = asset_issuer_keypair.public_key,
        asset_code = asset_cd,
        limit = lim
    )
    .append_payment_op(
        destination = source_keypair.public_key,
        asset_code = asset_cd,
        asset_issuer = asset_issuer_keypair.public_key,
        amount = "1",
        source = asset_issuer_keypair.public_key
    )
    .set_timeout(30)
    .build()
)

transaction.sign(source_keypair)
transaction.sign(asset_issuer_keypair)

response = server.submit_transaction(transaction)
