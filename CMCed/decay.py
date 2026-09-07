import random



def decay_all_memory_chunks(memories, memory_store, decay_amount):
    """
        Reduces the utility of every chunk in a specified memory store by a given decay amount.

        This function iterates over all chunks in the specified memory store (found within the 'memories'
        dictionary) and subtracts the 'decay_amount' from each chunk's 'utility' value. The updated utility
        is clamped at 0 to prevent negative values. For each chunk, a message is printed indicating the new
        utility value; if a chunk does not have a 'utility' field, a message is printed stating that no utility
        value was found. If the specified memory store does not exist in 'memories', an error message is displayed.

        Parameters:
            memories (dict): A dictionary containing various memory stores, each mapping chunk names to their data.
            memory_store (str): The key representing the memory store to be processed (e.g., 'declarative_memory').
            decay_amount (int or float): The numerical amount to reduce each chunk's utility by.

        Returns:
            None
        """
    if memory_store in memories:
        memory = memories[memory_store]

        # Iterate over all chunks in the specified memory store
        for chunk_name, chunk_data in memory.items():
            # Decrement the utility by the decay amount if the 'utility' field exists
            if 'utility' in chunk_data:
                current_utility = chunk_data.get('utility', 0)
                new_utility = max(0, current_utility - decay_amount)  # Ensure utility doesn't go below zero
                memories[memory_store][chunk_name]['utility'] = new_utility
                #print(f"Decayed utility of {chunk_name} in {memory_store} to {new_utility}")
            else:
                #print(f"Chunk {chunk_name} in {memory_store} has no utility value.")
                pass
    else:
        #print(f"Memory store {memory_store} not found in memories.")
        pass
