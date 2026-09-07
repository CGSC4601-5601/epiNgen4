import random


def spreading_activation_boost(memories, memory_store, source_chunk, boost_factor=1):
    """
    Boost the utility of chunks in memory based on partial matching with a source chunk.
    The matching score is determined by counting shared values between the source chunk and each chunk in memory.

    Args:
        memories (dict): The memory system containing the memory store.
        memory_store (str): The name of the memory store to search (e.g., 'declarative_memory').
        source_chunk (dict): The source chunk for spreading activation.
        boost_factor (float): The multiplier applied to the matching score for utility boost.

    Returns:
        None
    """
    if memory_store not in memories:
        print(f"[ERROR] Memory store '{memory_store}' not found in memories.")
        return

    memory = memories[memory_store]
    source_values = set(source_chunk.values())  # Extract values from the source chunk

    print(f" Source chunk values for spreading activation: {source_values}")

    for chunk_name, chunk_data in memory.items():
        if 'utility' not in chunk_data:
            continue
        chunk_values = set(chunk_data.values())  # Extract values from the target chunk
        match_score = len(source_values & chunk_values)  # Count intersecting values
        utility_boost = match_score * boost_factor

        # Apply the utility boost
        chunk_data['utility'] += utility_boost

        print(f" Chunk '{chunk_name}': Match score = {match_score}, Utility boost = {utility_boost}")
        print(f" Updated utility for chunk '{chunk_name}': {chunk_data['utility']}")