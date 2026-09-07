
import random



def retrieve_memory_chunk_partial(buffer, matches, negations={}, utility_threshold=0):
    """
    Retrieve a memory chunk using partial matching.
    Instead of only considering perfect matches, this function evaluates every chunk and scores it based on how many
    slot values match the provided 'matches' dictionary. Negative matches and wildcard '*' behave as in the original function.

    Args:
        buffer (dict): Memory buffer containing chunks.
        matches (dict): Key-value pairs for positive matching. '*' indicates any value is acceptable if the slot exists.
        negations (dict): Key-value pairs to avoid in each chunk. '*' indicates any value in the slot will negate the match.
        utility_threshold (int, optional): Minimum utility required to consider a chunk.

    Returns:
        dict: The chunk with the highest partial match score (excluding 'utility') or a placeholder if no chunk matches.
    """
    import random
    candidates = []  # List to store tuples of (chunk, score)

    # Iterate through each chunk in the buffer
    for chunk in buffer.values():
        # Exclude the 'utility' slot from the chunk for matching purposes
        filtered_chunk = {k: v for k, v in chunk.items() if k != 'utility'}

        # Check negative matches as in the original function
        negative_fail = False
        for key, value in negations.items():
            if key in filtered_chunk:
                if value == '*' or filtered_chunk[key] == value:
                    negative_fail = True
                    break
        if negative_fail:
            continue

        # Check if the chunk meets the utility threshold
        if chunk.get('utility', 0) < utility_threshold:
            continue

        # Compute a partial match score based on positive matches.
        score = 0
        for key, expected in matches.items():
            if key in filtered_chunk:
                if expected == '*' or filtered_chunk[key] == expected:
                    score += 1
        candidates.append((chunk, score))

    # If no candidates were found, return a placeholder.
    if not candidates:
        return {"name": "no_match"}

    # Print out the partial match scores for each candidate with a non-zero score.
    for candidate, score in candidates:
        if score > 0:
            print(f"Candidate: {candidate} - Score: {score}")

    # Select the candidate with the highest (score, utility)
    selected_chunk, selected_score = max(candidates, key=lambda x: (x[1], x[0].get('utility', 0)))

    # Remove the 'utility' slot from the returned chunk
    result_chunk = {k: v for k, v in selected_chunk.items() if k != 'utility'}
    return result_chunk