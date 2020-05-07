class HashTable(object):            #creatring a class
#defining constructor for our class
    def __init__(self):
        self.size = 10 # initial size but can be increased till 256
        self.keys = [None]*self.size
        self.values = [None]*self.size

    # hash_function basically converts the keys into integer if given
    # in string, here with ord() function we rae converting string characters into its ascii values and
    # then adding all the values, but this value may be out of range of our hash_table size so we are
    # taking modulus with the size of the hash_table
    def hash_function(self, keys):

        sum1 = 0
        for pos in range(len(keys)):
            sum1 = sum1 + ord(keys[pos])

            return sum1 % self.size

    def put(self, new_key, new_value):
        # Calling hash function to generate value of index from given key
        # now here we will have 3 cases
        # case:1 --> Initial table is empty, we will have to just input the value to the
        # case:2 --> there is a value at the index, but the key is same as new_key, here we just
        #            have to update the old value with new_value
        # case:3 --> index is already occupied and the key is not same as new_key, this is called collision
        #             in this we just need to find the next empty cell
        index = self.hash_function(new_key)

        while self.keys[index] is not None:
            if self.keys[index] == new_key:
                self.values[index] = new_value
                return

            index = (index + 1)% self.size

        self.keys[index] = new_key
        self.values[index] = new_value

    # a function to find the value associated with the given key
    # here we can have two cases
    # case:1 --> index found  was directly designated to the key
    # case:2 --> index found was in collision so it was changed

    def get(self, key_to_find):

        index = self.hash_function(key_to_find)

        while self.keys[index] is not None:
            if self.keys[index] == key_to_find:
                print(self.values[index])

            index = (index + 1) % self.size

        return None

myhash = HashTable()
myhash.put("1","test1")
myhash.put("2","test2")
myhash.put("3","test3")
myhash.put("4","test4")

myhash.get("4")
