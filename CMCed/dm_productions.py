# dm_productions.py
# allows dm to retrieve a matching chunk

from CMCed.retrieve import retrieve_memory_chunk

# -------------------------
# Define DM Productions
# -------------------------


DMProductions = []

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