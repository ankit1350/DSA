class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.ht = [-1] * size   # initialize with -1 (empty slots)

    def insert(self, key):
        loc = key % self.size
        if self.ht[loc] == -1:
            self.ht[loc] = key
        else:
            cnt = 0
            start = loc
            while self.ht[loc] != -1 and cnt < self.size:
                loc = (loc + 1) % self.size
                cnt += 1
            if cnt < self.size:
                self.ht[loc] = key
            else:
                print(f"Table full, cannot insert {key}")

    def display(self):
        for i, val in enumerate(self.ht):
            print(f"{i} --> {val}")


# Example usage
h = HashTable()
while True:
    key = int(input("Enter key to insert: "))
    h.insert(key)
    ans = int(input("Do you want to insert more keys? (1=yes / 0=no): "))
    if ans != 1:
        break

h.display()
