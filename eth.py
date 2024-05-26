from eth_account import Account
from web3 import Web3
import requests

# Generate a random Ethereum account
account = Account.create()

# Retrieve the private key and address
private_key = account.key.hex()
address = account.address

print(f"Ethereum Address: {address}")
print(f"Private Key: {private_key}")

# Connect to a public RPC endpoint
public_rpc_url = "https://cloudflare-eth.com"
web3 = Web3(Web3.HTTPProvider(public_rpc_url))

# Check if connected
if web3.is_connected():
    print("Successfully connected to the Ethereum blockchain")
else:
    print("Connection to the Ethereum blockchain failed")

# Function to check Ethereum address activity
def check_ethereum_activity(address):
    balance = web3.eth.get_balance(address)
    transaction_count = web3.eth.get_transaction_count(address)
    
    print(f"Ethereum Balance: {web3.from_wei(balance, 'ether')} Ether")
    print(f"Ethereum Transaction Count: {transaction_count}")

    if balance > 0 or transaction_count > 0:
        return True
    else:
        return False

# Check the activity of the generated Ethereum address
eth_activity = check_ethereum_activity(address)
if eth_activity:
    print("The Ethereum address has activity on the blockchain.")
else:
    print("The Ethereum address does not have any activity on the blockchain.")

# Optional: Check for ERC-20 token balances using Etherscan API or similar
def check_token_balances(address):
    etherscan_api_key = 'YOUR_ETHERSCAN_API_KEY'
    url = f"https://api.etherscan.io/api?module=account&action=tokenbalance&contractaddress=TOKEN_CONTRACT_ADDRESS&address={address}&tag=latest&apikey={etherscan_api_key}"
    
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data['status'] == '1':
            balance = int(data['result'])
            print(f"Token Balance: {balance}")
        else:
            print("Failed to retrieve token balance:", data['message'])
    else:
        print(f"Failed to retrieve token balance. Status code: {response.status_code}")

# Example: Check for a specific ERC-20 token balance
# Replace 'TOKEN_CONTRACT_ADDRESS' with the actual contract address of the token you want to check
# check_token_balances(address)
