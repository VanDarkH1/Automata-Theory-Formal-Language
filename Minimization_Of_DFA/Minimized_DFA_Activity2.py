def run_second_minimized_dfa(input_string):
    # 1. Define the transition table for the minimized DFA
    transitions = {
        "AB":  {"0": "AB",  "1": "CDE"},
        "CDE": {"0": "CDE", "1": "F"},
        "F":   {"0": "F",   "1": "F"}
    }
    
    # 2. Define the starting state and the set of accepting states
    current_state = "AB"
    accept_states = {"CDE"}
    
    # 3. Process the input string one character at a time
    for char in input_string:
        if char not in ["0", "1"]:
            return False, "Error: Invalid character. Only 0 and 1 are allowed."
        
        # Move to the next state
        current_state = transitions[current_state][char]
        
    # 4. Check if the final state is an accept state
    is_accepted = current_state in accept_states
    return is_accepted, current_state

# --- INTERACTIVE LOOP ---

print("DFA Tester started for the second minimized machine.")
print("Type 'quit' or 'exit' to stop.")

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
    accepted, final_state = run_second_minimized_dfa(user_input)
    
    # Print the result
    if final_state.startswith("Error"):
        print(final_state)
    else:
        status = "Accepted" if accepted else "Rejected"
        print(f"Result: {status} (Ended in state {final_state})")