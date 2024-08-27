"""DNA Krub P'Few"""
def find_longest_common_substring(dna1, dna2):
    """Main Function use Dynamic Programming for Longest Common Substring"""
    def is_valid_dna(dna):
        """Checks DNA sequence"""
        return all(c in 'ACGT' for c in dna)

    if not is_valid_dna(dna1) or not is_valid_dna(dna2):
        return "Error"

    def longest_common_substring(s1, s2):
        """longest common substring"""
        len1, len2 = len(s1), len(s2)
        longest = ""

        dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]

        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    if dp[i][j] > len(longest):
                        longest = s1[i - dp[i][j]:i]
                else:
                    dp[i][j] = 0

        return longest if longest else "None"

    return longest_common_substring(dna1, dna2)

print(find_longest_common_substring(input().strip(), input().strip()))
