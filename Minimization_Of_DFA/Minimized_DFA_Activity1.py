def run_minimized_dfa(input_string):
    # 1. Define the transition table for the minimized DFA
    transitions = {
        "AC": {"0": "B", "1": "AC"},
        "B":  {"0": "B", "1": "D"},
        "D":  {"0": "B", "1": "E"},
        "E":  {"0": "B", "1": "AC"}
    }
    
    # 2. Define the starting state and the set of accepting states
    current_state = "AC"
    accept_states = {"E"}
    
    # 3. Process the input string one character at a time
    for char in input_string:
        if char not in ["0", "1"]:
            return False, "Error: Invalid character. Only 0 and 1 are allowed."
        
        # Move to the next state based on the current state and input character
        current_state = transitions[current_state][char]
        
    # 4. Check if the final state is an accept state
    is_accepted = current_state in accept_states
    return is_accepted, current_state

# --- INTERACTIVE LOOP ---

print("DFA Tester started. Type 'quit' or 'exit' to stop.")

while True:
    # Prompt the user for input
    user_input = input("\nEnter a binary string: ").strip()
    
    # Check if the user wants to exit
    if user_input.lower() in ['quit', 'exit']:
        print("Exiting DFA Tester.")
        break
        
    # Handle empty inputs gracefully
    if not user_input:
        print("Input cannot be empty. Try again.")
        continue
        
    # Run the DFA logic
    accepted, final_state = run_minimized_dfa(user_input)
    
    # Print the result
    if final_state.startswith("Error"):
        print(final_state)
    else:
        status = "Accepted" if accepted else "Rejected"
        print(f"Result: {status} (Ended in state {final_state})")