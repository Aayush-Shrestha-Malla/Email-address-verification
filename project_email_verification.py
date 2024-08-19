import re

email = input("Enter your email address: ")

# Basic length check
if len(email) >= 6:
    # First character must be a letter
    if email[0].isalpha():
        # Check for exactly one "@" and at least one "."
        if email.count("@") == 1:
            local_part, domain = email.split("@")
            
            # Check if local part and domain part have valid lengths
            if len(local_part) > 0 and len(domain) > 3:
                # Check if domain contains exactly one "."
                if domain.count(".") == 1:
                    domain_name, extension = domain.split(".")
                    
                    # Check if domain name and extension are valid
                    if domain_name.isalnum() and extension.isalpha() and (len(extension) == 2 or len(extension) == 3):
                        # Additional checks using regular expressions
                        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
                        if re.match(pattern, email):
                            print("Valid email address")
                        else:
                            print("Invalid email format")
                    else:
                        print("Invalid domain or extension")
                else:
                    print("Domain must contain exactly one '.'")
            else:
                print("Local part or domain part is invalid")
        else:
            print("Invalid email: '@' should appear exactly once")
    else:
        print("Invalid email: The first character must be a letter")
else:
    print("Invalid email: Length should be at least 6 characters")
