# Execute both files

import mood_responses
import text_utils as tu  # Import the custom module with an alias

# Ask the user for their mood
mood = input("How are you feeling today? ")

# [ Task 1 Execution ]
print(mood_responses.mood_response(mood))

# [ Task 2 Execution ]
text = input("Enter string to adjust: ")
reversed_string = tu.reverse_string(text)
print(f"Reversed string: {reversed_string}")

capitalized_string = tu.capitalize_string(text)
print(f"Capitalized string: {capitalized_string}")
