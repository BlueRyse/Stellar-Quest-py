from stellar_sdk import Keypair, Network, Server, TransactionBuilder

class manage_data:

    def __init__(self, source_secr_seed, data_name, data_value, fee = 100):
        self.data_name = data_name
        self.data_value = data_value
        self.fee = fee
        self.server = Server("https://horizon-testnet.stellar.org")
        self.source = Keypair.from_secret(source_secr_seed)
        self.source_account = self.server.load_account(account_id=self.source.public_key)
        self.__create_transaction()

    def __create_transaction(self):
        self.transaction = (
            TransactionBuilder(
                source_account = self.source_account,
                network_passphrase = Network.TESTNET_NETWORK_PASSPHRASE,
                base_fee = self.fee
            )
            .append_manage_data_op(
                data_name=self.data_name, data_value = self.data_value
            )
            .build()
        )
        self.__execute_transaction()

    def __execute_transaction(self):
        self.transaction.sign(self.source)
        self.response = self.server.submit_transaction(self.transaction)
