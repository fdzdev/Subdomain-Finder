# Subdomain Enumeration Script

This Python script automates subdomain enumeration for a list of domains using `assetfinder` and `subfinder`. It processes a list of domains from a file, enumerates subdomains for wildcard entries (e.g., `*.example.com`), removes duplicates, prepends `http://` to each domain, and saves the results to an output file.

## Features
- Enumerates subdomains using `assetfinder` and `subfinder`.
- Handles both wildcard domains (e.g., `*.example.com`) and regular domains (e.g., `example.com`).
- Removes duplicate entries and filters out invalid domains.
- Adds `http://` to each domain for compatibility with web tools.
- Saves results to a specified output file (`all_domains.txt` by default).

## Prerequisites
Before using this script, ensure you have the following installed:
1. **Python 3.x** - The script is written in Python 3.
2. **`assetfinder`** - A tool for finding subdomains. Install it via:
   > go install github.com/tomnomnom/assetfinder@latest
   >
   > Ensure it’s in your system’s PATH.
3. **`subfinder`** - Another subdomain enumeration tool. Install it via:
   > go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest
   >
   > Ensure it’s in your system’s PATH.

## Installation
1. Clone this repository to your local machine:
   > git clone https://github.com/fdzdev/Subdomain-Finder.git
   >
   > cd Subdomain-Finder
2. Ensure the prerequisites (Python, `assetfinder`, and `subfinder`) are installed.

## Usage
1. **Prepare your domain list**:
   - Create a file named `domains.txt` in the same directory as the script.
   - Add one domain per line. For example:
     > example.com
     > *.tesla.com
     > *.nasa.gov
     >
     > test.com
   - Wildcard domains (e.g., `*.example.org`) will trigger subdomain enumeration.

2. **Run the script**:
   - Open a terminal in the script’s directory and execute:
     > python3 mark.py

3. **Monitor the output**:
   - The script will:
     - Display the total number of domains and wildcard domains.
     - Enumerate subdomains for each wildcard entry using `assetfinder` and `subfinder`.
     - Save the results to `all_domains.txt`.

4. **Check the results**:
   - Open `all_domains.txt` to see the list of unique domains with `http://` prepended.

## Configuration
You can customize the following variables at the top of the script:
- `DOMAIN_LIST_FILE`: Change the input file name (default: `domains.txt`).
- `OUTPUT_FILE`: Change the output file name (default: `all_domains.txt`).
- `COMMAND_TIMEOUT`: Adjust the timeout for each tool’s execution (default: 60 seconds).

Example modification:
   > DOMAIN_LIST_FILE = "my_domains.txt"
   >
   > OUTPUT_FILE = "results.txt"
   >
   > COMMAND_TIMEOUT = 120

## Example Output
If `domains.txt` contains:
   > example.com
   >
   > *.test.com

The script might produce `all_domains.txt` with:
   > http://example.com
   >
   > http://sub1.test.com
   >
   > http://sub2.test.com
   >
   > http://test.com

## Notes
- Ensure `assetfinder` and `subfinder` are in your PATH, or the script will fail to execute those commands.
- The script handles timeouts and errors gracefully, printing warnings if a command fails or times out.
- Interrupt the script with `Ctrl+C` if needed; it will exit cleanly.

## Troubleshooting
- **"Command failed" errors**: Verify that `assetfinder` and `subfinder` are installed and accessible in your terminal.
- **"Domain list file not found"**: Ensure `domains.txt` (or your custom input file) exists in the script’s directory.
- **No subdomains found**: Check that your tools are properly configured and that the target domains support enumeration.

## License
[Insert your license here, e.g., MIT, GPL, etc.]

## Contributing
Feel free to submit issues or pull requests to improve this script!
