def shift_lags(memories):
    """
    Shift register for middle memory:

    lag1 -> lag2
    current focusbuffer -> lag1
    lag2 is overwritten (old value discarded)
    """

    middle = memories['middle_memory']
    focus = memories['working_memory']['focusbuffer']
# shift
    middle['lag2'] = middle['lag1'].copy()
    middle['lag1'] = middle['lag0'].copy()
    middle['lag0'] = focus.copy()

    # # Shift lag1 into lag2
    # middle['lag2'] = middle['lag1'].copy()
    #
    # # Copy current focus buffer into lag1
    # middle['lag1'] = focus.copy()