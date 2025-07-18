# Vinted Scraper

This Python script is a simple, command-line based tool to automatically scrape the Vinted website for new items based on a specific search query. It's designed to run continuously, checking for new listings at a set interval and saving the results to a CSV file.

## Features

*   **Continuous Monitoring:** The script runs in an infinite loop to periodically check for new items.
*   **Specific Search:** You can easily configure the script to search for any item you are interested in.
*   **Duplicate Prevention:** It keeps track of items that have already been found to avoid adding them to the results file again.
*   **CSV Output:** Neatly saves the found items' title, price, and URL into a CSV file for easy viewing and processing.
*   **Cookie Management:** Automatically fetches the necessary cookies from Vinted to make successful API requests.

## Requirements

*   Python 3.x
*   The `requests` library

## Installation

1.  Make sure you have Python 3 installed on your system.
2.  Clone this repository or download the `vinted.py` script.
3.  Install the required `requests` library using pip:
    ```sh
    pip install requests
    ```

## Configuration

Before running the script, you can customize its behavior by changing the following variables at the top of the `vinted.py` file:

*   `SCRAPE_DELAY`: The time in seconds between each check for new items. The default is `60 * 5` (300 seconds, or 5 minutes).
    ```python
    SCRAPE_DELAY = 60 * 5 # in secs
    ```
*   `SEARCH_QUERY`: The search term for the items you want to find on Vinted.
    ```python
    SEARCH_QUERY = "timex marlin"
    ```
*   `CSV_FILE_NAME`: The name of the file where the results will be saved.
    ```python
    CSV_FILE_NAME = "items.csv"
    ```

## Usage

1.  Open your terminal or command prompt.
2.  Navigate to the directory where you saved the `vinted.py` script.
3.  Run the script with the following command:
    ```sh
    python vinted.py
    ```
4.  The script will start running. It will print messages to the console when it successfully scrapes the site or when it finds a new item.
5.  To stop the script, press `Ctrl+C` in the terminal.

## How It Works

The script works by making requests to Vinted's internal API to get a list of items that match the `SEARCH_QUERY`. It mimics a real user by including necessary headers and cookies in its requests.

When a new item is found (one that isn't already in the `links` list or the CSV file), its title, price, and a direct link to the item page are printed to the console and appended as a new line in the specified CSV file.

## Output

### Console Output
When a new item is found, you will see a message like this in your terminal:

```
Found: Orologio Timex Marlin Automatic
    At: 150.00
    https://vinted.it/items/12345678-orologio-timex-marlin-automatic
```

### CSV File
A file named `items.csv` (or your custom name) will be created in the same directory. It will store the data in the following format:

```csv
title,price,url
Watch,95.50,https://vinted.it/items/87654321-watch
```

## Disclaimer

This script is for personal and educational use only. Web scraping may be against the terms of service of Vinted. Use this script responsibly and at your own risk. The author is not responsible for any consequences of its use.
