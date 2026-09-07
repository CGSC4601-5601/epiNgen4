from cognitive_functions.shift_register import shift_lags

Trace_Productions = []

def shift(memories):
    #shift_lags(memories)
    focus = memories['working_memory']['focusbuffer']
    middle = memories['middle_memory']
    if focus != middle['lag0']:
        shift_lags(memories)
    print(
        f"[MM SHIFT] "
        f"current: {focus} | "
        f"lag0: {middle['lag0']} | "
        f"lag1: {middle['lag1']} | "
        f"lag2: {middle['lag2']}"

    )

Trace_Productions.append({
    'matches': {
        'working_memory': {
            'focusbuffer': {'state': '*'}
        }
    },
    'negations': {},
    'utility': 1,  # low priority background process
    'action': shift,
    'report': "middle memory shift",
})