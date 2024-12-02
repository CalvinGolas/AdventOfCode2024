# Takes in a file with two lists, returns difference between the values once they've been ordered
import bisect


def find_location_distance_diff(list_file: str) -> int:
    # Read in both lists
    file_reader = open(list_file, "r")

    list_a = []
    list_b = []

    while file_reader.readable():
        line = file_reader.readline()
        if line == "":
            break
        split_point = line.find("   ")
        location_a, location_b = line[:split_point], line[split_point + 3 :]
        # Order them as they're added to each list
        bisect.insort(list_a, int(location_a))
        bisect.insort(list_b, int(location_b))

    # Return the difference between the two lists
    list_diff = 0
    for i in range(0, len(list_a)):
        list_diff += abs(list_a[i] - list_b[i])
    return list_diff


if __name__ == "__main__":
    location_diff = find_location_distance_diff("locations.txt")
    print(f"The difference between the two lists is {location_diff}")
