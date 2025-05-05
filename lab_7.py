def compute_lps(pattern):
    lps = [0] * len(pattern)
    length = 0
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    return lps

def search(haystack, needle):
    if not needle:
        return []

    lps = compute_lps(needle)
    result = []
    i = 0
    j = 0

    while i < len(haystack):
        if haystack[i] == needle[j]:
            i += 1
            j += 1
            if j == len(needle):
                result.append(i - j)
                j = lps[j - 1]
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return result

if __name__ == "__main__":
    haystack = input("Введіть текст, в якому хочете шукати збіги: ")
    needle = input("Введіть текст, який хочете знайти в іншому: ")
    print("Знайдено на позиціях:", search(haystack, needle))
