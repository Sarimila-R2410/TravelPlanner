import heapq
from tabulate import tabulate

# Func to create a graph of destinations and travel details
def build_travel_map(destinations, travel_info):
    travel_map = {}
    for destination in destinations:
        travel_map[destination] = []
    for origin, destination, info in travel_info:
        travel_map[origin].append((destination, info))
        travel_map[destination].append((origin, info))
    return travel_map

# Func to find the shortest path between two destinations
def get_shortest_path(travel_map, start_point, end_point):
    priority_queue = [(0, start_point, [])]
    visited_points = set()

    while priority_queue:
        (current_cost, current_point, path) = heapq.heappop(priority_queue)
        if current_point in visited_points:
            continue
        path = path + [current_point]
        visited_points.add(current_point)

        if current_point == end_point:
            return path, current_cost

        for next_point, info in travel_map[current_point]:
            if next_point not in visited_points:
                heapq.heappush(priority_queue, (current_cost + info['time'], next_point, path))

    return None, float('inf')


# Func to display travel information in a table format
def display_travel_info(travel_info):
    info_data = []
    for origin, destination, info in travel_info:
        info_data.append([origin, destination, info['time'], info['mode'], info['price']])

    headers = ["Origin", "Destination", "Travel Time (mins)", "Mode of Transport", "Cost ($)"]
    return tabulate(info_data, headers, tablefmt="grid")



def main():
    destinations = [
        'Loguetown', 'Alabasta', 'Skypiea', 'Water 7', 'Enies Lobby',
        'Marineford', 'Dressrosa', 'Whole Cake Island'
    ]

    travel_info = [
        ('Loguetown', 'Alabasta', {'time': 150, 'mode': 'Ship', 'price': 20}),
        ('Alabasta', 'Skypiea', {'time': 200, 'mode': 'Airship', 'price': 50}),
        ('Skypiea', 'Water 7', {'time': 180, 'mode': 'Ship', 'price': 40}),
        ('Water 7', 'Enies Lobby', {'time': 30, 'mode': 'Boat', 'price': 10}),
        ('Enies Lobby', 'Marineford', {'time': 100, 'mode': 'Ship', 'price': 30}),
        ('Marineford', 'Dressrosa', {'time': 250, 'mode': 'Ship', 'price': 60}),
        ('Dressrosa', 'Whole Cake Island', {'time': 180, 'mode': 'Ship', 'price': 45}),
    ]
    travel_map = build_travel_map(destinations, travel_info)
    start_point = input("Enter the starting point (e.g., Loguetown): ")
    end_point = input("Enter the destination (e.g., Whole Cake Island): ")

    path, total_time = get_shortest_path(travel_map, start_point, end_point)

    if path:
        print(f"\nShortest route from {start_point} to {end_point}:")
        print(" -> ".join(path))
        print(f"Total travel time: {total_time} minutes")
    else:
        print("No route found!")

    print("\nTravel Information Table:")
    print(display_travel_info(travel_info))

if __name__ == "__main__":
    main()



