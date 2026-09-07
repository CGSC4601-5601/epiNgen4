## this file contains functions to help with debugging


def report_memory_contents(memory, matches=None, negations=None):
    """
    Reports the contents of a selected memory, including utility levels and whether a chunk matched given criteria.
    if matches and negations are not specified it defaults to None and everything is a match

    Args:
        memory (dict): The memory to report on (e.g., declarative or environment memory).
        matches (dict, optional): Criteria for matching. The chunk must contain these key-value pairs to match.
        negations (dict, optional): Criteria for negations. If a chunk contains these key-value pairs, it will not match.

    Returns:
        None
    """
    print("\n--- Memory Report ---")

    if matches:
        print(f"Match Criteria: {matches}")
    if negations:
        print(f"Negation Criteria: {negations}")

    if not memory:
        print("The memory is empty.")
        return

    for chunk_name, chunk_data in memory.items():
        print(f"Chunk '{chunk_name}':")

        # Check if the chunk matches the criteria
        match = True
        if matches:
            for key, value in matches.items():
                if key not in chunk_data or (value != '*' and chunk_data[key] != value):
                    match = False
                    break
        if match and negations:
            for neg_key, neg_value in negations.items():
                if neg_key in chunk_data and (neg_value == '*' or chunk_data[neg_key] == neg_value):
                    match = False
                    break

        # Print match status
        print("  Match status:", "MATCHED" if match else "DID NOT MATCH")

        # Print each key-value pair in the chunk, except utility (handled separately)
        for key, value in chunk_data.items():
            if key != 'utility':
                print(f"  {key}: {value}")

        # Print utility if available
        if 'utility' in chunk_data:
            print(f"  Utility: {chunk_data['utility']}")
        else:
            print("  No utility information.")

    print("--- End of Memory Report ---\n")
