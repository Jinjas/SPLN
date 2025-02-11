import re
import sys

def remove_repetitive_lines(input_file):
    seen_lines = set()
    pattern = re.compile(r'^.*$')  # Matches entire lines
    
    with open(input_file, 'r', encoding='utf-8') as infile, open('output.txt', 'w', encoding='utf-8') as outfile:
        for line in infile:
            match = pattern.match(line)
            if match and match.group(0) not in seen_lines:
                outfile.write(line)
                seen_lines.add(match.group(0))

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script.py <input_file>")
    else:
        input_file = sys.argv[1]
        remove_repetitive_lines(input_file)
        print(f'Repetitive lines removed from {input_file} and saved to output.txt')
