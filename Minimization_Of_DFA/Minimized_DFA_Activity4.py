def run_substring_dfa(input_string):
    # 1. Define the minimized transition table
    transitions = {
        "q0":  {"0": "q0",  "1": "q1"},
        "q1":  {"0": "q23", "1": "q1"},
        "q23": {"0": "q23", "1": "q23"}
    }
    
    # 2. Define start and accept states
    current_state = "q0"
    accept_states = {"q23"}
    
    # 3. Process the input string
    for char in input_string:
        if char not in ["0", "1"]:
            return False, "Error: Invalid character. Only 0 and 1 allowed."
        
        current_state = transitions[current_state][char]
        
    # 4. Return whether the final state is an accept state
    is_accepted = current_state in accept_states
    return is_accepted, current_state

# --- INTERACTIVE LOOP ---

print("Substring '10' DFA Tester")
print("Type 'quit' or 'exit' to stop.")

while True:
    user_input = input("\nEnter a binary string: ").strip()
    
    if user_input.lower() in ['quit', 'exit']:
        print("Exiting DFA Tester.")
        break
        
    if not user_input:
        print("Input cannot be empty.")
        continue
        
    accepted, final_state = run_substring_dfa(user_input)
    
    if final_state.startswith("Error"):
        print(final_state)
    else:
        status = "Accepted" if accepted else "Rejected"
        print(f"Result: {status} (Ended in state {final_state})")