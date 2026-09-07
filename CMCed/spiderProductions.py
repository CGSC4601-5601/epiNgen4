#required to start - {'environment': {'spider': {'visible': 'no'}}}

import random

def do_nothing(memories):
    print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&')
    return 0

spider_productions = []


def spider_visibility(memories):
    #Updates whether the spider is visible or not.
    r = random.random()
    visibility_probability = 0.5
    if r < visibility_probability:
        memories['environment']['spider']['visible'] = 'yes'
        print('spider is visible!!!!!!!!!')
    else:
        memories['environment']['spider']['visible'] = 'no'
        print('spider is not visible ***************')

spider_productions.append({
    'matches': {'environment': {'spider': {'visible': '*'}}},
    'negations': {},
    'utility': 10,
    'action': spider_visibility,
    'report': "spider",
})


