class DynamicArray:
    def __init__(self, capacity=2):
        self.capacity = capacity
        self.size = 0
        self.array = [None] * capacity

    def insert(self, value):
        if self.size == self.capacity:
            # Double the capacity
            self.capacity *= 2
            new_array = [None] * self.capacity
            # Copy old values
            for i in range(self.size):
                new_array[i] = self.array[i]
            self.array = new_array
        # Insert new value
        self.array[self.size] = value
        self.size += 1

    def __str__(self):
        return f"Array: {self.array[:self.size]}, Capacity: {self.capacity}"

# Test
dyn = DynamicArray(2)
for val in [10, 20, 30, 40, 50]:
    dyn.insert(val)
    print(dyn)
