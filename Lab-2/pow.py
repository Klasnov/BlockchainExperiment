"""
Proof-of-Work (PoW) Implementation

This is a Python implementation of a simple Proof-of-Work (PoW)
consensus algorithm for educational purposes. PoW is the mechanism
used in blockchain networks to secure and validate new blocks
added to the blockchain. It requires miners to find a hash
that meets a specific difficulty requirement, which is typically
a certain number of leading zeros in the hash.

This implementation demonstrates how miners can continuously search
for a valid block by adjusting the nonce value until a hash with the
required number of leading zeros is found. The mined block is then
added to the blockchain as a new block.

Author: Kai Lei, Yanming Shao
"""

import hashlib
import time
import threading
from block import Block, Blockchain


class ProofOfWork:
    def __init__(self, blockchain):
        self.blockchain = blockchain
        self.difficulty = 4  # The number of leading zeros required for a valid PoW
        self.mining_reward = 1  # Reward for mining a new block

    def mineBlock(self, data):
        """
        Mine a new block.

        Args:
            data (str): The data to be stored in the block.

        Returns:
            Block: The mined block.
        """
        index = len(self.blockchain.chain)
        previousHash = self.blockchain.getLatestBlock().hash
        timestamp = time.time()
        nonce = 0

        while True:
            block = Block(data, previousHash)
            block.index = index
            block.timestamp = timestamp
            block.nonce = nonce
            block.hash = block.calculateHash()

            if self.isValidProof(block.hash):
                return block

            nonce += 1

    def isValidProof(self, hash):
        """
        Check if the given hash meets the PoW requirement.

        Args:
            hash (str): The hash to be checked.

        Returns:
            bool: True if the hash meets the requirement, False otherwise.
        """
        return hash[:self.difficulty] == "0" * self.difficulty


def mineBlocksThread(blockchain, pow, data, threadNum):
    block = pow.mineBlock(data)
    blockchain.addBlock(block)
    print(f"Thread {threadNum} mined a block.")
    print(f"Data: {data}")
    print(f"Nonce: {block.nonce}")
    print(f"Current Hash: {block.hash}\n")


if __name__ == "__main__":
    blockchain = Blockchain()
    pow = ProofOfWork(blockchain)

    # List of data for new blocks to be mined
    dataList = [
        "Transaction 1",
        "Transaction 2",
        "Transaction 3",
        "Transaction 4",
        "Transaction 5"
    ]

    # Create threads for mining blocks
    threads = []
    for i, data in enumerate(dataList):
        thread = threading.Thread(target=mineBlocksThread, args=(blockchain, pow, data, i + 1))
        threads.append(thread)
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    # Verify the integrity of the blockchain
    if blockchain.isChainValid():
        print("Blockchain is valid.")
    else:
        print("Blockchain is NOT valid.")
