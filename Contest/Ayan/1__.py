def fun(words):
    result = []
    for word in words:
        i = 0
        ans = 0
        while i < len(word):
            count_ = 1
            while i < len(word) - 1 and word[i] == word[i + 1]:
                count_ += 1
                i += 1
            i += 1
            ans += (count_ // 2)
        result.append(ans)
    return result
words = ["ab", "abb", "aab", "aaa", "abab", "abaaaba", 'abaaaaaaab']
print(fun(words))
                