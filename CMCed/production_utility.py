import random


def adjust_production_utility(production_systems, system_name, production_name, change, max_utility=None):
    """
    Adjusts the utility of a specific production in a production system.

    Args:
        production_systems (dict): Dictionary of production systems.
        system_name (str): The name of the production system containing the production.
        production_name (str): The name of the production to adjust.
        change (int): The amount to adjust the utility by (can be positive or negative).
        max_utility (int, optional): Maximum allowable utility value. If None, no cap is applied.

    Returns:
        None
    """
    if system_name in production_systems:
        for production in production_systems[system_name]:
            if production['name'] == production_name:
                # Adjust the utility
                production['utility'] += change

                # Ensure utility doesn't fall below 0
                if production['utility'] < 0:
                    production['utility'] = 0

                # Apply max utility cap if specified
                if max_utility is not None and production['utility'] > max_utility:
                    production['utility'] = max_utility

                print(f"Updated utility for production '{production_name}': {production['utility']}")
                return
    else:
        print(f"Production system '{system_name}' not found.")
