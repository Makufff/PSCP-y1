"""Bubble"""
def simulate_bubble_jump(course: str) -> tuple[str, int]:
    """
    Simulate a bubble jumping through a course.

    Args:
        course (str): A string representing the course

    Returns:
        tuple[str, int]: A tuple containing the result ("POSSIBLE" or "IMPOSSIBLE")
                         and the count of jumps or remaining distance
    """

    position = 0
    jump_count = 0
    course_length = len(course)

    while position < course_length - 1:
        current_char = course[position]

        if current_char in ("^", "a", "b", "c", "d", "e"):
            jump_count += 1
            position += 1
        elif current_char.isupper():
            jump_count += 1
            position += 3

            if position >= course_length - 1:
                break

            backtrack = 0
            while backtrack < 2 and position < course_length and course[position].islower():
                position -= 1
                backtrack += 1

            if position < course_length and not course[position].isupper():
                position += backtrack

            while position < course_length and course[position].isspace():
                position -= 1
        
        if position < course_length and course[position].isspace():
            return "IMPOSSIBLE", course_length - position

    return "POSSIBLE", jump_count

def main():
    """Main function"""
    course = input()
    result, count = simulate_bubble_jump(course)
    print(result)
    print(count)

if __name__ == "__main__":
    main()
