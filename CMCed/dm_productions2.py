# dm_productions.py
# allows dm to retrieve
# and adds noise - set in chunk_noise.py
# and a threshold - set in retrieve.py

from CMCed.retrieve import retrieve_memory_chunk
from CMCed.chunk_noise import add_noise_to_utility

# -------------------------
# Define DM Productions (memory)
# -------------------------


DMProductions = []

def adjust_DM(memories):
    print("adjust_DM: add noise")
    add_noise_to_utility(memories['declarative_memory'], scalar=1.0)
DMProductions.append({
    'matches': {'working_memory': {'DM_command_buffer': {'state': 'normal'}}},
    'negations': {},
    'utility': 10,
    'action': adjust_DM,
    'report': "adjust_DM",
                })


def retrieve_DM(memories):
    # Retrieve retrieval_conditions from DM_retieval_buffer
    retrieval_conditions = memories['working_memory']['DM_retieval_buffer']
    matches = retrieval_conditions.get('matches', {})
    negations = retrieval_conditions.get('negations', {})
    # Retrieve from declarative memory
    retrieved_chunk = retrieve_memory_chunk(
        memories['declarative_memory'],
        matches,
        negations
    )
    print(f"DM module recalls ------------------------- {retrieved_chunk}")
    # Reset DM_command_buffer
    DM_command_buffer = memories['working_memory']['DM_command_buffer']
    DM_command_buffer.update({'state': 'normal'})
    # Put retrieved chunk in DM_output_buffer
    DM_output_buffer = memories['working_memory']['DM_output_buffer']
    DM_output_buffer.update(retrieved_chunk)
    # Create awareness of retrieval
    focusbuffer = memories['working_memory']['focusbuffer']
    focusbuffer.update({'state': 'memory_retrieved'})
DMProductions.append({
    'matches': {'working_memory': {'DM_command_buffer': {'state': 'retrieve'}}},
    'negations': {},
    'utility': 10,
    'action': retrieve_DM,
    'report': "retrieve_DM",
})



# Optional contract for printing / later validation
REQUIRES = {
    "working_memory_buffers": [
        "DM_retieval_buffer",
        "DM_command_buffer",
        "DM_output_buffer",
        "focusbuffer",
    ],
    "memories_keys": ["declarative_memory", "working_memory"],
}