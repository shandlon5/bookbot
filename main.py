def get_book_text(path_to_file):
    with open(path_to_file) as f:
         text = f.read()
         return text 
import sys
from stats import word_count

from stats import character_amount

from stats import report

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
# Step 1: Get the text from your file
    path_to_file = sys.argv[1]
    text = get_book_text(path_to_file)  # Make sure the path is correct
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



