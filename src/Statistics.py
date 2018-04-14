import statistics

"""
Function for the mode of the provided grades
Parameters:
    student_grades : list of final student grades (floats)
Returns:
    mode : mode of the dataset (string of a float)
"""
def calculate_mode(student_grades):
    try:
        mode = statistics.mode(student_grades)
    except statistics.StatisticsError:
        mode = "No Mode"
    return str(mode)

"""
Function for the median of the provided grades
Parameters:
    student_grades : list of final student grades (floats)
Returns:
    median : median of the dataset (string of a float)
"""
def calculate_median(student_grades):
    median = statistics.median(student_grades)
    return str(median)

"""
Function for the mean of the provided grades
Parameters:
    student_grades : list of final student grades (floats)
Returns:
    mean : mean of the dataset (string of a float)
"""
def calculate_mean(student_grades):
    mean = statistics.mean(student_grades)
    return str(mean)

"""
Function for the standard deviation of the provided grades
Parameters:
    student_grades : list of final student
Returns:
    std_dev : standard deviation of the dataset (string of a float) 
"""
def calculate_std_dev(student_grades):
    std_dev = statistics.stdev(student_grades)
    return std_dev


if __name__ == "__main__":
    mode_records = [1, 2, 4, 3, 5, 6, 7, 8]
    print(calculate_std_dev(mode_records))