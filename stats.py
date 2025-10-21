def word_count(text):
    num_words = text.split()
    count = len(num_words)
    print(f"Found {count} total words")
    return count

def character_amount(text):
    lowercase = text.lower()
    counts = {}
    for character in lowercase:
        if character.isalpha():
            counts[character] = counts.get(character, 0) + 1
    return counts

def report(counts):
    return counts[1]


