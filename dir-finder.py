import requests
from concurrent.futures import ThreadPoolExecutor

def brute_force_directories(url, wordlist):
    with open(wordlist, 'r') as file:
        directories = file.read().splitlines()

    def check_directory(directory):
        response = requests.get(url + directory)
        if response.status_code == 200:
            print(f"Found directory: {url + directory}")

    with ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(check_directory, directories)

if __name__ == "__main__":
    url = input("Enter the base URL: ")
    wordlist = input("Enter the path to the wordlist: ")
    brute_force_directories(url, wordlist)
