
# -------------------------
# Define Amygdala Productions (Vision)
# -------------------------
AmygdalaProductions = []

def fear_spider(memories):
    memories['working_memory']['emotional_buffer']['emotion_state'] = '01001010' # neural state for fear
    print('amygdala is detecting a fearful situation !!!!!!!!!!!!!!!!!!!!!!!!')
AmygdalaProductions.append({
    'matches': {'working_memory': {'visual_representation_buffer': {'spider': {'visible':'yes'}}}},
    'negations': {},
    'utility': 10,
    'action': fear_spider,
    'report': "fear_spider",
})

def spider_calm_down(memories):
    memories['working_memory']['emotional_buffer']['emotion_state'] = '00000000' # neural state for fear
    print('amygdala is detecting relatively calm situation &&&&&&&&&&&&&&&&&&&&&&&&&&&')
AmygdalaProductions.append({
    'matches': {'working_memory': {'visual_representation_buffer': {'spider': {'visible':'no'}}}},
    'negations': {},
    'utility': 10,
    'action': spider_calm_down,
    'report': "spider_calm_down",
})

# Optional “contract” / assumptions
REQUIRES = {
    "working_memory_buffers": ["visual_command_buffer", "visual_representation_buffer"],
    "memories_keys": ["environment", "working_memory"],
}