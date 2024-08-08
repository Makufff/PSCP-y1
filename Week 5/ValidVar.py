"""Vaild Variable"""
KEYWORDS = [
    'if', 'else', 'elif', 'while', 'for', 'True', 'False', 'continue', 'break',
    'return', 'is', 'in', 'and', 'or', 'from', 'as', 'pass', 'not', 'def', 'None'
]

def is_valid_variable_name(name):
    """
    Check if the given name is a valid variable name.

    Args:
    name (str): The variable name to check.

    Returns:
    bool: True if the name is valid, False otherwise.
    """
    name = name.strip()

    if not name:
        return False

    if name[0].isdigit() or name in KEYWORDS:
        return False

    return all(char.isalnum() or char == '_' for char in name)

def validate_variable_names(num_names):
    """
    Validate a specified number of variable names.

    Args:
    num_names (int): The number of variable names to validate.
    """
    for _ in range(num_names):
        name = input().strip()
        result = "Valid" if is_valid_variable_name(name) else "Invalid"
        print(result)

def main():
    """Main function to run the variable name validator."""
    num_names = int(input().strip())
    validate_variable_names(num_names)

if __name__ == "__main__":
    main()
