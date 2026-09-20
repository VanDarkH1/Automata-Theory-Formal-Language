
def run_custom_minimized_dfa(input_string):
    # 1. Define the transition table for the minimized DFA
    transitions = {
        "A":  {"0": "B",  "1": "A"},
        "B":  {"0": "CD", "1": "A"},
        "CD": {"0": "CD", "1": "A"}
    }
    
    # 2. Define the starting state and the set of accepting states
    current_state = "A"
    accept_states = {"CD"}
    
    # 3. Process the input string
    for char in input_string:
        if char not in ["0", "1"]:
            return False, "Error: Invalid character. Only 0 and 1 are allowed."
        
        current_state = transitions[current_state][char]
        
    # 4. Check if the final state is an accept state
    is_accepted = current_state in accept_states
    return is_accepted, current_state

# --- INTERACTIVE LOOP ---

print("Custom DFA Tester (Accepts strings ending in '00')")
print("Type 'quit' or 'exit' to stop.")

while True:
    user_input = input("\nEnter a binary string: ").strip()
    
    if user_input.lower() in ['quit', 'exit']:
        print("Exiting DFA Tester.")
        break
        
    if not user_input:
        print("Input cannot be empty. Try again.")
        continue
        
    accepted, final_state = run_custom_minimized_dfa(user_input)
    
    if final_state.startswith("Error"):
        print(final_state)
    else:
        status = "Accepted" if accepted else "Rejected"
        print(f"Result: {status} (Ended in state {final_state})")