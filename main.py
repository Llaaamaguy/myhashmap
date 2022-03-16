class MyHashMap:
    def __init__(self, expt=3):
        self.radix = 2**expt
        self.keys = [None]*self.radix
        self.values = [None]*self.radix

    def __getitem__(self, key):
        keyhash = hash(key) % self.radix
        return self.values[keyhash]

    def __contains__(self, key):
        keyhash = hash(key) % self.radix
        return self.keys[keyhash] is key

    def __setitem__(self, key, value):
        keyhash = hash(key) % self.radix

        while self.values[keyhash]:
            self.rehash()

        self.keys[keyhash] = key
        self.values[keyhash] = value

    def rehash(self):
        self.radix *= 2
        new_keys = [None]*self.radix
        new_values = [None]*self.radix

        for i, key in enumerate(self.keys):
            if key:
                keyhash = hash(key) % self.radix
                new_keys[keyhash] = key
                new_values[keyhash] = self.values[i]

        self.keys = new_keys
        self.values = new_values


def main():
    test = MyHashMap()


if __name__ == "__main__":
    main()