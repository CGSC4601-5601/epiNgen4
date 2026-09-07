import random

def retrieve_memory_chunk(buffer, matches, negations={}, utility_threshold=1):
    """
    Retrieve the highest utility chunk that meets match criteria and negation constraints,
    excluding the 'utility' slot from both matching and the final returned result.
    Note - buffer refers to the memory being searched

    Args:
        buffer (dict): Memory buffer containing chunks.
        matches (dict): Key-value pairs to match in each chunk. '*' indicates any value is acceptable if the slot exists.
        negations (dict): Key-value pairs to avoid in each chunk. '*' indicates any value in the slot will negate the match.
        utility_threshold (int, optional): Minimum utility required to consider a chunk.

    Returns:
        dict: The chunk with the highest utility (excluding 'utility') or a placeholder if no matches.
    """
    matched_chunks = []

    # Iterate through each chunk in the buffer to check for matches
    for chunk in buffer.values():
        # Exclude 'utility' slot from the chunk for matching purposes
        filtered_chunk = {k: v for k, v in chunk.items() if k != 'utility'}
        match = True

        # Check positive matches
        for key, value in matches.items():
            if key not in filtered_chunk:  # Slot must exist for wildcard match
                match = False
                break
            elif value != '*' and filtered_chunk[key] != value:  # Specific value required, no wildcard
                match = False
                break

        # Check negations
        for key, value in negations.items():
            if key in filtered_chunk:  # Slot must exist for wildcard negation
                if value == '*' or filtered_chunk[key] == value:  # Any value in this slot negates the match
                    match = False
                    break

        # Add chunk if it matches and meets the utility threshold
        if match and chunk.get('utility', 0) >= utility_threshold:
            matched_chunks.append(chunk)

    # Return placeholder if no chunks matched
    if not matched_chunks:
        return {"name": "no_match"}

    # Find the highest-utility chunk among matches
    max_utility = max(chunk.get('utility', 0) for chunk in matched_chunks)
    best_chunks = [chunk for chunk in matched_chunks if chunk.get('utility', 0) == max_utility]

    # Randomly select one chunk if multiple have the same max utility
    selected_chunk = random.choice(best_chunks)

    # Remove the 'utility' slot from the returned chunk
    result_chunk = {k: v for k, v in selected_chunk.items() if k != 'utility'}

    return result_chunk



