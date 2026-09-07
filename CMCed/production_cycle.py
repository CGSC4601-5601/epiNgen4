from CMCed.utility import *
# nov 7

class ProductionCycle:
    def __init__(self):
        self.pending_actions = []
        self.delayed_actions = []

    def match_productions(self, memories, AllProductionSystems):
        """Finds and groups matched productions."""
        grouped_matched_productions = {key: [] for key in AllProductionSystems}

        for prod_system_key, prod_system_value in AllProductionSystems.items():
            if prod_system_value[1] > 0:
                prod_system_value[1] -= 1

            prod_system = prod_system_value[0]
            delay = prod_system_value[1]

            if delay > 0:
                continue

            for production in prod_system:
                is_match_for_all_conditions = True

                for memory_system_key, buffer_conditions in production['matches'].items():
                    for buffer_key, match_criteria in buffer_conditions.items():
                        if memory_system_key in memories and buffer_key in memories[memory_system_key]:
                            memory_content = memories[memory_system_key][buffer_key]
                            # debug
                            #extracted_negations = production['negations'].get(memory_system_key, {}).get(buffer_key, {})
                            extracted_negations = production['negations'].get(buffer_key, {})
                            #print(f"[DEBUG] Corrected extracted negations for '{buffer_key}': {extracted_negations}")
                            #print(f"[DEBUG] Extracted negations for '{memory_system_key}' and buffer '{buffer_key}': {extracted_negations}")
                            #print(f"[DEBUG] Full production structure: {production}")
                            ## debug
                            #print(f"[DEBUG] Passing extracted negations to buffer_match_eval: {extracted_negations}")
                            if not Utility.buffer_match_eval(
                                memory_content,
                                match_criteria,
                                #production['negations'].get(memory_system_key, {}).get(buffer_key, {})
                                extracted_negations
                            ):
                                is_match_for_all_conditions = False
                                break
                        else:
                            is_match_for_all_conditions = False
                            break
                    if not is_match_for_all_conditions:
                        break

                if is_match_for_all_conditions:
                    grouped_matched_productions[prod_system_key].append(production)

        return grouped_matched_productions

    def process_pending_actions(self, memories, AllProductionSystems, DelayResetValues):
        for i in range(len(self.pending_actions) - 1, -1, -1):
            prod_system_key, production, delay = self.pending_actions[i]

            if delay <= 1:
                production['action'](memories)
                #print(f'Action executed: {production.get("report")}')
                AllProductionSystems[prod_system_key][1] = DelayResetValues[prod_system_key]
                del self.pending_actions[i]
            else:
                self.pending_actions[i] = (prod_system_key, production, delay - 1)

        for i in range(len(self.delayed_actions) - 1, -1, -1):
            delayed_action, remaining_cycles = self.delayed_actions[i]

            if remaining_cycles <= 1:
                delayed_action(memories)
                #print(f'Delayed action executed after waiting: {delayed_action.__name__}')
                del self.delayed_actions[i]
            else:
                self.delayed_actions[i] = (delayed_action, remaining_cycles - 1)

    def filter_and_execute_productions(self, grouped_productions, memories, AllProductionSystems, DelayResetValues):
        for prod_system_key, productions in grouped_productions.items():
            highest_utility_production = Utility.find_max(productions)
            if highest_utility_production:
                delay = highest_utility_production['action'](memories)
                #print(f'Immediate action executed: {highest_utility_production.get("report")}')
                AllProductionSystems[prod_system_key][1] = DelayResetValues[prod_system_key]

                # Schedule delayed action
                if 'delayed_action' in highest_utility_production and delay:
                    self.delayed_actions.append(
                        (highest_utility_production['delayed_action'], delay)
                    )
                    #print(f'Delayed action scheduled: {highest_utility_production["delayed_action"].__name__} to be executed in {delay} cycles')

    def execute_actions(self, memories, matched_productions, AllProductionSystems, DelayResetValues):
        self.process_pending_actions(memories, AllProductionSystems, DelayResetValues)
        self.filter_and_execute_productions(matched_productions, memories, AllProductionSystems, DelayResetValues)

    def run_cycles(self, memories, AllProductionSystems, DelayResetValues, cycles=5, millisecpercycle=10):
        for cycle_number in range(cycles):
            print(f'\nCycle {(cycle_number + 1)}, Time: {(cycle_number + 1) * millisecpercycle} ms')
            matched_productions = self.match_productions(memories, AllProductionSystems)
            # if matched_productions:
            #     print(f'Matched productions: {matched_productions}')
            # else:
            #     print('No productions matched this cycle.')
            self.execute_actions(memories, matched_productions, AllProductionSystems, DelayResetValues)
            #for prod_system_key, prod_system_value in AllProductionSystems.items():
                #print(f'Remaining delay for {prod_system_key}: {prod_system_value[1]} cycles')
