"""Cat Parade"""
def process_parade():
    """Cat Parade"""
    parade = []
    breed_info = {}
    breed_stack = []

    while True:
        line = input().strip()
        if line == "END":
            break

        if line == "IT'S A DOG":
            if breed_stack:
                last_breed = breed_stack.pop()
                if last_breed in breed_info:
                    breed_info[last_breed][1] -= 1
                    if not breed_info[last_breed][1]:
                        del breed_info[last_breed]
                parade.pop()
            continue

        # Split the line into breeds
        breeds = [b.strip() for b in line.split(", ")]
        for breed in breeds:
            if breed not in breed_info:
                breed_info[breed] = [len(parade) + 1, 1]
            else:
                breed_info[breed][1] += 1

            parade.append(breed)
            breed_stack.append(breed)

    output = []
    for breed in sorted(breed_info):
        first_position, count = breed_info[breed]
        output.append(f"{breed} {first_position} {count}")

    for line in output:
        print(line)

process_parade()
