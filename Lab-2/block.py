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
        self.nonce = 0
        self.timestamp = time.time()
        self.data = data
        self.previousHash = previous_hash
        self.hash = self.calculateHash()

    def calculateHash(self):
        """
        Calculate the SHA-256 hash of the block.

        Returns:
            str: The SHA-256 hash of the block.
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
        Constructor for the Blockchain class.
        Initializes the blockchain with a genesis block.
        """
        self.chain = [Block("Genesis Block", "0")]

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
        newBlock.index = self.getLatestBlock().index + 1
        newBlock.previousHash = self.getLatestBlock().hash
        newBlock.hash = newBlock.calculateHash()
        self.chain.append(newBlock)

    def isChainValid(self):
        """
        Validate the integrity of the blockchain.

        Returns:
            bool: True if the blockchain is valid, False otherwise.
        """
        for i in range(1, len(self.chain)):
            currentBlock = self.chain[i]
            previousBlock = self.chain[i - 1]
            if currentBlock.hash != currentBlock.calculateHash():
                print(f"Block {currentBlock.index} hash is invalid.")
                print(f"Current Hash: {currentBlock.hash}")
                print(f"Calculated Hash: {currentBlock.calculateHash()}\n")
                return False
            if currentBlock.previousHash != previousBlock.hash:
                print(f"Block {currentBlock.index} previous_hash is invalid.")
                print(f"Current Previous Hash: {currentBlock.previousHash}")
                print(f"Previous Block Hash: {previousBlock.hash}\n")
                return False
        return True
