from stellar_sdk import Keypair, Network, Server, TransactionBuilder, Asset

server = Server("https://horizon-testnet.stellar.org")

source_secret = "your source secret"
source_keypair = Keypair.from_secret(source_secret)
channel_secret = "your channel account secret" #the account you want to pay the fees with
channel_keypair = Keypair.from_secret(channel_secret)
account = server.load_account(account_id=channel_keypair.public_key)

transaction = (
    TransactionBuilder(
        source_account = account,
        network_passphrase = Network.TESTNET_NETWORK_PASSPHRASE,
        base_fee = 100
    )
    .add_text_memo("Channel transaction")
    .append_payment_op(
    destination = channel_keypair.public_key, #we are sending a payment to the same account that pays the fees
    asset_code = "XLM",
    amount = "1",
    source = source_keypair.public_key
    )
    .set_timeout(30)
    .build()
)

#we need to sign with both accounts
transaction.sign(source_keypair)
transaction.sign(channel_keypair)

response = server.submit_transaction(transaction)
