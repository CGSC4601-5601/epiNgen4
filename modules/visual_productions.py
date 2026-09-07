# visual_productions.py
import copy

# -------------------------
# Define Visual Productions (Vision)
# -------------------------
VisualProductions = []

def scan_environment(memories):
    # Snapshot the environment into the visual representation buffer
    memories['working_memory']['visual_representation_buffer'] = copy.deepcopy(memories['environment'])
    print("visual module ^^^^^^^^^^^^^^^^^^^ scan_environment production executed: visual_representation_buffer updated.")
    return 2  # Delay in cycles

VisualProductions.append({
    'matches': {'working_memory': {'visual_command_buffer': {'state': 'scan'}}},
    'negations': {},
    'utility': 10,
    'action': scan_environment,
    'report': "scan_environment",
})

# Optional “contract” / assumptions
REQUIRES = {
    "working_memory_buffers": ["visual_command_buffer", "visual_representation_buffer"],
    "memories_keys": ["environment", "working_memory"],
}