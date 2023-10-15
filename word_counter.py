def count_unique_words(filename):
    try:
        with open(filename, 'r') as file:
            text = file.read().lower()
            words = text.split()

            word_count = {} 

            for word in words:
                word = word.strip('.,!?()[]{}"\'')
                if word.isalpha():
                    if word in word_count:
                        word_count[word] += 1
                    else:
                        word_count[word] = 1

            return word_count

    except FileNotFoundError:
        print(f"The file '{filename}' was not found.")
        return None

filename = 'sample.txt'

result = count_unique_words(filename)

if result:
    print("Word\t\tCount")
    print("-----------------")
    for word, count in result.items():
        print(f"{word}\t\t{count}")
