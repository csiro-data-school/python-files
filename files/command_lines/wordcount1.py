from wordcount import read_file, word_count

counts = word_count(read_file("sample-text.txt"))
for word, count in counts.items():
    if count >= 2:
        print("{0}: {1}".format(word, count))
