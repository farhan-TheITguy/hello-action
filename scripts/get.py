# Usage 
# python get.py --deployment-type site
# Output: site:1A3B5C

# python get.py --deployment-type supersite
# Output: supersite:4D6E7F

import argparse
import random
import string

def generate_hex_prefix(deployment_type):
    # Generate a random 6-character hexadecimal string
    hex_chars = string.hexdigits.upper()  # Use uppercase hexadecimal characters
    prefix = ''.join(random.choice(hex_chars) for _ in range(6))
    
    # Add the deployment type as the prefix
    if deployment_type == "site":
        return prefix
    elif deployment_type == "supersite":
        return prefix
    else:
        return "Invalid deployment type. Use 'site' or 'supersite'."

if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Generate a random hexadecimal prefix for a deployment type.")
    parser.add_argument("--deployment-type", required=True, choices=["site", "supersite"], help="Type of deployment: site or supersite.")
    
    # Parse arguments
    args = parser.parse_args()
    
    # Generate and print the prefix
    result = generate_hex_prefix(args.deployment_type)
    print(result)