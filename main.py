def get_book_text(path_to_file):
    with open(path_to_file) as f:
         text = f.read()
         return text 

from stats import word_count

from stats import character_amount

from stats import report

def main():
# Step 1: Get the text from your file
    text = get_book_text("books/frankenstein.txt")  # Make sure the path is correct
    words = word_count(text)
    counts = character_amount(text)
    
    sorted_counts = sorted(counts.items(), reverse=True, key=report)
    print("============ BOOKBOT ============")
    print("Analyzing book found at {path_to_file}")
    print("----------- Word Count ----------")
    word_count(text)
    print("--------- Character Count -------")
    for char, count in sorted_counts:
        print(f"{char}: {count}")
    print("============= END ===============")

main()



