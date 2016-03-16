VOWELS = set("aeiouAEIOU")

def anti_vowel(text):
    return "".join(ch for ch in text if ch not in VOWELS)