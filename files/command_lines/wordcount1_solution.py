from wordcount import read_file, word_count, print_counts

data = read_file("sample-text.txt")
counts = word_count(data)
print_counts(counts)
