from datetime import datetime

def extract_date_parts(datetime_obj):
    # Return the components directly
    return datetime_obj.year, datetime_obj.month, datetime_obj.day 

# Sample datetime object
dt = datetime(2022, 12, 25)

# Call the function and unpack the results
year, month, day = extract_date_parts(dt)

# Verification
print(f"Year: {year}, Month: {month}, Day: {day}")