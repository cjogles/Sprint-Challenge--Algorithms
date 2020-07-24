'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    first_2_chars = word[:2]
    word_len = len(word)
    if word_len <= 2:
        if first_2_chars == "th":
            return 1
        else:
            return 0
    else:
        if first_2_chars == "th":
            return 1 + count_th(word[2:])
        else:
            return count_th(word[1:])

count_th("thThthTh")
