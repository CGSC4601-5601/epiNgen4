# interacting with the environment using a coffee machine

# this model uses the CMC architecture
# the motor module carries out motor commands from the motor_buffer in working memory
# the visual module scans the environment and updates the visual_representation_buffer in working memory

# this model also includes independent delays that come from actions in the environment
# in this case it's a coffee machine
# but it could be a computer running a cognitive experiment
# or a detailed simualtiion of a car, plane, etc.

from computational_architecture.production_cycle import ProductionCycle

from modules.visual_productions import VisualProductions
from modules.motor_productions import MotorProductions

from environment_actors.coffee_machine import CoffeeMachineProductions

# -------------------------
# Initialize Memories
# -------------------------
working_memory = {
    'focusbuffer': {'state': 'bread1'},
    'motor_buffer': {'state': 'no_action'},  # Initially, no motor action is scheduled.
    'visual_representation_buffer': {
        'bread1': {'location': 'counter'},
        'cheese': {'location': 'counter'},
        'ham': {'location': 'counter'},
        'bread2': {'location': 'counter'},
        'coffee_cup': {'status': 'empty'}},
   'visual_command_buffer': {'state': 'scan'}  # Command to continuously scan the environment.
}
environment = {
    'bread1': {'location': 'counter'},
    'cheese': {'location': 'counter'},
    'ham': {'location': 'counter'},
    'bread2': {'location': 'counter'},
    'coffee_cup': {'status': 'empty'},
    'coffee_switch': {'position': 'up'}
}

coffee_memory = {
    'state': {'status': 'off'}} # a coffee machine keeps track of its state

memories = {
    'working_memory': working_memory,
    'environment': environment,
    'coffee_memory': coffee_memory,
}

# -------------------------
# Define Procedural Productions (Sandwich Steps)
# These productions match on the visual_representation_buffer directly.
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
    print("bread1 production executed: focus updated to 'cheese'; motor action scheduled for bread1.")

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
    print("cheese production executed: focus updated to 'ham'; motor action scheduled for cheese.")

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
    print("ham production executed: focus updated to 'bread2'; motor action scheduled for ham.")

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
    print("bread2 production executed: focus updated to 'done'; motor action scheduled for bread2.")

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
# -------------------------

def announce_sandwich(memories):
    print("Ham and cheese sandwich is ready!")
    memories['working_memory']['focusbuffer']['state'] = 'finished'
    print('getting coffee')
    motorbuffer = memories['working_memory']['motor_buffer']
    motorbuffer.update({
        'state': 'do_action',
        'env_object': 'coffee_switch',
        'slot': 'position',
        'newslotvalue': 'down',
        'delay': 3})

ProceduralProductions.append({
    'matches': {
        'working_memory': {'focusbuffer': {'state': 'done'}}
    },
    'negations': {},
    'utility': 10,
    'action': announce_sandwich,
    'report': "announce_sandwich",
})
# -------------------------



# -------------------------
# Define Motor Productions (Generic Motor)
# -------------------------


# -------------------------
# Define coffee machine Productions (productions that run in the coffee machine)
# -------------------------


# CoffeeMachiineProductions = []
#
# def coffee(memories):
#     memories['coffee_memory']['state']['status'] = 'working'
#     print('coffee machine started !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
#     return 4 #set action completion for X cycles later
# def coffee_poured(memories):
#     memories['environment']['coffee_cup']['status'] = 'full'
#     print('coffee cup is full according to the coffee machine')
# CoffeeMachiineProductions.append({
#     'matches': {'environment': {'coffee_switch': {'position': 'down'}},
#                 'coffee_memory': {'state': {'status': 'off'}}},
#     'negations': {},
#     'utility': 10,
#     'action': coffee,
#     'delayed_action': coffee_poured,
#     'report': "coffee",
# })




# -------------------------
# Production Systems Setup
# -------------------------
ProductionSystem1_Countdown = 1  # For procedural productions.
ProductionSystem2_Countdown = 1  # For motor productions.
ProductionSystem3_Countdown = 1  # For visual productions (vision system).
ProductionSystem4_Countdown = 1  # For coffee machine.

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
    'ProductionSystem4': [CoffeeMachineProductions, ProductionSystem4_Countdown]

}


# -------------------------
# Initialize and Run the Production Cycle
# -------------------------
ps = ProductionCycle()
ps.run_cycles(memories, AllProductionSystems, DelayResetValues, cycles=30, millisecpercycle=50)