

from CMCed.production_cycle import ProductionCycle
from CMCed.retrieve import retrieve_memory_chunk


working_memory = {'focusbuffer': {'state': 'bread1'},
                  'declarative_buffer': {'state': 'no_action'}}

declarative_memory = {'fries': {'name': 'fries',
                                'condition': 'good',
                                'side_order': 'yes',
                                'utility':2},
                      'house_salad': {'name': 'house_salad',
                                      'condition': 'good',
                                      'side_order': 'no',
                                      'utility':1},
                      'poutine': {'name': 'poutine',
                                  'condition': 'good',
                                  'side_order': 'yes',
                                  'utility':5},
                      'ceasar_salad': {'name': 'ceasar_salad',
                                       'condition': 'bad',
                                       'side_order': 'no',
                                       'utility':10},
                      }

memories = {
    'working_memory': working_memory,
    'declarative_memory': declarative_memory
}

ProceduralProductions = []

def bread1(memories):
    memories['working_memory']['focusbuffer']['state'] = 'cheese'
    print(f"bread bottom executed. Updated working_memory: {memories['working_memory']}")
ProceduralProductions.append({
    'matches': {'working_memory': {'focusbuffer': {'state': 'bread1'}}},
    'negations': {},
    'utility': 10,
    'action': bread1,
    'report': "bread1",
})

def cheese(memories):
    memories['working_memory']['focusbuffer']['state'] = 'ham'
    print(f"cheese executed. Updated working_memory: {memories['working_memory']}")
ProceduralProductions.append({
    'matches': {'working_memory': {'focusbuffer': {'state': 'cheese'}}},
    'negations': {},
    'utility': 10,
    'action': cheese,
    'report': "cheese",
})

def ham(memories):
    memories['working_memory']['focusbuffer']['state'] = 'bread2'
    print(f"ham executed. Updated working_memory: {memories['working_memory']}")
ProceduralProductions.append({
    'matches': {'working_memory': {'focusbuffer': {'state': 'ham'}}},
    'negations': {},
    'utility': 10,
    'action': ham,
    'report': "ham",
})

def bread2(memories):
    memories['working_memory']['focusbuffer']['state'] = 'done'
    print(f"bread top executed. Updated working_memory: {memories['working_memory']}")
ProceduralProductions.append({
    'matches': {'working_memory': {'focusbuffer': {'state': 'bread2'}}},
    'negations': {},
    'utility': 10,
    'action': bread2,
    'report': "bread2",
})

def announce_sandwich(memories):
    print("Ham and cheese sandwich is ready!")
# retrieval conditions
    memory = declarative_memory
    matches = {'side_order': 'yes','condition': 'good'}
    negations = {'condition': 'bad'}
    utility_threshold = 0
# retrieve the best match
    retrieved_chunk = retrieve_memory_chunk(memory, matches, negations, utility_threshold)
    print('I recall the side order was......................')
    print(retrieved_chunk['name'])

ProceduralProductions.append({
    'matches': {'working_memory': {'focusbuffer': {'state': 'done'}}},
    'negations': {},
    'utility': 10,
    'action': announce_sandwich,
    'report': "announce_sandwich",
})


# Production system delays in ticks
ProductionSystem1_Countdown = 3

# Stores the number of cycles for a production system to fire and reset
DelayResetValues = {
    'ProductionSystem1': ProductionSystem1_Countdown}

# Dictionary of all production systems and delays
AllProductionSystems = {
    'ProductionSystem1': [ProceduralProductions, ProductionSystem1_Countdown]}

# Initialize ProductionCycle
ps = ProductionCycle()

# Run the cycle with custom parameters
ps.run_cycles(memories, AllProductionSystems, DelayResetValues, cycles=17, millisecpercycle=100)

