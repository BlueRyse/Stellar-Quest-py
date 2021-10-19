from stellar_sdk import Keypair, Network, Server, TransactionBuilder

class payment:
    def __init__(self, server, source_secr_seed, new_acc_public_key, amount, asset):
        self.asset = asset
        self.mbase_fee = 100
        self.server = server
        self.source = Keypair.from_secret(source_secr_seed)
        self.source_account = server.load_account(account_id=self.source.public_key)
        self.dest_account = Keypair.from_public_key(new_acc_public_key)
        self.amount = amount
        self.create_transaction()

    def create_transaction(self):
        self.transaction = (
            TransactionBuilder(
                source_account = self.source_account,
                network_passphrase = Network.TESTNET_NETWORK_PASSPHRASE,
                base_fee = self.mbase_fee
            )
         .add_text_memo("Test_transaction")
         .append_payment_op(
            destination = self.dest_account.public_key,
            asset_code = self.asset,
            amount = self.amount
        )
         .set_timeout(30)  # Make this transaction valid for the next 30 seconds only
         .build()
        )
        self.execute_transaction()

    def execute_transaction(self):
        if self.transaction is None:
            raise ValueError("Create transaction first")
        self.transaction.sign(self.source)
        self.response = self.server.submit_transaction(self.transaction)
