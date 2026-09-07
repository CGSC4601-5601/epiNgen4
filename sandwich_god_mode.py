# interacting with the environment for quick models

# this model uses a method that is sometimes called 'god' mode
    # where the procedural production system knows and does everything
# for motor actions it uses 'delayed_actions'
    # this sets a seperate function to make a change in the environment
    # after a certain number of cycles
    # representing the delay for the action to be done
# for vision the productions are assumed to have perfect and instant access to the environment
    # this is done by treating the environement as both an environment and a memory

# this can be used to make quick models
# and can also be used as a first step in building a detailed cognitive model


from CMCed.production_cycle import ProductionCycle

working_memory = {'focusbuffer': {'state': 'bread1'}}
environment = {'bread1': {'location': 'counter'},
                'cheese': {'location': 'counter'},
                'ham': {'location': 'counter'},
                'bread2': {'location': 'counter'}}

memories = {
    'working_memory': working_memory,
    'environment': environment   # NOTE environment added here
}

ProceduralProductions = []

def bread1(memories):
    memories['working_memory']['focusbuffer']['state'] = 'cheese'
    print(f"bread1. Updated working_memory: {memories['working_memory']}")
    return 4 #set action completion for X cycles later
def bread1_method(memories):
    memories['environment']['bread1']['location'] = 'plate'
    print(f"{memories['environment']}")
ProceduralProductions.append({
    'matches': {'working_memory': {'focusbuffer': {'state': 'bread1'}},
                'environment': {'bread1': {'location': 'counter'}}},
    'negations': {},
    'utility': 10,
    'action': bread1,
    'delayed_action': bread1_method,
    'report': "bread1",
})

def cheese(memories):
    memories['working_memory']['focusbuffer']['state'] = 'ham'
    print(f"cheese executed. Updated working_memory: {memories['working_memory']}")
    print(f"{memories['environment']}")
    return 4 #set action completion for X cycles later
def cheese_method(memories):
    memories['environment']['cheese']['location'] = 'plate'
    print(f"{memories['environment']}")
ProceduralProductions.append({
    'matches': {'working_memory': {'focusbuffer': {'state': 'cheese'}},
                'environment': {'bread1': {'location': 'plate'}}},
    'negations': {},
    'utility': 10,
    'action': cheese,
    'delayed_action': cheese_method,
    'report': "cheese",
})

def ham(memories):
    memories['working_memory']['focusbuffer']['state'] = 'bread2'
    print(f"ham executed. Updated working_memory: {memories['working_memory']}")
    print(f"{memories['environment']}")
    print(f"ham executed. Updated working_memory: {memories['working_memory']}")
    return 4 #set action completion for X cycles later
def ham_method(memories):
    memories['environment']['ham']['location'] = 'plate'
    print(f"{memories['environment']}")
ProceduralProductions.append({
    'matches': {'working_memory': {'focusbuffer': {'state': 'ham'}},
                'environment': {'cheese': {'location': 'plate'}, 'ham': {'location': 'counter'}}
                },
    'negations': {},
    'utility': 10,
    'action': ham,
    'delayed_action': ham_method,
    'report': "ham",
})

def bread2(memories):
    memories['working_memory']['focusbuffer']['state'] = 'done'
    print(f"bread top executed. Updated working_memory: {memories['working_memory']}")
    print(f"{memories['environment']}")
    return 4 #set action completion for X cycles later
def bread2_method(memories):
    memories['environment']['bread2']['location'] = 'plate'
    print(f"{memories['environment']}")
ProceduralProductions.append({
    'matches': {'working_memory': {'focusbuffer': {'state': 'bread2'}},
                'environment': {'ham': {'location': 'plate'}, 'bread2': {'location': 'counter'}}
                },
    'negations': {},
    'utility': 10,
    'action': bread2,
    'delayed_action': bread2_method,
    'report': "bread2",
})

# Production system delays in ticks
ProductionSystem1_Countdown = 1

# Stores the number of cycles for a production system to fire and reset
DelayResetValues = {
    'ProductionSystem1': ProductionSystem1_Countdown}

# Dictionary of all production systems and delays
AllProductionSystems = {
    'ProductionSystem1': [ProceduralProductions, ProductionSystem1_Countdown]}

# Initialize ProductionCycle
ps = ProductionCycle()

# Run the cycle with custom parameters
ps.run_cycles(memories, AllProductionSystems, DelayResetValues, cycles=20, millisecpercycle=50)
