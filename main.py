def count_words(text): #makes a count of all the words based on spaces
    words = text.split()
    return len(words)

def count_characters(text): #creates dictionary of all letters and a count of each
    characters = {}
    for char in text:
        lowered_char = char.lower()
        if lowered_char.isalpha(): #check if its an alpha character
            characters[lowered_char] = characters.get(lowered_char, 0) +1 #increment count
    
    #creates a list of dictionaries from character counts
    letter_list =[{"letter": letter, "count": count} for letter, count in characters.items()]

    #sort the list based on character count, descending
    letter_list.sort(reverse=True, key=lambda item: item["count"])

    # return sorted list
    return letter_list

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

        #get word count
        word_count = count_words(file_contents)
        print(f"{word_count} words found in the document\n")

        #get character counts
        char_count = count_characters(file_contents)

        #print the character counts
    for item in char_count:
        print(f"The '{item['letter']}' character was found {item['count']} times")

if __name__ == "__main__":
    main()
