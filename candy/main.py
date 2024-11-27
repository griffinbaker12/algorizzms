class Node:
    def __init__(self, candy=0, left=None, right=None):
        self.candy = candy
        self.left = left
        self.right = right


def read_candy_val_with_len(tree, pos, len):
    val = ""
    while pos[0] < len and tree[pos[0]] not in (" ", ")", "\n"):
        val += tree[pos[0]]
        pos[0] += 1
    return int(val)


def read_candy_val(tree, pos):
    val = ""
    while tree[pos[0]] not in (" ", ")", "\n"):
        val += tree[pos[0]]
        pos[0] += 1
    return int(val)


# NOTE: interesting that C lets us pass the pointer directly which is actually easier to manage then indexing
# this array properly; this would also be pretty annoying to do as a loop and reads so much easier with recursion
def read_tree_helper(line, pos):
    tree = Node()
    if line[pos[0]] == "(":
        pos[0] += 1
        tree.left = read_tree_helper(line, pos)
        pos[0] += 1
        tree.right = read_tree_helper(line, pos)
        pos[0] += 1
    else:
        tree.candy = read_candy_val(line, pos)
    return tree


def read_tree(tree):
    pos = [0]
    return read_tree_helper(tree, pos)


def print_candy_values(tree, depth=0):
    if tree.candy != 0:
        print(f"candy: {tree.candy} at depth: {depth}")
        return
    print_candy_values(tree.left, depth + 1)
    print_candy_values(tree.right, depth + 1)


def read_total_candy(tree):
    def get_candy(tree):
        if tree.left is None and tree.right is None:
            return tree.candy
        return get_candy(tree.left) + get_candy(tree.right)

    candy = get_candy(tree)
    print(f"total candy: {candy}")


def main():
    with open("input.txt", "r") as f:
        for i, line in enumerate(f):
            print("reading tree", i)
            print(20 * "-")
            tree = read_tree(line)
            print_candy_values(tree)
            read_total_candy(tree)
            print(20 * "-")


if __name__ == "__main__":
    main()
