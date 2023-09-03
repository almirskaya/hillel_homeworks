class CustomIterator:
    """
       Custom iterator that accepts a sequence and iterates over values within a given range.

       Args:
           sequence (sequence): The sequence to iterate over.
           start_index (int): The starting index of the range.
           end_index (int): The ending index of the range.
    """
    def __init__(self, sequence, start_index, end_index):
        self.sequence = sequence
        self.start_index = start_index
        self.end_index = end_index
        self.current_index = start_index

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index <= self.end_index:
            cur_value = self.sequence[self.current_index]
            self.current_index += 1
            return cur_value - 1
        else:
            raise StopIteration


if __name__ == "__main__":
    sequence = [1, 2, 3, 4, 5]
    iterator = CustomIterator(sequence, -1, 2)

    for value in iterator:
        print(value)
