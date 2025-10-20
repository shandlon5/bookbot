def get_book_text(path_to_file):
    with open(path_to_file) as f:
         text = f.read()
         return text 

def word_count(text):
    num_words = text.split()
    count = len(num_words)
    print(f"Found {count} total words")
    return count

def main():
# Step 1: Get the text from your file
    text = get_book_text("books/frankenstein.txt")  # Make sure the path is correct

# Step 2: Count the words in that text
    total_words = word_count(text)

main()



