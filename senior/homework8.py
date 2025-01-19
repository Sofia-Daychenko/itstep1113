class EvenNumberIterator:
    def __init__(self, sequence, max_iterations):
        self.sequence = sequence
        self.max_iterations = max_iterations
        self.count = 0

    def __iter__(self):
        self.count = 0
        self.evens = [num for num in self.sequence if num % 2 == 0]
        return iter(self.evens[:self.max_iterations])

numbers = list(range(1, 21))

even_iterator = EvenNumberIterator(numbers, max_iterations=20)

for even_number in even_iterator:
    print(even_number)
