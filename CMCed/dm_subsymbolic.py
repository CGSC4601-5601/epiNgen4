
from CMCed.chunk_noise import add_noise_to_utility
from CMCed.decay import decay_all_memory_chunks
from CMCed.spreading_activation import spreading_activation_boost


DM_Subsymbolic_Productions = []

def adjust_DM(memories):
    print("adjust_DM: add noise, decay utility, spreading activation boost")
    add_noise_to_utility(memories['declarative_memory'], scalar=1.0)
    decay_all_memory_chunks(memories, 'working_memory', decay_amount=3)
    spreading_activation_boost(memories, 'working_memory',
                               memories['working_memory']['focusbuffer'], boost_factor=1)
DM_Subsymbolic_Productions.append({
    'matches': {'working_memory': {'DM_command_buffer': {'state': '*'}}}, # always matches state
    'negations': {},
    'utility': 10,
    'action': adjust_DM,
    'report': "adjust_DM",
                })

