# Usage 
# python release.py --deployment-type site --prefix 1A3B5C
# Output: Site prefix '1A3B5C' has been unlocked.

# python release.py --deployment-type supersite --prefix 4D6E7F
# Output: Supersite prefix '4D6E7F' has been unlocked.

import argparse

def unlock_prefix(deployment_type, prefix):
    if deployment_type == "site":
        print(f"Site prefix '{prefix}' has been unlocked.")
    elif deployment_type == "supersite":
        print(f"Supersite prefix '{prefix}' has been unlocked.")
    else:
        print("Invalid deployment type. Use 'site' or 'supersite'.")

if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Unlock a deployment prefix.")
    parser.add_argument("--deployment-type", required=True, choices=["site", "supersite"], help="Type of deployment: site or supersite.")
    parser.add_argument("--prefix", required=True, help="The prefix to unlock.")
    
    # Parse arguments
    args = parser.parse_args()
    
    # Unlock and print the result
    unlock_prefix(args.deployment_type, args.prefix)