import difflib
import heapq

def read_strings_from_file(filename):
    with open(filename, 'r') as file:
        strings = [line.strip() for line in file.readlines()]
    return strings

def get_top_k_similar_strings(input_string, strings, k=3):
    # Calculate the similarity of input_string with each string in the list
    similarities = [(difflib.SequenceMatcher(None, input_string, s).ratio(), s) for s in strings]
    # Get the top k similar strings based on the similarity score
    top_k_similar = heapq.nlargest(k, similarities, key=lambda x: x[0])
    return [s for _, s in top_k_similar]

def main():
    # Read strings from a file (you can replace 'strings.txt' with your actual file)
    strings = read_strings_from_file('strings.txt')
    
    while True:
        # Take user input
        user_input = input("Input >> ")
        if user_input.lower() == 'exit':
            break
        
        # Find and print the top k similar strings
        suggestions = get_top_k_similar_strings(user_input, strings, k=3)
        print("Output >>", ", ".join(suggestions))

if __name__ == "__main__":
    main()
