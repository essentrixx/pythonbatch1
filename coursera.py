import re
import urllib.request

# Option 1: Read from URL
url = 'http://py4e-data.dr-chuck.net/regex_sum_2339375.txt'
try:
    # Read the file from the URL
    with urllib.request.urlopen(url) as response:
        data = response.read().decode('utf-8')
    
    # Find all numbers using regex
    numbers = re.findall('[0-9]+', data)
    
    # Convert strings to integers and sum them
    total = sum(int(num) for num in numbers)
    
    print(f"Count of numbers: {len(numbers)}")
    print(f"Sum: {total}")
    
except Exception as e:
    print(f"Error reading from URL: {e}")
    print("\nTrying to read from local file instead...")
    
    # Option 2: Read from local file (if downloaded)
    try:
        filename = input("Enter file name: ")
        with open(filename, 'r') as file:
            data = file.read()
        
        # Find all numbers using regex
        numbers = re.findall('[0-9]+', data)
        
        # Convert strings to integers and sum them
        total = sum(int(num) for num in numbers)
        
        print(f"Count of numbers: {len(numbers)}")
        print(f"Sum: {total}")
        
    except FileNotFoundError:
        print(f"File '{filename}' not found!")
    except Exception as e:
        print(f"An error occurred: {e}")


# Alternative compact version:
# import re
# import urllib.request
# 
# url = 'http://py4e-data.dr-chuck.net/regex_sum_2339375.txt'
# data = urllib.request.urlopen(url).read().decode('utf-8')
# numbers = re.findall('[0-9]+', data)
# print(sum(int(num) for num in numbers))