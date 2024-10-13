import subprocess
import os

# Set the path to your domain list file
DOMAIN_LIST_FILE = "domains.txt"

# Set the output file name
OUTPUT_FILE = "all_domains.txt"

# Set the timeout for each command (in seconds)
COMMAND_TIMEOUT = 60


def run_command(command):
    try:
        result = subprocess.run(
            command,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=COMMAND_TIMEOUT,
        )
        if result.returncode != 0:
            print(f"Command failed: {command}\nError: {result.stderr}")
        return result.stdout.splitlines()
    except subprocess.TimeoutExpired:
        print(f"Command timed out: {command}")
        return []


# Use both assetfinder + subfinder
# Imp
def enumerate_subdomains(root_domain):
    assetfinder_command = f"assetfinder {root_domain}"
    subfinder_command = f"subfinder -d {root_domain}"

    subdomains = set()
    subdomains.update(run_command(assetfinder_command))
    subdomains.update(run_command(subfinder_command))

    return subdomains


def main():
    if not os.path.exists(DOMAIN_LIST_FILE):
        print(f"Domain list file not found: {DOMAIN_LIST_FILE}")
        return

    with open(DOMAIN_LIST_FILE, "r") as file:
        domains = [line.strip() for line in file]

    total_domains = len(domains)
    wildcard_domains = [domain for domain in domains if domain.startswith("*.")]
    num_wildcard_domains = len(wildcard_domains)

    print(f"Total number of domains: {total_domains}")
    print(f"Number of domains starting with '*.': {num_wildcard_domains}")

    all_domains = set()
    counter = 1

    for domain in domains:
        if domain.startswith("*."):
            root_domain = domain[2:]
            print(f"{counter}. Enumerating subdomains for: {root_domain}")
            subdomains = enumerate_subdomains(root_domain)
            all_domains.update(subdomains)
            counter += 1
        else:
            all_domains.add(domain)

    # Remove duplicates and add 'http://' to each domain
    unique_domains = {f"http://{domain}" for domain in all_domains if domain}

    # Filter out any domains that start with '*.'
    unique_domains = {
        domain for domain in unique_domains if not domain.startswith("http://*")
    }

    with open(OUTPUT_FILE, "w") as file:
        for domain in sorted(unique_domains):
            file.write(domain + "\n")

    print(f"Subdomain enumeration complete. Results saved to {OUTPUT_FILE}")
    print(f"Total number of unique domains: {len(unique_domains)}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nScript interrupted by user. Exiting...")
