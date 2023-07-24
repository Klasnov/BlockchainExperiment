"""
Blockchain Data Structure

This is a Python implementation of a basic blockchain data
structure and essential methods for educational purposes.
It provides a simple framework to help students understand
the fundamental concepts of blockchain, including blocks,
hashing, and chain validation, and allows them to experiment
with its behavior.

Author: Kai Lei, Yanming Shao
"""

import hashlib
import time


class Block:
    def __init__(self, data, previous_hash):
        """
        Constructor for the Block class.

        Args:
            data (str): The data to be stored in the block.
            previous_hash (str): The hash of the previous block in the blockchain.
        """
        self.index = 0
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        """
        Calculate the SHA-256 hash of the block.

        Returns:
            str: The SHA-256 hash of the block.
        """
        sha = hashlib.sha256()
        sha.update(str(self.index).encode('utf-8') +
                   str(self.timestamp).encode('utf-8') +
                   str(self.data).encode('utf-8') +
                   str(self.previous_hash).encode('utf-8'))
        return sha.hexdigest()


class Blockchain:
    def __init__(self):
        """
        Constructor for the Blockchain class.
        Initializes the blockchain with a genesis block.
        """
        self.chain = [Block("Genesis Block", "0")]

    def get_latest_block(self):
        """
        Get the latest block in the blockchain.

        Returns:
            Block: The latest block in the blockchain.
        """
        return self.chain[-1]

    def add_block(self, new_block):
        """
        Add a new block to the blockchain.

        Args:
            new_block (Block): The new block to be added to the blockchain.

        """
        new_block.index = self.get_latest_block().index + 1
        new_block.previous_hash = self.get_latest_block().hash
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)

    def is_chain_valid(self):
        """
        Validate the integrity of the blockchain.

        Returns:
            bool: True if the blockchain is valid, False otherwise.
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            if current_block.hash != current_block.calculate_hash():
                return False
            if current_block.previous_hash != previous_block.hash:
                return False
        return True
