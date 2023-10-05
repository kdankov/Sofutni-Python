from string import punctuation

with open('text.txt') as input_file, open('output.txt', 'w') as output_file:
    result = []
    for row, line in enumerate(input_file):
        letters_count = 0
        punctuation_marks_count = 0

        for ch in line:
            if ch.isalpha():
                letters_count += 1
            elif ch in punctuation:
                punctuation_marks_count += 1
        result.append(f'Line {row + 1}: {line[:-1]} ({letters_count})({punctuation_marks_count})')

    output_file.write('\n'.join(result))