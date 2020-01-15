def main():
    languages = {
        'Python': 'Guido van Rossum',
        'Ruby': 'Yukihiro Matsumoto',
        'PHP': 'Rasmus Lerdorf',
    }
    for language in languages:
        print(language, languages.get(language))


if __name__ == '__main__':
    main()
