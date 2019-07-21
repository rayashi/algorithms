
def get_total_machring_pairs(sockets: [int]) -> int:
    machting_pairs = 0
    colors = {}
    for socket in sockets:
        try:
            colors[socket] += 1
        except KeyError:
            colors[socket] = 1

    for count in colors.values():
        machting_pairs += count // 2

    return machting_pairs
