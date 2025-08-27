# 🪙 Wallet Balance Checker (ETH + SOL)

## Overview
A simple Python script that allows users to check the balance of any wallet on the **Ethereum** or **Solana** blockchain.  
Users can choose between Ethereum and Solana at runtime and input a wallet address to retrieve the balance in **ETH** or **SOL**.

---

## ✨ Features
- Connects to **Ethereum** via Web3.py for real-time balance checks.
- Connects to **Solana** via the Solana JSON-RPC API.
- Validates wallet addresses for both blockchains.
- Supports configuration via environment variables (`.env`).
- Includes retry logic for robust API connections.
- User-friendly prompts and error handling.

---

## 📦 Prerequisites
- Python **3.8+**
- Git (for cloning and version control)
- A valid **Ethereum RPC URL** (e.g., from Infura, Alchemy, or a personal node)
- (Optional) Ethereum and Solana wallet addresses (can also be input manually)

---

## ⚙️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/EbenezerML/wallet-balance-checker.git
   cd wallet-balance-checker

2. **install the required Python packages:**
   ```bash 
   pip install solders web3 solana python-dotenv tenacity


3. **Create a .env file in the project directory with the following:**

  - ETH_RPC_URL=https://your-ethereum-rpc-url
  - SOL_RPC_URL=https://api.mainnet-beta.solana.com
  - ETH_WALLET=your-ethereum-wallet-address   # Optional
  - SOL_WALLET=your-solana-wallet-address     # Optional

 
## ▶️ Usage

1. **Run the script:**
   ```bash
   python check_balance.py

2. **Choose a blockchain:**
    ```bash
    Which blockchain would you like to check?
    1. Ethereum (ETH)
    2. Solana (SOL)
    Enter 1 or 2:

3. **Provide a wallet address:**

- If you did not set a wallet address in the `.env` file, the script will prompt you to enter one at runtime.

- **Ethereum Example:**  
  `0x1234567890abcdef1234567890abcdef12345678`

- **Solana Example:**  
  `7C4jsPZpht42Tw6MjXWF56Q5RFGtTNGJ5f2qWsKnDuPw`


4. **View the balance:**

✅ Connecting to Ethereum network...
💰 ETH Wallet: 0x1234567890abcdef1234567890abcdef12345678
🔹 Balance: 1.2345 ETH

✅ Connecting to Solana network...
💰 SOL Wallet: 7C4jsPZpht42Tw6MjXWF56Q5RFGtTNGJ5f2qWsKnDuPw
🔹 Balance: 10.5678 SOL

5. **📚 Dependencies**

- solders → For Solana public key handling

- web3 → For Ethereum blockchain interactions

- solana → For Solana blockchain API calls

- python-dotenv → For loading environment variables

- tenacity → For retrying failed API requests

6. **🔒 Security Notes**

-  Never store private keys in the .env file or the repository.

-  This script only uses public wallet addresses.

-  .env is excluded from version control via .gitignore to protect sensitive information.

7. **🤝 Contributing**

- Fork the repository.

- Create a new branch:

- git checkout -b feature-branch


- Make your changes and commit:
   ```bash
   git commit -m "Add new feature"


- Push to your branch:
   ```bash
  git push origin feature-branch


- Open a Pull Request on GitHub.

8. **📄 License**

- This project is licensed under the MIT License.

