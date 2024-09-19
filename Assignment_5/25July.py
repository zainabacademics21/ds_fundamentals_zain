def read_csv_file(file_path):
    data = []
    with open(file_path, 'r') as file:
        # Read subsequent rows
        for line in file:
            # Remove any leading/trailing whitespace and split by comma
            fields = line.strip().split(',')
            data.append(fields)
    return data

# Function to convert date string to a comparable tuple (year, month, day)
def convert_date(date_str):
    day, month, year = map(int, date_str.split('-'))
    return (year, month, day)

def calculation(data, from_date, to_date):
    filtered_data = []
    
    # Convert from_date and to_date to tuples for comparison
    from_date_tuple = convert_date(from_date)
    to_date_tuple = convert_date(to_date)
    
    for row in data:
        date_str = row[0]  # Assuming date is the first column in your CSV
        row_date_tuple = convert_date(date_str)
        
        # Compare dates using tuples
        if from_date_tuple <= row_date_tuple <= to_date_tuple:
            filtered_data.append(row)
    
    return filtered_data

def calculate_average_calories_per_day(filtered_data):
    daily_calories = {}
    
    for row in filtered_data:
        date_str = row[0]  # Assuming date is the first column in your CSV
        calories = int(row[1])  # Assuming calories is the second column in your CSV
        
        if date_str in daily_calories:
            daily_calories[date_str].append(calories)
        else:
            daily_calories[date_str] = [calories]
    
    average_calories_per_day = {}
    
    for date, calories_list in daily_calories.items():
        average_calories = sum(calories_list) / len(calories_list)
        average_calories_per_day[date] = average_calories
    
    return average_calories_per_day

def calculate_average_calories_in_range(filtered_data):
    total_calories = 0
    count = 0
    
    for row in filtered_data:
        calories = int(row[1])  # Assuming calories is the second column
        total_calories += calories
        count += 1
    
    if count > 0:
        average_calories = total_calories / count
        return average_calories
    else:
        return None

def calculate_highest_calories_in_range(filtered_data):
    max_calories = 0
    for row in filtered_data:
        calories = int(row[1])  # Assuming calories is the second column
        if calories > max_calories:
            max_calories = calories
    
    return max_calories

def calculate_standard_deviation(filtered_data):
    calories_list = []
    for entry in filtered_data:
        calories_list.append(int(entry[1]))  # Assuming calories is the second column
    
    if len(calories_list) > 1:
        mean = sum(calories_list) / len(calories_list)
        variance = sum((x - mean) ** 2 for x in calories_list) / len(calories_list)
        standard_deviation = variance ** 0.5
        return standard_deviation
    else:
        return None

def find_highest_calories_per_day(filtered_data):
    daily_calories = {}
    
    # Group calories by date
    for row in filtered_data:
        date_str = row[0]  # Assuming date is the first column in your CSV
        calories = int(row[1])  # Assuming calories is the second column in your CSV
        
        if date_str in daily_calories:
            daily_calories[date_str].append(calories)
        else:
            daily_calories[date_str] = [calories]
    
    # Find maximum calories per day
    highest_calories_per_day = {}
    
    for date, calories_list in daily_calories.items():
        max_calories = max(calories_list)
        highest_calories_per_day[date] = max_calories
    
    return highest_calories_per_day

def input_valid_date(prompt):
    while True:
        date_str = input(f"{prompt} (DD-MM-YYYY): ")
        # Validate the input date format
        if len(date_str) == 10 and date_str[2] == '-' and date_str[5] == '-':
            return date_str
        else:
            print("Invalid date format. Please enter in DD-MM-YYYY format.")

def main():
    file_path = 'data_sample.csv'  # Replace with your actual file path
    data = read_csv_file(file_path)
    
    from_date = input_valid_date("From Date")
    to_date = input_valid_date("To Date")
    
    filtered_data = calculation(data, from_date, to_date)
    
    # Display data of selected range of dates
    average_calories_per_day = calculate_average_calories_per_day(filtered_data)
    highest_calories_per_day = find_highest_calories_per_day(filtered_data)
    standard_deviation = calculate_standard_deviation(filtered_data)
    range_highest_calories=calculate_highest_calories_in_range(filtered_data)
    range_average=calculate_average_calories_in_range(filtered_data)

    print(f"Data from {from_date} to {to_date}:")
    for date, avg_calories in average_calories_per_day.items():
        print(f"Date: {date}, Average Calories: {avg_calories:.2f}")
    
    for date, max_calories in highest_calories_per_day.items():
        print(f"Date: {date}, Highest Calories: {max_calories}")

    if standard_deviation is not None:
        print(f'Standard deviation of calories from {from_date} to {to_date}: {standard_deviation:.2f}')

    if range_highest_calories is not None:
        print(f'Highest Calories consumed between {from_date} to {to_date}: {range_highest_calories:.2f}')

    if range_average is not None:
        print(f'Average Calories consumed between {from_date} to {to_date}: {range_average}')
    else:
        print("no data")
if __name__ == "__main__":
    main()