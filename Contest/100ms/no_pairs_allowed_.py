def get_char_change(word):
    count_ = 0
    i = 0
    while i < len(word):
        if i < len(word) - 1 and word[i] == word[i + 1]:
            count_ += 1
            i += 1
        i += 1
    return count_
def minimalOperartions(words):
    return [get_char_change(words[i]) for i in range(len(words))]

words = ["add", "boook", "break"]
words = [ 'ab','aab','abb', 'abab','abaaaba' ]
print(minimalOperartions(words))
        