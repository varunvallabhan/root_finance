# root_finance
Root_coding_test

Problem Statement-
Given a text file, where each line of the input file starts with a command. One of the commands is Driver, which registers a new driver in the app. The second command is Trip, which will record a trip attributed to a driver.
limiting conditions-Discard any trips that average a speed of less than 5 mph or greater than 100 mph.

We have to generate a report containing each driver with total miles driven and average speed sorted by most miles driven to least. Miles and miles per hour are to be rounded to the nearest integer.

TO run the code-

1. download the file.
2. In command prompt navigate to the folder where you have downloaded the file and type= python root.py your_file_name.txt(this needs to be a text file)
It would print the summary.

The logic and thought process.

For the test input file I tried to generalise it by adding blank line and drivers and trips are added randomly.

To handle this stream of data where the trips can be counted no matter when they come in the file and they would be updated if there is an entry for the driver. If the driver is not present then the trip details associated with them are ignored.

Dictionaries are easier to update for a given a known key. Hence, the drivers are updated as a dictionary. 

Trips corresponding to each driver is then updated by fetching each trip detail and looking for the driver. If we can remove the generalisation where trips and drivers can be generated randomly then then we can merge this step with the splitting step and reduce a for loop by updating the trips while reading the file itself. It's an additional feature that is not asked but i felt its important as drivers can enroll at any point or the file can be shuffled etc due to network lag or other factors.

The trip summary function uses a simple relation between speed, time, miles to calculate the desired parameters and rounds them where ever needed. Also, as requested trips above 100mph and below 5mph are discarded. The final average speed is the weighted average with wrt to time.

The print function just prints the values in the desired format.

For functionality of each block look at the comments in the code.
