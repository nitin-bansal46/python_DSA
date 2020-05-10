class Node(object):

    def __init__(self, character):

        self.character = character
        self.middle = None
        self.left = None
        self.right = None
        self.value = 0

class TST(object):

    def __init__(self):
        self.root_node = None

    def put(self, key, value):

        self.root_node = self.put_item(self.root_node, key, value, 0)

    def put_item(self, cur_node, key, value, index):

        c = key[index]

        if cur_node is None:
            cur_node = Node(c)

        if c < cur_node.character:
            cur_node.left = self.put_item(cur_node.left, key, value, index)

        elif c > cur_node.character:
            cur_node.right = self.put_item(cur_node.right, key, value, index)

        elif index < len(key) - 1:
            cur_node.middle = self.put_item(cur_node.middle, key, value, index + 1)

        else:
            cur_node.value = value

        return cur_node

    def get(self, key):
        cur_node = self.get_item(self.root_node, key, 0)

        if cur_node is None:
            return ("No such key Found")
        return cur_node.value

    def get_item(self, cur_node, key, index):

        if cur_node is None:
            return None

        c = key[index]

        if c < cur_node.character:
            return self.get_item(cur_node.left, key, index)
        elif c > cur_node.character:
            return self.get_item(cur_node.right, key, index)
        elif index < len(key) - 1:
            return self.get_item(cur_node.middle, key, index +1)
        else:
            return cur_node


test = TST()
test.put("lamao", 100)
test.put("dune", 10)
test.put("bust", 200)
test.put("nits", 1000)
test.put("flow", 400)

print(test.get("flow"))
print(test.get("yes"))