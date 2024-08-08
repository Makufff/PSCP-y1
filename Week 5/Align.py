"""Left"""
def main(size , direction , message):
    """Direction"""
    direction = direction.lower()
    if direction == "left":
        print(message+" "*(size-len(message)))
    elif direction == "center":
        space1 = (size-len(message))//2
        space2 = (size-len(message))%2
        print(" "*(space1+space2)+message+" "*space1)
    elif direction == "right":
        print(" "*(size-len(message))+message)
main(int(input()) , input() , input())
