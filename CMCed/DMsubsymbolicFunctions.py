from CMCed.chunk_noise import add_noise_to_utility
from CMCed.retrieve import retrieve_memory_chunk
from CMCed.debugging import report_memory_contents
from CMCed.decay import decay_all_memory_chunks
from CMCed.chunk_utility import utility_change
from CMCed.spreading_activation import spreading_activation_boost
from CMCed.retrieve_partial import retrieve_memory_chunk_partial


# Define a memory store for sandwich working_memory with initial utilities
working_memory = {
    'focus_buffer': {'name': 'fries', 'taste': 'salty'},
    'fries': {'name': 'fries', 'taste': 'salty','utility': 10},
    'salad': {'name': 'salad', 'taste': 'fresh','utility': 5},
    'chips': {'name': 'chips', 'taste': 'crispy','utility': 7}
}

# Wrap the working_memory in a dictionary as decay_all_memory_chunks expects a collection of stores
memories = {'working_memory_dictionary': working_memory}

# Add noise to each chunk's utility to simulate variability
print("\nAdding noise to utilities...")
add_noise_to_utility(working_memory, scalar=2.0)

# Provide a detailed report of memory contents after noise addition
print("\nDetailed Memory Report after Noise Addition:")
report_memory_contents(working_memory)

# Apply decay to all memory chunks in the 'working_memory_dictionary' (simulate decay over time)
print("\nApplying decay to all memory chunks...")
decay_all_memory_chunks(memories, 'working_memory_dictionary', decay_amount=3)

# Display memory contents after decay to see the updated utilities
print("\nDetailed Memory Report after Decay:")
report_memory_contents(working_memory)

# Raise the utility of a specific chunk (e.g., 'salad') after noise and decay
print("\nRaising the utility of 'salad' by 5...")
utility_change(memories, 'working_memory_dictionary', 'salad', amount=5)

# Display memory contents after the utility change to see the updated utilities
print("\nDetailed Memory Report after Utility Change:")
report_memory_contents(working_memory)

# apply spreading activation from the focus buffer
spreading_activation_boost(memories, 'working_memory_dictionary', memories['working_memory_dictionary']['focus_buffer'], boost_factor=1)
# Display memory contents after the spreading activation change to see the updated utilities
print("\nDetailed Memory Report after spreading activation Change:")
report_memory_contents(working_memory)

# Retrieve the sandwich side with the highest (noisy, decayed, and adjusted) utility
print("\nSelected sandwich side (after noise, decay, utility change, and spreading activation boost - perfect match):")
matches = {"name": "salad", "taste": "crispy"}
selected_side = retrieve_memory_chunk(working_memory, matches)
print(selected_side)

print("\nSelected sandwich side (after noise, decay, utility change, and spreading activation boost - partial match):")
matches = {"name": "salad", "taste": "crispy"}
selected_side = retrieve_memory_chunk_partial(working_memory, matches)
print(selected_side)