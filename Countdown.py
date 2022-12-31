#NewYearCountdown2023 
#Copyright by Jimmy Majumder
#Robotics Engineer @Qibitech Inc., Japan 
#Founder of Bangladesh Advance Robotics research center 
#https://barrc-bd.com/ 


import datetime

# Get the current time Zoon example: BD timezone
#use your GMT time integer like JST = 9
current_time = datetime.datetime.now(datetime.timezone.utc).astimezone(datetime.timezone(datetime.timedelta(hours=6))) 
# Set the target time for New Year's Day 2023 in BD timezone 
# #use your GMT time integer value like JST = 9 
Happy_New_Year_2023 = datetime.datetime(2023, 1, 1, tzinfo=datetime.timezone(datetime.timedelta(hours= 6))) 

# Calculate the time remaining until the new year 2023
time_remaining = Happy_New_Year_2023 - current_time

# Print the remaining time <00.00>    
print(f"Happy New year: {time_remaining} & Will you marry me?")  

# create a loop to update and display the time remaining every second
while time_remaining.total_seconds() > 0:

    # Get the current time in BD timezone 
    #use your GMT time integer value like JST = 9 
    current_time = datetime.datetime.now(datetime.timezone.utc).astimezone(datetime.timezone(datetime.timedelta(hours=6))) 

    # Calculate the time remaining until the new year
    time_remaining = Happy_New_Year_2023 - current_time

    # Print the updated remaining time
    print(f"Let's Countdown <Happy New Year>: {time_remaining} \n I love You. Will you marry me, My Love?") 
    
