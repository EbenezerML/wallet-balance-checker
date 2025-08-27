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
