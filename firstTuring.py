#Sam Crowe
#Practice reading the  turing.txt

def read_text_to_list(filename):
    """
    Reads the content of a file and stores each line as a separate element in a list.
    :param filename: The name of the file to read.
    :return: A list containing each line of the file as an element.
    """
    with open(filename, 'r') as file:
        lines = file.readlines()
    return lines

def first_and_last_two(lines):
    """
    Prints the first and last two elements of the list.
    :param lines: The list of lines from the file.
    """
    print("First two lines:")
    print(lines[0].strip())
    print(lines[1].strip())
    print("\nLast two lines:")
    print(lines[-2].strip())
    print(lines[-1].strip())

def num_of_lines(lines):
    """
    Prints the number of lines in the list.
    :param lines: The list of lines from the file.
    """
    print("\nNumber of lines in the file:", len(lines))

def main():
    filename = 'turing.txt'
    lines = read_text_to_list(filename)
    first_and_last_two(lines)
    num_of_lines(lines)
    print(lines)

if __name__ == "__main__":
    main()