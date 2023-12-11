# Compact banner design with replacement
banner = '''
\033[1;32m ____   __   ____  __ _    ____  _  _   __  ____  __ _  __  _  _ \033[0m
\033[1;32m(    \ / _\ (  _ \(  / )  (  _ \/ )( \ /  \(  __)(  ( \(  )( \/ )\033[0m
\033[1;32m ) D (/    \ )   / )  (    ) __/) __ ((  O )) _) /    / )(  )  ( \033[0m
\033[1;32m(____/\_/\_/(__\_)(__\_)  (__)  \_)(_/ \__/(____)\_)__)(__)(_/\_)\033[0m
\033[1;32mAuthor: \033[1;32mSh tamim\033[0m \033[1;31mVersion: \033[1;31m1.0\033[0m
'''

print(banner)

# Rest of the code remains unchanged
import itertools

def generate_wordlist(chars, min_length, max_length, output_file):
    with open(output_file, 'w') as f:
        for length in range(min_length, max_length + 1):
            for combination in itertools.product(chars, repeat=length):
                word = ''.join(combination)
                f.write(word + '\n')

if __name__ == "__main__":
    try:
        chars = input("Enter characters to include in the wordlist: ")
        min_length = int(input("Enter the minimum word length: "))
        max_length = int(input("Enter the maximum word length: "))
        output_file = input("Enter the output file name: ")
    except ValueError:
        print("Invalid input. Please enter valid values.")
        exit(1)

    generate_wordlist(chars, min_length, max_length, output_file)
    print("Wordlist generated successfully.")
