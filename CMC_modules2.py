# This model uses the threshold and noise to affect retrieval
# this is done in dm_productions2.py, retrieve.py, and chunk_noise.py


# import productions for modules
from CMCed.visual_productions import VisualProductions, REQUIRES as VISUAL_REQUIRES
print("Motor Module REQUIRES:", VISUAL_REQUIRES)

from CMCed.motor_productions import MotorProductions, REQUIRES as MOTOR_REQUIRES
print("Motor Module REQUIRES:", MOTOR_REQUIRES)

from CMCed.dm_productions2 import DMProductions, REQUIRES as DM_REQUIRES
print("DM Module REQUIRES:", DM_REQUIRES)

# import production cycle
from CMCed.production_cycle import ProductionCycle

# -------------------------
# Initialize Memories
# -------------------------
working_memory = {
    'focusbuffer': {'state': 'bread1'},
    'motor_buffer': {'state': 'no_action'},  # Initially, no motor action is scheduled.
    'visual_representation_buffer': {},
    'DM_output_buffer': {},
    'DM_retieval_buffer': {'matches': {'side_order': 'yes', 'condition': 'good'},'negations': {'condition': 'bad'}},
    'visual_command_buffer': {'state': 'scan'},  # Command to continuously scan the environment.
    'DM_command_buffer': {'state': 'normal'}  # Command to continuously adjust DM.
}


declarative_memory = {'fries': {'name': 'fries',
                                'condition': 'good',
                                'side_order': 'yes',
                                'utility':4},
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


environment = {
    'bread1': {'location': 'counter'},
    'cheese': {'location': 'counter'},
    'ham': {'location': 'counter'},
    'bread2': {'location': 'counter'}
}
memories = {
    'working_memory': working_memory,
    'declarative_memory': declarative_memory,
    'environment': environment  # Motor productions still update the actual environment.
}

# -------------------------
# Define Procedural Productions (Sandwich Steps)
# -------------------------
ProceduralProductions = []

def bread1(memories):
    # Set up motor action to move bread1 from 'counter' to 'plate'
    motorbuffer = memories['working_memory']['motor_buffer']
    motorbuffer.update({
        'state': 'do_action',
        'env_object': 'bread1',
        'slot': 'location',
        'newslotvalue': 'plate',
        'delay': 4
    })
    # Update the focus for the next production.
    memories['working_memory']['focusbuffer']['state'] = 'cheese'
    print("procedural module !!!!!!!!!!!!!!!! bread1 production executed: focus updated to 'cheese'; motor action scheduled for bread1.")

ProceduralProductions.append({
    'matches': {
        'working_memory': {
             'focusbuffer': {'state': 'bread1'},
             'visual_representation_buffer': {'bread1': {'location': 'counter'}}}},
    'negations': {},
    'utility': 10,
    'action': bread1,
    'report': "bread1",
})
# -------------------------

def cheese(memories):
    motorbuffer = memories['working_memory']['motor_buffer']
    motorbuffer.update({
        'state': 'do_action',
        'env_object': 'cheese',
        'slot': 'location',
        'newslotvalue': 'plate',
        'delay': 4
    })
    memories['working_memory']['focusbuffer']['state'] = 'ham'
    print("procedural module !!!!!!!!!!!!!!!! cheese production executed: focus updated to 'ham'; motor action scheduled for cheese.")

ProceduralProductions.append({
    'matches': {
        'working_memory':
            {'focusbuffer': {'state': 'cheese'},
            'visual_representation_buffer': {'bread1': {'location': 'plate'},
                                             'cheese': {'location': 'counter'}}}},
    'negations': {},
    'utility': 10,
    'action': cheese,
    'report': "cheese",
})
# -------------------------

def ham(memories):
    motorbuffer = memories['working_memory']['motor_buffer']
    motorbuffer.update({
        'state': 'do_action',
        'env_object': 'ham',
        'slot': 'location',
        'newslotvalue': 'plate',
        'delay': 4
    })
    memories['working_memory']['focusbuffer']['state'] = 'bread2'
    print("procedural module !!!!!!!!!!!!!!!! ham production executed: focus updated to 'bread2'; motor action scheduled for ham.")

ProceduralProductions.append({
    'matches': {
        'working_memory': {'focusbuffer': {'state': 'ham'},
        'visual_representation_buffer': {
            'cheese': {'location': 'plate'},
            'ham': {'location': 'counter'}}}},
    'negations': {},
    'utility': 10,
    'action': ham,
    'report': "ham",
})
# -------------------------

def bread2(memories):
    motorbuffer = memories['working_memory']['motor_buffer']
    motorbuffer.update({
        'state': 'do_action',
        'env_object': 'bread2',
        'slot': 'location',
        'newslotvalue': 'plate',
        'delay': 4
    })
    memories['working_memory']['focusbuffer']['state'] = 'done'
    print("procedural module !!!!!!!!!!!!!!!! bread2 production executed: focus updated to 'done'; motor action scheduled for bread2.")

ProceduralProductions.append({
    'matches': {
        'working_memory': {'focusbuffer': {'state': 'bread2'},
        'visual_representation_buffer': {
            'ham': {'location': 'plate'},
            'bread2': {'location': 'counter'}}}},
    'negations': {},
    'utility': 10,
    'action': bread2,
    'report': "bread2",
})


def announce_sandwich(memories):
    print("procedural module !!!!!!!!!!!!!!!! Ham and cheese sandwich is almost ready, just adding the bread")
    print("while I am adding the bread I will recall if there was a side order")
    memories['working_memory']['focusbuffer']['state'] = 'sandwich_done'
    # Set retrieval conditions
    memories['working_memory']['DM_retieval_buffer']['matches'] = {'side_order': 'yes', 'condition': 'good'}
    memories['working_memory']['DM_retieval_buffer']['negations'] = {'condition': 'bad'}
    # tell DM to work on the retrival
    memories['working_memory']['DM_command_buffer']['state'] = 'retrieve'
ProceduralProductions.append({
    'matches': {'working_memory': {'focusbuffer': {'state': 'done'}}},
    'negations': {},
    'utility': 10,
    'action': announce_sandwich,
    'report': "announce_sandwich",
})

def announce_side(memories):
    print("procedural module !!!!!!!!!!!!!!!! I recall the side order was")
    print(memories['working_memory']['DM_output_buffer'])
    memories['working_memory']['focusbuffer']['state'] = 'end'
ProceduralProductions.append({
    'matches': {'working_memory': {'focusbuffer': {'state': 'memory_retrieved'}}},
    'negations': {},
    'utility': 10,
    'action': announce_side,
    'report': "announce_side",
})


# -------------------------
# Production Systems Setup
# -------------------------
ProductionSystem1_Countdown = 1  # For procedural productions.
ProductionSystem2_Countdown = 1  # For motor productions.
ProductionSystem3_Countdown = 1  # For visual productions (vision system).
ProductionSystem4_Countdown = 1  # For DM productions.


DelayResetValues = {
    'ProductionSystem1': ProductionSystem1_Countdown,
    'ProductionSystem2': ProductionSystem2_Countdown,
    'ProductionSystem3': ProductionSystem3_Countdown,
    'ProductionSystem4': ProductionSystem4_Countdown

}

AllProductionSystems = {
    'ProductionSystem1': [ProceduralProductions, ProductionSystem1_Countdown],
    'ProductionSystem2': [MotorProductions, ProductionSystem2_Countdown],
    'ProductionSystem3': [VisualProductions, ProductionSystem3_Countdown],
    'ProductionSystem4': [DMProductions, ProductionSystem4_Countdown]

}


# -------------------------
# Initialize and Run the Production Cycle
# -------------------------
ps = ProductionCycle()
ps.run_cycles(memories, AllProductionSystems, DelayResetValues, cycles=24, millisecpercycle=50)