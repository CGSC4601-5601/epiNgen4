import random

import random

def add_noise_to_utility(memory, scalar=1.0):
    """
    Adds noise to the utility values of each chunk in a specified memory.
    Noise is drawn from a normal distribution (mean=0, std=1) and scaled by the given scalar.

    Args:
        memory (dict): The memory to add noise to (e.g., declarative or environment memory).
        scalar (float): The factor to scale the noise, default is 1.0.

    Returns:
        None
    """
    #print("\n--- Adding Noise to Memory ---")

    for chunk_name, chunk_data in memory.items():
        if 'utility' in chunk_data:
            # Generate noise from a normal distribution and scale it
            noise = random.gauss(0, 1) * scalar
            old_utility = chunk_data['utility']
            new_utility = max(0, old_utility + noise)  # Ensure utility doesn't go below 0
            chunk_data['utility'] = new_utility
            #print(f"Chunk '{chunk_name}': Old Utility = {old_utility}, Noise = {noise:.2f}, New Utility = {new_utility:.2f}")
        else:
            #print(f"Chunk '{chunk_name}' has no utility to add noise to.")
            pass

    #print("--- End of Noise Addition ---\n")
    pass

