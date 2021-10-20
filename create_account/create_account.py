from stellar_sdk import Keypair, Network, Server, TransactionBuilder

#This class allows to create an account on testnet or mainnet, used on create_account_script.py and create_random_account_script.py

class create_account:

    def __init__(self, source_secr_seed, new_acc_public_key, balance, fee = 100):
        self.fee = fee
        self.server = Server("https://horizon-testnet.stellar.org")
        self.source = Keypair.from_secret(source_secr_seed)
        self.source_account = self.server.load_account(account_id=self.source.public_key)
        self.new_account = Keypair.from_public_key(new_acc_public_key)
        self.balance = balance
        self.__create_transaction()

    def __create_transaction(self):
        self.transaction = (
            TransactionBuilder(
                source_account = self.source_account,
                network_passphrase = Network.TESTNET_NETWORK_PASSPHRASE,
                base_fee = self.fee
            )
            .append_create_account_op(
                destination=self.new_account.public_key, starting_balance = self.balance
            )
            .build()
        )
        self.__execute_transaction()

    def __execute_transaction(self):
        self.transaction.sign(self.source)
        self.response = self.server.submit_transaction(self.transaction)
