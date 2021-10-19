from stellar_sdk import Keypair, Network, Server, TransactionBuilder

#This class permits to create an account on testnet or mainnet, used on create_account_script.py and create_random_account_script.py

class create_account:

    def __init__(self, server, source_secr_seed, new_acc_public_key, balance):
        self.mbase_fee = 100
        self.server = server
        self.source = Keypair.from_secret(source_secr_seed)
        self.source_account = server.load_account(account_id=self.source.public_key)
        self.new_account = Keypair.from_public_key(new_acc_public_key)
        self.balance = balance
        self.create_transaction()

    def create_transaction(self):
        self.transaction = (
            TransactionBuilder(
                source_account = self.source_account,
                network_passphrase = Network.TESTNET_NETWORK_PASSPHRASE,
                base_fee = self.mbase_fee
            )
            .append_create_account_op(
                destination=self.new_account.public_key, starting_balance = self.balance
            )
            .build()
        )
        self.execute_transaction()

    def execute_transaction(self):
        if self.transaction is None:
            raise ValueError("Create transaction first")
        self.transaction.sign(self.source)
        self.response = self.server.submit_transaction(self.transaction)
