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

