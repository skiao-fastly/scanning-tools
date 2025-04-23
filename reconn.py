#!/usr/bin/python3
import os

# Prompt the user for the tool choice
print("Select a tool to run:")
print("1. Nmap")
print("2. Gobuster")
print("3. FFUF")
print("4. Subfinder")

tool_choice = input("Please choose the tool: ")

# Prompt the user for the URL
url = input("Enter the URL to scan or IP for nmap: ")

# Prompt the user for the wordlist file path
wordlist_file = "~/Documents/Tools/SecLists/Discovery/Web-Content/common.txt"

# Construct the command based on the tool choice
if tool_choice.lower() == "1":
    command = f"nmap -sV -Pn {url} -oA nmapscan"
    os.system(command)
elif tool_choice.lower() == "2":
    command = f"gobuster dir -u {url} -w {wordlist_file} --output dirbuster.txt"
    os.system(command)
elif tool_choice.lower() == "3":
    command = f"ffuf -u {url}/FUZZ -w {wordlist_file}"
    os.system(command)
elif tool_choice.lower() == "4":
    command1 = f"subfinder -d {url} -output subdomains.txt"
    command2 = f"docker run --rm -i -v $PWD:/data httpx -silent -status-code -mc 200,301 < subdomains.txt > live-subdomains.txt"
    os.system(command1)
    os.system(command2)
else:
    print("Invalid tool choice. Please enter 'gobuster' or 'ffuf'.")
    exit()