import account_merge


merged_account =input("What's the secret seed of the account you want to merge?: ")  #Account that gets deleted. Every lumens or asset get transferred to destination
destination = input("What's the destination public key? (account that survives!): ")

account_merge.account_merge(merged_account,destination)
