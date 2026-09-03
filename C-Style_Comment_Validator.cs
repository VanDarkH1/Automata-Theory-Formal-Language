using System;

public class CStyleCommentValidator
{
    // Define the states of our Deterministic Finite Automaton (DFA)
    private enum State
    {
        Start,
        SeenFirstSlash,
        InsideComment,
        SeenStarInside,
        Accepted,
        Dead
    }

    public static bool IsValid(string input)
    {
        if (string.IsNullOrEmpty(input)) return false;

        State currentState = State.Start;

        foreach (char c in input)
        {
            // Map character to the allowed alphabet { '/', '*', 'a' (everything else) }
            char mappedChar = (c == '/' || c == '*') ? c : 'a';

            switch (currentState)
            {
                case State.Start:
                    currentState = (mappedChar == '/') ? State.SeenFirstSlash : State.Dead;
                    break;
                
                case State.SeenFirstSlash:
                    currentState = (mappedChar == '*') ? State.InsideComment : State.Dead;
                    break;
                
                case State.InsideComment:
                    if (mappedChar == '*') currentState = State.SeenStarInside;
                    // 'a' or '/' keeps the DFA inside the comment
                    break;
                
                case State.SeenStarInside:
                    if (mappedChar == '/') currentState = State.Accepted;
                    else if (mappedChar == '*') currentState = State.SeenStarInside;
                    else currentState = State.InsideComment; // Reverted back to inside by an 'a'
                    break;
                
                case State.Accepted:
                    // Any character after a complete comment invalidates the string
                    currentState = State.Dead; 
                    break;
                
                case State.Dead:
                    return false; // Fast fail once the dead state is reached
            }
        }

        // The string is only valid if it terminates exactly in the Accepted state
        return currentState == State.Accepted;
    }

    public static void Main()
    {
        Console.WriteLine("C-Style Comment Validator");
        Console.WriteLine("Type 'exit' to quit.");
        Console.WriteLine(new string('-', 25));

        while (true)
        {
            Console.Write("\nEnter a string to validate: ");
            string input = Console.ReadLine();

            // Exit condition
            if (input != null && input.Trim().Equals("exit", StringComparison.OrdinalIgnoreCase))
            {
                Console.WriteLine("Exiting validator...");
                break;
            }

            // Validate and print the result
            bool isValid = IsValid(input);
            
            if (isValid)
            {
                Console.WriteLine("Result: ACCEPTED");
            }
            else
            {
                Console.WriteLine("Result: REJECTED");
            }
        }
    }
}