from solders.pubkey import Pubkey
from web3 import Web3
from solana.rpc.api import Client
from dotenv import load_dotenv
import os
import re
from tenacity import retry, stop_after_attempt, wait_fixed

# ---------------- Load Environment Variables ----------------
load_dotenv()

eth_rpc_url = os.getenv("ETH_RPC_URL")
sol_rpc_url = os.getenv("SOL_RPC_URL", "https://api.mainnet-beta.solana.com")

if not eth_rpc_url:
    raise ValueError("❌ ETH_RPC_URL not set in .env file")


# ---------------- Helper Functions ----------------
def is_valid_solana_address(address: str) -> bool:
    """Validate Solana address format (base58, 32-44 characters)."""
    try:
        Pubkey.from_string(address)
        return len(address) >= 32 and len(address) <= 44 and re.match(r"^[1-9A-HJ-NP-Za-km-z]+$", address)
    except Exception:
        return False


@retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
def get_eth_balance(wallet: str) -> float:
    """Fetch Ethereum balance with retry logic."""
    web3 = Web3(Web3.HTTPProvider(eth_rpc_url))
    if not web3.is_connected():
        raise ConnectionError("❌ Failed to connect to Ethereum network")

    if not web3.is_address(wallet):
        raise ValueError("❌ Invalid Ethereum wallet address")

    balance_wei = web3.eth.get_balance(wallet)
    return web3.from_wei(balance_wei, "ether")


@retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
def get_sol_balance(wallet: str) -> float:
    """Fetch Solana balance with retry logic."""
    sol_client = Client(sol_rpc_url)
    try:
        sol_wallet_pubkey = Pubkey.from_string(wallet)
    except Exception:
        raise ValueError("❌ Invalid Solana wallet address")

    response = sol_client.get_balance(sol_wallet_pubkey)
    if not hasattr(response, "value") or response.value is None:
        raise ValueError("❌ Failed to fetch Solana balance or invalid API response")

    return response.value / 1_000_000_000


# ---------------- User Choice ----------------
def get_user_choice() -> str:
    """Prompt user to choose between Ethereum and Solana."""
    while True:
        print("Which blockchain would you like to check?")
        print("1. Ethereum (ETH)")
        print("2. Solana (SOL)")
        choice = input("Enter 1 or 2: ").strip()
        if choice in ["1", "2"]:
            return choice
        print("❌ Invalid choice. Please enter 1 for Ethereum or 2 for Solana.")


# ---------------- Main Logic ----------------
try:
    choice = get_user_choice()

    if choice == "1":
        # Ethereum
        print("\n✅ Connecting to Ethereum network...")
        eth_wallet = os.getenv("ETH_WALLET") or input("Enter Ethereum wallet address: ")
        eth_balance = get_eth_balance(eth_wallet)
        print(f"💰 ETH Wallet: {eth_wallet}")
        print(f"🔹 Balance: {eth_balance:.4f} ETH")

    elif choice == "2":
        # Solana
        print("\n✅ Connecting to Solana network...")
        sol_wallet = os.getenv("SOL_WALLET") or input("Enter Solana wallet address: ")
        if not is_valid_solana_address(sol_wallet):
            raise ValueError("❌ Invalid Solana wallet address format")
        sol_balance = get_sol_balance(sol_wallet)
        print(f"💰 SOL Wallet: {sol_wallet}")
        print(f"🔹 Balance: {sol_balance:.4f} SOL")

except Exception as e:
    print(f"❌ Error: {str(e)}")