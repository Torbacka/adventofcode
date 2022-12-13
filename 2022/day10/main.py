data = [[int(n) for n in line.strip()] for line in open("input.in").readlines()]

print(data)
visible_tree = 0
tree_score = []
for y, x_row in enumerate(data):
    for x, value in enumerate(x_row):
        row = x_row.copy()
        column = [data[n][x] for n in range(len(row))]

        tree = data[y][x]
        smaller = True
        seen = False
        viewed_trees = [0, 0, 0, 0]
        for i in range(x, -1, -1):
            if i != x and tree <= row[i]:
                viewed_trees[0] += 1
                smaller = False
                break
            if i != x:
                viewed_trees[0] += 1
        if smaller:
            seen = True
        smaller = True

        for i in range(x, len(row)):
            if i != x and tree <= row[i]:
                viewed_trees[1] += 1
                smaller = False
                break
            if i != x:
                viewed_trees[1] += 1
        if smaller:
            seen = True
        smaller = True
        for i in range(y, -1, -1):
            if i != y and tree <= column[i]:
                viewed_trees[2] += 1
                smaller = False
                break
            if i != y:
                viewed_trees[2] += 1
        if smaller:
            seen = True
        smaller = True
        for i in range(y, len(column)):
            if i != y and tree <= column[i]:
                viewed_trees[3] += 1
                smaller = False
                break
            if i != y:
                viewed_trees[3] += 1
        if smaller:
            seen = True
        if seen:
            visible_tree += 1
        score = 1
        for viewed_tree in viewed_trees:
                score *= viewed_tree
        tree_score.append(score)

print(sorted(tree_score, reverse=True))
print(visible_tree)
