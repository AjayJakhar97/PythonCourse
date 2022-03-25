# Anagram : An anagram is a word or phrase formed by rearranging the letters of a different word or phrase.
'''
An examples could include.

“Listen” and “Silent”
Where you notice that the letters in LISTEN are the exact same as in SILENT, just in a different order.

What you also notice is that the lowercase and uppercase of the letters do not matter.

The definition says also phrases, hence, examples of anagrams include.

“a gentleman” and “elegant man”
“eleven plus two” and “twelve plus one”
“William Shakespeare” = “I am a weakish speller”
The last example is quite interesting, as it shows that the number of spaces do not seem to matter. The phrase “William Shakespeare” has 1 space, while the phrase “I am a weakish speller” has 4 spaces.
'''
# %%  https://www.learnpythonwithrune.org/understand-why-anagram-is-a-favorite-interview-coding-problem/

def is_anagram_naive(str_a, str_b):
    if len(str_a) != len(str_b):
        return False
    for c in str_a:
        if c not in str_b:
            return False
        else:
            str_b = str_b.replace(c, '', 1)
    return True

print(is_anagram_naive("silent", "listen"))
print(is_anagram_naive("elevenplustwo", "twelveplusone"))
print(is_anagram_naive("anna", "anaa"))


# %%

def is_anagram_improved(str_a, str_b):
    if len(str_a) != len(str_b):
        return False
    list_a = list(str_a)
    list_b = list(str_b)
    list_a.sort()
    list_b.sort()
    for l1, l2 in zip(list_a, list_b):
        if l1 != l2:
            return False
    return True

print(is_anagram_improved("silent", "listen"))
print(is_anagram_improved("elevenplustwo", "twelveplusone"))
print(is_anagram_improved("anna", "anaa"))

#%% 

