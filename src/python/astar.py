import heapq
from TreeNode import TreeNode
# from map_node import map_node


def manhattan_distance(origin: tuple[int, int], dst: tuple[int, int]) -> int:
    distance = abs(origin[0] - dst[0]) + abs(origin[1] - dst[1])
    return distance


def get_available_neighbors(map, pos : tuple[int, int]) -> list:
    north_neighbor = (pos[0], pos[1] + 1)
    south_neighbor = (pos[0], pos[1] - 1)
    east_neighbor = (pos[0] + 1, pos[1])
    west_neighbor = (pos[0] - 1, pos[1])

    valid_neighbors = []
    if north_neighbor in map:
        valid_neighbors.append(north_neighbor)
    if south_neighbor in map:
        valid_neighbors.append(south_neighbor)
    if east_neighbor in map:
        valid_neighbors.append(east_neighbor)
    if west_neighbor in map:
        valid_neighbors.append(west_neighbor)

    return valid_neighbors


def reconstruct_path(dst: TreeNode) -> list[tuple[int, int]]:
    path = []

    curr_node = dst
    while curr_node:
        path.insert(0, curr_node.get_coord())
        curr_node = curr_node.get_parent()

    return path


# def get_route(path: list) -> list[tuple[int, int]]:
#     total_path = []
#     curr_pos = map_start_pos()

#     map = get_map()

#     for i in path:
#         total_path += pathfinder(map, curr_pos, map_find_gym(i))[0]
#         curr_pos = map_find_gym(i)

#     total_path += pathfinder(map, curr_pos, map_end_pos())[0]
#     return total_path


def astar(map, origin: tuple[int, int], dst: tuple[int, int]) -> tuple[list, int]:
    origin_node = TreeNode(origin, 0, manhattan_distance(origin, dst))

    border = [(origin_node.get_value_gx(), origin_node)]
    visited = []

    while border:
        current_node = heapq.heappop(border)[1]
        current_cord = current_node.get_coord()

        if current_cord in visited:
            continue

        if current_cord == dst:
            return reconstruct_path(current_node)

        visited.append(current_cord)

        neighbors = get_available_neighbors(map, current_cord)
        for neighbor in neighbors:
            if neighbor in visited:
                continue

            neighbor_cost = 1 + current_node.get_priority()
            neighbor_dist = manhattan_distance(neighbor, dst)
            neighbor_parent = current_node

            neighbor_node = TreeNode(neighbor, neighbor_cost, neighbor_dist)
            neighbor_node.set_parent(neighbor_parent)

            heapq.heappush(border, (neighbor_dist, neighbor_node))

    return [], 0
