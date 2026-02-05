# Scrape all Emails from Domain

OS: any
Security Domains: Reconnaissance (https://www.notion.so/Reconnaissance-1434c8e5237680fe960be92e51e13491?pvs=21)
Target_Technology: Web (https://www.notion.so/Web-2f44c8e5237680fdb8badd976a14f751?pvs=21)

```jsx
import requests
import re
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from collections import deque

# Configuration
BASE_URL = "http://IP_OF_TARGET"
OUTPUT_FILE = "usernames.txt"

# Regex for extracting email addresses
EMAIL_REGEX = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

def get_emails_from_text(text):
    """Finds all email addresses in a string using regex."""
    return set(re.findall(EMAIL_REGEX, text))

def is_internal_link(url, base_domain):
    """Checks if a URL belongs to the same domain/IP."""
    parsed_url = urlparse(url)
    parsed_base = urlparse(base_domain)
    return parsed_url.netloc == parsed_base.netloc or parsed_url.netloc == ''

def crawl_and_extract(start_url):
    """Crawls the website and extracts emails."""
    visited_urls = set()
    urls_to_visit = deque([start_url])
    all_emails = set()

    print(f"Starting crawl at: {start_url}")

    while urls_to_visit:
        current_url = urls_to_visit.popleft()

        if current_url in visited_urls:
            continue

        print(f"Scanning: {current_url}")
        
        try:
            response = requests.get(current_url, timeout=5)
            response.raise_for_status() # Raise error for bad status codes (404, 500)
            
            # 1. Extract Emails from the current page content
            emails = get_emails_from_text(response.text)
            if emails:
                print(f"  -> Found {len(emails)} email(s)")
                all_emails.update(emails)

            # 2. Parse HTML to find new links
            soup = BeautifulSoup(response.text, 'html.parser')
            
            for link in soup.find_all('a', href=True):
                href = link['href']
                
                # specific excludes (optional, to avoid mailto links or anchors)
                if href.startswith('mailto:') or href.startswith('#'):
                    continue

                # Construct absolute URL
                absolute_url = urljoin(current_url, href)
                
                # Clean URL (remove query parameters/fragments to avoid duplicates)
                parsed = urlparse(absolute_url)
                clean_url = f"{parsed.scheme}://{parsed.netloc}{parsed.path}"

                # Only add if internal and not visited
                if is_internal_link(clean_url, start_url) and clean_url not in visited_urls:
                    if clean_url not in urls_to_visit:
                        urls_to_visit.append(clean_url)

            visited_urls.add(current_url)

        except requests.exceptions.RequestException as e:
            print(f"  -> Error fetching {current_url}: {e}")
            visited_urls.add(current_url) # Mark as visited to avoid retrying

    return all_emails

def save_emails(emails, filename):
    """Saves a set of emails to a file."""
    try:
        with open(filename, 'w') as f:
            for email in sorted(emails):
                f.write(email + '\n')
        print(f"\nSuccess! {len(emails)} unique emails saved to {filename}")
    except IOError as e:
        print(f"Error writing to file: {e}")

if __name__ == "__main__":
    found_emails = crawl_and_extract(BASE_URL)
    save_emails(found_emails, OUTPUT_FILE)
```