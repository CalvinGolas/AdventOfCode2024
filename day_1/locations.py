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
        location_a, location_b = split_line_locations(line)
        # Order them as they're added to each list
        bisect.insort(list_a, int(location_a))
        bisect.insort(list_b, int(location_b))

    # Return the difference between the two lists
    list_diff = 0
    for i in range(0, len(list_a)):
        list_diff += abs(list_a[i] - list_b[i])
    return list_diff


def find_similarity_score(list_file: str) -> int:
    # Construct hashmap where keys are list_a
    loc_frequencies = {}
    file_reader = open(list_file, "r")

    list_b_locations = []
    while file_reader.readable():
        line = file_reader.readline()
        if line == "":
            break
        location_a, location_b = split_line_locations(line)
        loc_frequencies[location_a] = 0
        list_b_locations.append(location_b)

    # Iterate through list_b and increment frequency to dict constructed from list_a
    for loc in list_b_locations:
        if loc in loc_frequencies:
            loc_frequencies[loc] += 1

    # Find total value from list
    total_value = 0
    for key in loc_frequencies:
        total_value += int(key) * loc_frequencies[key]
    return total_value


def split_line_locations(line: str) -> tuple:
    split_point = line.find("   ")
    return int(line[:split_point]), int(line[split_point + 3 :])


if __name__ == "__main__":
    location_diff = find_location_distance_diff("locations.txt")
    print(f"The difference between the two lists is {location_diff}")

    similarity_score = find_similarity_score("locations.txt")
    print(f"The similarity score between the two lists is {similarity_score}")
