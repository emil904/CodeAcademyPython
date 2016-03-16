def count(sequence, item):
    counter = 0
    for i in sequence:
        if item == i:
            counter += 1
    return counter