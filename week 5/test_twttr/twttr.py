def main():
    word = input('Input: ')
    print(f'Output: {shorten(word)}')


def shorten(word):
    ntweet = ''
    for letter in word:
        if letter not in set('aeiouAEIOU'):
            ntweet += letter
    return ntweet


if __name__ == "__main__":
    main()
