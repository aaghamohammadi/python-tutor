def main():
    n_sentences = parse_n_sentences()
    sentences = parse_sentences(n_sentences)
    number_of_duplicates(sentences)
    count = total_duplicate_adjunct_ch(sentences)
    print(count)


def total_duplicate_adjunct_ch(sentences):
    count = 0
    for sentence in sentences:
        sentence_words = sentence.split()
        for word in sentence_words:
            if has_adjunct_ch(word):
                count += 1
    return count


def has_adjunct_ch(word):
    for i in range(len(word) - 1):
        if word[i] == word[i + 1]:
            return True
    return False


def number_of_duplicates(sentences):
    for sentence in sentences:
        duplicates = number_of_duplicate_words_in_a_sentence(sentence)
        print(duplicates)


def number_of_duplicate_words_in_a_sentence(sentence):
    sentence_words = sentence.lower().split()
    return len(sentence_words) - len(set(sentence_words))


def parse_n_sentences():
    n_sentences = input()
    n_sentences = int(n_sentences)
    return n_sentences


def parse_sentences(n_sentences):
    sentences = []
    for i in range(n_sentences):
        sentences.append(input().lower())
    return sentences


if __name__ == '__main__':
    main()
