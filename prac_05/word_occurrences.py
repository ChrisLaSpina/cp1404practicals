def main():
    counted_phrase = {}
    phrase = input("Enter a phrase: ")
    print("Text:", phrase)
    phrase = phrase.split()
    for word in phrase:
        counts = phrase.count(word)
        counted_phrase[word] = counts

    for word, count in counted_phrase.items():
        print("{:{}} : {}".format(word, 8, count))


main()
