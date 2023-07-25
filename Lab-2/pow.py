"""
Proof-of-Work Blockchain Mining

This Python script demonstrates a simple implementation
of a proof-of-work (PoW) based blockchain mining process.

Author: Kai Lei, Yanming Shao
"""

import time
import threading
from queue import Queue
from block import Block, Blockchain


class ProofOfWork:
    def __init__(self, blockchain):
        """
        Constructor for ProofOfWork class.

        Args:
            blockchain (Blockchain): The blockchain instance to perform Proof of Work on.
        """
        self.blockchain = blockchain
        self.difficulty = 3  # The number of leading zeros required for a valid PoW

    def mineBlock(self, data):
        """
        Mine a new block using Proof of Work.

        Args:
            data (str): The data to be stored in the new block.

        Returns:
            Block: The newly mined block.
        """
        nonce = 0
        while True:
            with blockchain.lock:
                pass
                # TODO: Implementation of PoW algorithm

    def isValidProof(self, hash):
        """
        Check if a proof (hash) meets the required difficulty level.

        Args:
            hash (str): The hash to be checked.

        Returns:
            bool: True if the proof is valid, False otherwise.
        """
        return hash[:self.difficulty] == "0" * self.difficulty


def mineBlocksThread(blockchain, queue, threadNum):
    """
    Function to be executed by each mining thread.

    Args:
        blockchain (Blockchain): The blockchain instance to mine blocks on.
        queue (Queue): The shared queue containing data to be mined into blocks.
        threadNum (int): The thread number.

    """
    pow = ProofOfWork(blockchain)
    while True:
        with dataQueueLock:
            data = queue.get()
        if data is None:  # Stop thread if there is no more data in the queue
            break
        block = pow.mineBlock(data)
        if block is not None:
            with blockchain.lock:
                blockchain.addBlock(block)
                print(f"Thread {threadNum} mined a block.")
                print(f"Data: {data}")
                print(f"Nonce: {block.nonce}")
                print(f"Current Hash: {block.hash}\n")


if __name__ == "__main__":
    blockchain = Blockchain()

    dataList = [
        "Transaction 1",
        "Transaction 2",
        "Transaction 3",
        "Transaction 4",
        "Transaction 5"
    ]

    # Create a shared queue and put data into it
    dataQueue = Queue()
    dataQueueLock = threading.Lock()
    for data in dataList:
        dataQueue.put(data)

    # Create threads for mining blocks
    numThreads = 3
    for i in range(numThreads):
        with dataQueueLock:
            dataQueue.put(None)
    threads = []
    for i in range(numThreads):
        thread = threading.Thread(target=mineBlocksThread, args=(blockchain, dataQueue, i + 1))
        threads.append(thread)
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    # Verify the integrity of the blockchain
    print("*********  VERIFYING THE INTEGRITY OF THE BLOCKCHAIN  *********\n")
    if blockchain.isChainValid():
        print("Blockchain is valid.")
    else:
        print("Blockchain is NOT valid.")
