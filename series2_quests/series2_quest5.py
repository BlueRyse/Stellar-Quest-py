from stellar_sdk import Keypair, Network, Server, TransactionBuilder

server = Server("https://horizon-testnet.stellar.org")

source_secr = 'your source secret'
source_keypair = Keypair.from_secret(source_secr)
source_acc = server.load_account(source_keypair.public_key)

try:
    balances = (
        server
        .claimable_balances()
        .for_claimant(source_keypair.public_key)
        .limit(1)
        .order(desc = True)
        .call()
    )

except (BadRequestError, BadResponseError) as err:
    print(f"Claimable balance retrieval failed: {err}")

balanceId = balances["_embedded"]["records"][0]["id"]

transaction = (
    TransactionBuilder(
        source_account = source_acc,
        network_passphrase = Network.TESTNET_NETWORK_PASSPHRASE,
        base_fee = 100
    )
    .add_text_memo("Create Claimable balance")
    .append_claim_claimable_balance_op(
        balance_id = balanceId
    )
    .set_timeout(30)
    .build()
)

transaction.sign(source_keypair)
response = server.submit_transaction(transaction)
