import random


def utility_change(memories, memory_store, chunk_name, amount, max_utility=None):
    """
    Adjusts the utility of a specific chunk by a given amount. This function is used to
    directly modify the utility value associated with a chunk stored within a designated memory store.

    The function performs the following steps:
      1. Retrieves the target chunk from the specified memory store using its name.
      2. Increments (or decrements) the chunk's utility by the given 'amount'.
      3. Ensures that the resulting utility does not fall below 0.
      4. If a 'max_utility' is provided, caps the utility so that it does not exceed this maximum value.
      5. Prints a confirmation message showing the updated utility.

    Parameters:
        memories (dict): A dictionary of memory stores (e.g., 'declarative_memory') containing chunks.
        memory_store (str): The key for the memory store in which the target chunk resides.
        chunk_name (str): The unique identifier for the chunk whose utility will be updated.
        amount (int or float): The numerical value by which to adjust the utility (positive to increase,
                               negative to decrease).
        max_utility (int or float, optional): An optional cap for the utility value. If specified and the
                                              new utility exceeds this value, it will be set to max_utility.

    Returns:
        None
    """
    chunk = memories[memory_store][chunk_name]

    # Adjust the utility
    chunk['utility'] += amount

    # Ensure utility doesn't drop below 0
    if chunk['utility'] < 0:
        chunk['utility'] = 0

    # If a max_utility is specified, ensure utility doesn't exceed it
    if max_utility is not None and chunk['utility'] > max_utility:
        chunk['utility'] = max_utility

    print(f"Updated utility for {chunk_name}: {chunk['utility']}")


def utility_change_by_description(memories, memory_store, chunk_description, amount, max_utility=None):
    """
    Adjusts the utility of a specific chunk by finding a match based on a provided description.
    This function searches the specified memory store for chunks whose non-utility attributes match
    the given description (partial matching is allowed, that is, matching on a subset of slot values), updates the utility of the matching chunk by a given amount, and ensures
    that the updated utility remains within acceptable bounds.

    The function performs the following steps:
      1. Iterates over all chunks in the specified memory store and filters out the 'utility' attribute
         for matching purposes.
      2. Checks if each chunk matches the provided description based on its non-utility attributes.
      3. If more than one chunk matches the description, prints an error message and aborts the update.
      4. If no matching chunk is found, prints a message and aborts the update.
      5. If exactly one matching chunk is found, adjusts its utility by the specified amount.
      6. Ensures that the updated utility does not fall below 0.
      7. Optionally caps the updated utility to a specified maximum value if provided.
      8. Prints a confirmation message showing the updated utility value for the chunk.

    Parameters:
        memories (dict): A dictionary containing various memory stores.
        memory_store (str): The key indicating which memory store to search within.
        chunk_description (dict): A dictionary of key-value pairs describing the chunk (excluding 'utility')
                                  to be updated.
        amount (int or float): The value by which to adjust the utility (can be positive or negative).
        max_utility (int or float, optional): An optional maximum cap for the utility value.

    Returns:
        None
    """

    matches = []  # Keep track of matching chunks

    # Find all matching chunks, ignoring the 'utility' slot
    for chunk_name, chunk_data in memories[memory_store].items():
        filtered_chunk_data = {k: v for k, v in chunk_data.items() if k != 'utility'}
        if all(filtered_chunk_data.get(key) == value for key, value in chunk_description.items()):
            matches.append((chunk_name, chunk_data))

    # Check for duplicates
    if len(matches) > 1:
        print("Error: Multiple chunks match the given BOOST description. No changes were applied.")
        for chunk_name, _ in matches:
            print(f"Matching chunk: {chunk_name}")
        return

    if not matches:
        print("No matching chunk found for utility boost.")
        return

    # Update the utility of the single matching chunk
    chunk_name, chunk_data = matches[0]
    chunk_data['utility'] += amount

    # Ensure utility doesn't drop below 0
    if chunk_data['utility'] < 0:
        chunk_data['utility'] = 0

    # If a max_utility is specified, ensure utility doesn't exceed it
    if max_utility is not None and chunk_data['utility'] > max_utility:
        chunk_data['utility'] = max_utility

    print(f"Updated utility for memory key '{chunk_name}': {chunk_data['utility']}")
