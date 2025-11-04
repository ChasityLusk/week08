from functools import reduce

def read_numbers(filename):
    """Reads numbers froma text file and returns a list of floats."""
    with open(filename, 'r') as f:
        numbers = list(map(float, f.readlines()))
    return numbers    


def compute_average(numbers):
    """Computes the average of alist of numbers using high-order functions."""
    total = reduce(lambda x, y: x + y, numbers)
    return total / len(numbers) if numbers else 0


def main():
    filename = input("Enter the filename: ")
    numbers = read_numbers(filename)
    average = compute_average(numbers)
    print(f"The average of the numbers in {filename} is: {average}")

if __name__ == "__main__":
    main()
