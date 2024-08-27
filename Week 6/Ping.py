"""CLI"""
import re
from statistics import mean

def get_ping_target():
    """Extract ping target from first and third lines of input."""
    line1 = input()
    input()  # Skip second line
    line3 = input()

    match = re.search(r'ping (\S+)', line1)
    if match and match.group(1)[0].isdigit():
        return match.group(1)
    return re.search(r'\[(.*?)\]', line3).group(1)

def extract_time(line):
    """Extract time from a ping response line."""
    match = re.search(r'time=(\d+)', line.replace('<1', '=0'))
    return int(match.group(1)) if match else None

def process_ping_results():
    """Process ping results and return statistics."""
    target = get_ping_target()
    times = [extract_time(input()) for _ in range(4)]
    received = sum(1 for t in times if t is not None)

    return {
        'target': target,
        'sent': 4,
        'received': received,
        'lost': 4 - received,
        'times': [t for t in times if t is not None]
    }

def print_statistics(stats):
    """Print ping statistics."""
    print(f"Ping statistics for {stats['target']}:")
    loss_percentage = stats['lost'] * 25
    print(f"    Packets: Sent = {stats['sent']}, Received = {stats['received']}, "
          f"Lost = {stats['lost']} ({loss_percentage}% loss),")

    if stats['times']:
        print("Approximate round trip times in milli-seconds:")
        print(f"    Minimum = {min(stats['times'])}ms, "
              f"Maximum = {max(stats['times'])}ms, "
              f"Average = {int(mean(stats['times']))}ms")

def main():
    """Let's started"""
    stats = process_ping_results()
    print_statistics(stats)

if __name__ == "__main__":
    main()
