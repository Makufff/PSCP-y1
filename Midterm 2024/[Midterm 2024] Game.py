"""Game"""
def min_draws(score_a, score_b):
    """calu draw"""
    if score_a % 3 == score_b % 3 :
        return score_a % 3
    return "Error"

inputs_score_a = int(input())
inputs_score_b = int(input())

result = min_draws(inputs_score_a, inputs_score_b)
print(result)
