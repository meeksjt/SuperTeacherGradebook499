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
    try:
        median = statistics.median(student_grades)
    except Exception:
        median = "No Median"
    return str(median)

"""
Function for the mean of the provided grades
Parameters:
    student_grades : list of final student grades (floats)
Returns:
    mean : mean of the dataset (string of a float)
"""
def calculate_mean(student_grades):
    try:
        mean = statistics.mean(student_grades)
    except Exception:
        mean = "No Mean"
    return str(mean)

"""
Function for the standard deviation of the provided grades
Parameters:
    student_grades : list of final student
Returns:
    std_dev : standard deviation of the dataset (string of a float) 
"""
def calculate_std_dev(student_grades):
    try:
        std_dev = statistics.stdev(student_grades)
    except:
        std_dev = "No Std. Dev"
    return std_dev
