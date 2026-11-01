# Import libraries needed for the web scraper
import requests
import csv
import time

# Allows multiple web requests to run concurrently
from concurrent.futures import ThreadPoolExecutor

# Base URL for the official Hacker News API
BASE_URL = "https://hacker-news.firebaseio.com/v0/"

# Retrieve the IDs of the top 30 Hacker News stories
def get_story_ids():

    # Send a request to the Hacker News API
    response = requests.get(
        BASE_URL + "topstories.json",
        timeout=10
    )

    # Check if the request was successful
    response.raise_for_status()

    # Return the first 30 story IDs
    return response.json()[:30]
  
# Retrieve information about an individual story
def get_story(story_id):

    # Create the API URL using the story ID
    response = requests.get(
        BASE_URL + f"item/{story_id}.json",
        timeout=10
    )
  
    # Check if the request was successful
    response.raise_for_status()

    # Convert the response into Python data
    return response.json()

# Extract useful information from a story
def extract_story(story):

    # Organize the story information into a dictionary
    return {
        "Title": story.get("title", "No title"),
        "Author": story.get("by", "Unknown"),
        "Points": story.get("score", 0),
        "Comments": story.get("descendants", 0),
        "URL": story.get("url", "No external link"),

        # Create a link to the Hacker News discussion
        "Hacker News URL": (
            f"https://news.ycombinator.com/item?id={story['id']}"
        )
    }

# Save the collected stories into a CSV file
def save_stories(stories):

    # Open a CSV file for writing
    with open(
        "hacker_news.csv",
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        # Define the CSV column names
        fieldnames = [
            "Title",
            "Author",
            "Points",
            "Comments",
            "URL",
            "Hacker News URL"
        ]

        # Create a CSV writer
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        # Write the column headings
        writer.writeheader()

        # Write the story information into the file
        writer.writerows(stories)

# Main function that performs the web scraping
def scrape_hacker_news():

    # Record the starting time to measure performance
    start = time.time()

    # Retrieve the IDs of the top stories
    story_ids = get_story_ids()

    # Retrieve multiple stories at the same time
    with ThreadPoolExecutor(max_workers=10) as executor:

        # Send requests concurrently for each story
        raw_stories = list(executor.map(get_story, story_ids))

    # Use filter to remove missing stories
    valid_stories = filter(
        lambda story: story is not None and "title" in story,
        raw_stories
    )

    # Use map to extract information from each story
    stories = map(extract_story, valid_stories)

    # Convert the results into a list
    results = list(stories)

    # Display the number of stories and execution time
    print("\nHACKER NEWS SCRAPER")
    print("-------------------")
    print(f"Stories collected: {len(results)}")
    print(f"Time elapsed: {time.time() - start:.2f} seconds")

    # Return the collected stories
    return results

# Main program that runs the scraper
def main():

    # Start scraping Hacker News
    stories = scrape_hacker_news()

    # Save the collected information
    save_stories(stories)

    # Confirm that the CSV file was created
    print("Results saved to hacker_news.csv")


# Execute the main function when the program is run
if __name__ == "__main__":
    main()
