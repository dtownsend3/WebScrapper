# Hacker News Web Scraper

## Project Description

This project is a Python web scraper that collects information from the Hacker News website using its public API.

The scraper retrieves the top 30 stories and collects their titles, authors, points, number of comments, and article links.

The collected information is saved into a CSV file called `hacker_news.csv`.

## Requirements

This project uses:

- Python 3
- Requests
- Concurrent Futures
- CSV
- Time

## Installation

Install the Requests library:

```bash
pip install requests
```

## How to Run

1. Download or clone this repository.
2. Open a terminal in the project folder.
3. Run the following command:

```bash
python scraper.py
```

4. The scraper will retrieve the top 30 Hacker News stories.
5. The results will be saved in `hacker_news.csv`.

## Functional Programming

This project uses functional programming concepts through Python's built-in `map()`, `filter()`, and `lambda` functions.

- `map()` applies the `extract_story()` function to each collected story.
- `filter()` removes stories that are missing a title.
- `lambda` provides a small function used to check whether a story contains a title.

These functions help organize the code and process information without needing additional loops. They do not automatically make the program faster, but they make data processing more organized and reusable.

## Concurrent Futures

This project uses `ThreadPoolExecutor` from Python's `concurrent.futures` library.

Instead of retrieving each Hacker News story one at a time, the scraper uses multiple threads to send requests concurrently.

This helps reduce the amount of time spent waiting for individual website requests to finish.

## Performance Impact

Using concurrent programming can improve the performance of this scraper because retrieving information from a website requires waiting for network responses.

By allowing multiple requests to happen at the same time, the program can collect information more efficiently than making every request sequentially.

Functional programming helps organize the processing of collected information through `map()` and `filter()`. However, these functions do not necessarily improve execution speed compared to other approaches.

The actual performance depends on network speed, server response times, and the number of requests being made.

## Screenshot
<img width="1917" height="908" alt="image" src="https://github.com/user-attachments/assets/644c3f83-8fb1-4c7b-85d2-fc157aa0eca8" />

## Website

[Hacker News](https://news.ycombinator.com/)

## API Documentation

[Hacker News API](https://github.com/HackerNews/API)
