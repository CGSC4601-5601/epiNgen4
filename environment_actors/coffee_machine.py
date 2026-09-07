CoffeeMachineProductions = []

def coffee(memories):
    memories['coffee_memory']['state']['status'] = 'working'
    print('coffee machine started !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
    return 4 #set action completion for X cycles later
def coffee_poured(memories):
    memories['environment']['coffee_cup']['status'] = 'full'
    print('coffee cup is full according to the coffee machine!!!!!!!!!!!!!!!!!!!!!!!!')
CoffeeMachineProductions.append({
    'matches': {'environment': {'coffee_switch': {'position': 'down'}},
                'coffee_memory': {'state': {'status': 'off'}}},
    'negations': {},
    'utility': 10,
    'action': coffee,
    'delayed_action': coffee_poured,
    'report': "coffee",
})