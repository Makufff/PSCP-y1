"""SaveComputeRepeat"""
def main():
    """main"""
    start_here = 492137954293754252786
    milliseconds = start_here
    seconds = milliseconds // 1000
    milliseconds = milliseconds % 1000
    minutes = seconds // 60
    seconds = seconds % 60
    hours = minutes // 60
    minutes = minutes % 60
    days = hours // 24
    hours = hours % 24
    print(f"{days} {hours} {minutes} {seconds} {milliseconds}")
main()
