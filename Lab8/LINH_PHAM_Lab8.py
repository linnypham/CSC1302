total_words = 0
total_lines = 0

with open('example.txt', 'r') as infile:
    for line in infile:
        total_words += len(line.split())
        total_lines += 1

print(f'Total number of words: {total_words}')
print(f'Total number of lines: {total_lines}')
print('Word count per line (line_number >> word_count):')

index = 0

with open('output.txt', 'w') as output:
    output.write(f'Total number of words: {total_words}\n')
    output.write(f'Total number of lines: {total_lines}\n')
    output.write('Word count per line (line_number >> word_count):\n')

    with open('example.txt', 'r') as infile:
        for line in infile:
            index += 1
            num_words = len(line.split())
            output.write(f'Line {index} >> {num_words} words\n')
            print(f"Line {index} >> {num_words} words")
