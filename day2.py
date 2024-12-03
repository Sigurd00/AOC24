def process_input(input_file):
    numbers = []
    with open(input_file, 'r') as file:
        for line in file:
            numbers.append([int(number) for number in line.split(" ")])
    return numbers

def solve(reports, problem_dampener=0):
    sum_safe = 0
    for report in reports:
        if is_safe(report):
            sum_safe += 1
            continue
        
        if problem_dampener > 0:
            for i in range(len(report)):
                modified_report = report[:i] + report[i+1:]  # Remove the i-th level
                if is_safe(modified_report):
                    sum_safe += 1
                    break
    
    return sum_safe

def is_safe(report):
    if len(report) < 2:
        return True  # Trivially safe

    ord = None  # Positive for ascending, negative for descending
    for i in range(1, len(report)):
        step_size = report[i] - report[i - 1]
        
        # Check step size within range
        if abs(step_size) < 1 or abs(step_size) > 3:
            return False
        
        # Check for order violations
        if ord is None:
            ord = step_size
        elif (ord > 0 and step_size < 0) or (ord < 0 and step_size > 0):
            return False
    
    return True

if __name__ == "__main__":
    reports = process_input("inputs/day2.txt")
    result1 = solve(reports)
    result2 = solve(reports, 1)
    print(result1)
    print(result2)