def reverse_with_slice(input_text: str) -> str:
        return input_text[::-1]

def reverse_recursively(text_to_reverse: str) -> str:
    
    if len(text_to_reverse) <= 0:
        return ""
    return text_to_reverse[-1] + reverse_recursively(text_to_reverse[:-1])

def reverse_text_user(original_input: str) -> str:
    print("Analyzing your input...")
    user_choice = input("Choose a reversal method (slice/recursion): ")
    print("Understood your choice.")

    if user_choice == "slice":
        return reverse_with_slice(original_input)

    if user_choice == "recursion":
        return reverse_recursively(original_input)

    print("Invalid choice. Using slicing as default.")
    return reverse_with_slice(original_input)

def main() -> None:
    
    user_text = input("Enter a string to reverse: ")
    reversed_text = reverse_text_user(user_text)
    print("Original string:", user_text)
    print("Reversed string:", reversed_text)

if __name__ == "__main__":
    main()