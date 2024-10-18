"""Impostor"""
def main():
    """Main function"""
    crew_members = {}
    while True:
        line = input()
        if line == "Start":
            break
        member = line.strip().strip('{}').split(':')
        name = member[0].strip().strip('" ')
        role = member[1].strip().strip('" ')
        crew_members[name] = role
    voted_out = []
    while True:
        line = input()
        if line == "End":
            break
        voted_out.append(line.strip())
    alive = {name: role for name, role in crew_members.items() if name not in voted_out}
    dead = {name: role for name, role in crew_members.items() if name in voted_out}
    impostor_count = sum(1 for role in alive.values() if role == "Impostor")
    print(f"{impostor_count} Impostor Remains")
    print("***Alive***")
    for name in sorted(alive.keys()):
        print(f"{name} : {alive[name]}")
    print("***Dead***")
    for name in sorted(dead.keys()):
        print(f"{name} : {dead[name]}")
main()
