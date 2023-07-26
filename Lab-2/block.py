"""
Blockchain Implementation

This is a Python implementation of a simple blockchain with
the ability to add new blocks and validate the integrity of
the chain.

Author: Kai Lei, Yanming Shao
"""

import hashlib
import time
import threading


class Block:
    def __init__(self, data, previous_hash):
        """
        Constructor for Block class.

        Args:
            data (str): The data to be stored in the block.
            previous_hash (str): The hash of the previous block in the blockchain.
        """
        self.index = 0
        self.nonce = 0
        self.timestamp = time.time()
        self.data = data
        self.previousHash = previous_hash
        self.hash = self.calculateHash()

    def calculateHash(self):
        """
        Calculate the SHA-256 hash of the block.

        Returns:
            str: The hexadecimal representation of the calculated hash.
        """
        sha = hashlib.sha256()
        sha.update(
            str(self.index).encode('utf-8') +
            str(self.timestamp).encode('utf-8') +
            str(self.data).encode('utf-8') +
            str(self.previousHash).encode('utf-8') +
            str(self.nonce).encode('utf-8')
        )
        return sha.hexdigest()


class Blockchain:
    def __init__(self):
        """
        Constructor for Blockchain class.

        Initializes the blockchain with a genesis block.
        """
        self.chain = [Block("Genesis Block", "0")]
        self.lock = threading.Lock()  # Lock for accessing the blockchain

    def getLatestBlock(self):
        """
        Get the latest block in the blockchain.

        Returns:
            Block: The latest block in the blockchain.
        """
        return self.chain[-1]

    def addBlock(self, newBlock):
        """
        Add a new block to the blockchain.

        Args:
            newBlock (Block): The new block to be added to the blockchain.
        """
        self.chain.append(newBlock)

    def isChainValid(self):
        """
        Validate the integrity of the blockchain.

        Returns:
            bool: True if the blockchain is valid, False otherwise.
        """
        # TODO: Your code here
