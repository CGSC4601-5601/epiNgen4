
from cognitive_functions.retrieve import retrieve_memory_chunk
from cognitive_functions.retrieve_partial import retrieve_memory_chunk_partial


DM_Symbolic_Productions = []


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
    DM_command_buffer.update({'state': 'normal'}) # reset
    # Put retrieved chunk in DM_output_buffer
    DM_output_buffer = memories['working_memory']['DM_output_buffer']
    DM_output_buffer.update(retrieved_chunk)
    # Create awareness of retrieval
    focusbuffer = memories['working_memory']['focusbuffer']
    focusbuffer.update({'state': 'memory_retrieved'})
DM_Symbolic_Productions.append({
    'matches': {'working_memory': {'DM_command_buffer': {'state': 'retrieve'}}},
    'negations': {},
    'utility': 10,
    'action': retrieve_DM,
    'report': "retrieve_DM",
})

def retrieve_partial_DM(memories):
    # Retrieve retrieval_conditions from DM_retieval_buffer
    retrieval_conditions = memories['working_memory']['DM_retieval_buffer']
    matches = retrieval_conditions.get('matches', {})
    negations = retrieval_conditions.get('negations', {})
    # Retrieve from declarative memory
    retrieved_chunk = retrieve_memory_chunk_partial(
        memories['declarative_memory'],
        matches,
        negations
    )
    print(f"DM module recalls ------------------------- {retrieved_chunk}")
    # Reset DM_command_buffer
    DM_command_buffer = memories['working_memory']['DM_command_buffer']
    DM_command_buffer.update({'state': 'normal'}) # reset
    # Put retrieved chunk in DM_output_buffer
    DM_output_buffer = memories['working_memory']['DM_output_buffer']
    DM_output_buffer.update(retrieved_chunk)
    # Create awareness of retrieval
    focusbuffer = memories['working_memory']['focusbuffer']
    focusbuffer.update({'state': 'memory_retrieved'})
DM_Symbolic_Productions.append({
    'matches': {'working_memory': {'DM_command_buffer': {'state': 'retrieve_partial'}}},
    'negations': {},
    'utility': 10,
    'action': retrieve_DM,
    'report': "retrieve_DM",
})
