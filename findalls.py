import re

log_line = "From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"

# The pattern captures the domain name
# It looks for characters that are NOT a space (\S+)
# that immediately follow the '@' symbol.
pattern = r'@(\S+)'

matches = re.findall(pattern, log_line)

# The result is a list containing the matched domain
# In this case, ['uct.ac.za']
extracted_domain = matches[0] if matches else None

print(f"The extracted domain is: {extracted_domain}")