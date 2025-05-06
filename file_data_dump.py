import os

class AhoNode:
    def __init__(self):
        self.goto = {}
        self.out = []
        self.fail = None

def aho_create_forest(patterns):
    root = AhoNode()
    for path in patterns:
        node = root
        for symbol in path:
            node = node.goto.setdefault(symbol, AhoNode())
        node.out.append(path)
    return root

def create_statemachine(patterns):
    root = aho_create_forest(patterns)
    queue = []
    for node in root.goto.values():
        node.fail = root
        queue.append(node)

    while queue:
        rnode = queue.pop(0)
        for key, unode in rnode.goto.items():
            queue.append(unode)
            fnode = rnode.fail
            while fnode is not None and key not in fnode.goto:
                fnode = fnode.fail
            unode.fail = fnode.goto[key] if fnode and key in fnode.goto else root
            unode.out += unode.fail.out
    return root

def search_lines(lines, root):
    results = []
    for line in lines:
        node = root
        i = 0
        line_stripped = line.strip()
        while i < len(line):
            while node is not None and line[i] not in node.goto:
                node = node.fail
            if node is None:
                node = root
                i += 1
                continue
            node = node.goto[line[i]]
            if node.out:
                for pattern in node.out:
                    results.append((pattern, line_stripped))
            i += 1
    return results

if __name__ == "__main__":
    patterns = ["TODO", "FIXME", "BUG", "HACK", "NOTE", "OPTIMIZE", 
                "REVIEW", "DEPRECATED", "XXX"]

    with open("input.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()

    root = create_statemachine(patterns)
    matches = search_lines(lines, root)

    os.makedirs("results", exist_ok=True)

    for pattern, line in matches:
        filename = os.path.join("results", f"{pattern}.txt")
        with open(filename, "a", encoding="utf-8") as f:
            f.write(line + "\n")
