def find_valid_reports_in_file(report_file: str) -> int:
    report_reader = open(report_file, "r")
    safe_report_count = 0
    while report_reader.readable():
        report = report_reader.readline()
        if report == "":
            break
        if evaluate_report(report):
            safe_report_count += 1

    return safe_report_count


# Report is valid if it is fully increasing/decreasing with defference between each value in range 1->3 inclusive
def evaluate_report(report_str: str) -> bool:
    # Split string into list
    report = report_str.split()
    previous_val = int(report.pop())
    # determine first increase/decrease
    is_increasing = previous_val < int(report[0])
    while len(report) > 0:
        curr_val = int(report.pop())
        val_diff = abs(curr_val - previous_val)

        if is_increasing:
            if previous_val > curr_val:
                return False
        elif previous_val < curr_val:
            return False

        if val_diff < 1 or val_diff > 3:
            return False
        previous_val = curr_val
    # iterate through rest of list
    return True


if __name__ == "__main__":
    safe_reports = find_valid_reports_in_file("reports.txt")
    print(f"Number of safe reports: {safe_reports}")
