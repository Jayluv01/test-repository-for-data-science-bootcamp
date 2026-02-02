# Website Traffic Analytics
#As a Data Analyst, your job is to analyze the website traffic data for an ecommerce site
# The marketing team needs to understand which pages users visist most frequently to optimize ad send or marketing strategy

# The problem
# You have a log of page visits from 50 users. you need to:
# 1. Count how many time each page was visited.
# 2. Find the most and least popular pages.
# 3. Calculate what percentage of traffic each page receives
# 4. Identify pages with low traffic that need promotion.

import random 

pages = ["products", "product profile", "about", "home", "checkout", "cart", "contact"]
users = 50

log_of_pages_visited = []

for person in range(users):
    rounds = random.randint(3, 20)
    for take in range(rounds):
        index = random.randint(0, 6)
        log_of_pages_visited.append(pages[index])

# Step 1: Count page visits
# Concept: Use dictionaries to count frequency - a fundamental data science task

page_counts = {}

for page in log_of_pages_visited:
    if page in page_counts: 
        page_counts [page] = page_counts [page] + 1
    else:
        page_counts[page] = 1

print("/n")
print(log_of_pages_visited)
print("/n")
print(page_counts)

# Step 2 - Find most & least visited pages
# Concept: Extract insights from the frequency data

all_counts = page_counts.values()
max_visits = max(all_counts)
min_visits = min(all_counts)

for (key, value) in page_counts.items():
    if value == max_visits:
        print("\nMost popular pages:")
        print(f"   -{key}: {value} vivits")

print("\nLeast popular pages:")
for (key, value) in page_counts.items():
    if value == min_visits:
        print(f"   -{key}: {value} vivits")

# Step 3 - Find the traffic percentage
# Concept - Convert page visit count to percentages for better insight

total_visits = sum(page_counts.values())

print(f"\nTotal visits: {total_visits}")
print('\nTraffic Distribution:')

page_percentages = {}

for (key, value) in page_counts.items():
    percentage = (value / total_visits) * 100
    page_percentages[key] = f"{percentage:.1f}"
    print(f"    {key}: {value} visits ({page_percentages[key]}%)")

# Step 4 - Idemtify pages needing promotion
# Concept - Use conditional logic with dictionary data to generate insight
low_traffic_threshold = 13 # percentage
low_traffic_pages = {}

print("\n Pages needing promotion:")

for (key, value) in page_percentages.items():
    percentage_val = float(value)

    if percentage_val <= low_traffic_threshold:
        low_traffic_pages[key] = percentage_val

if len(low_traffic_pages) == 0:
    print("All pages have adequate traffic")
else:
    print(low_traffic_pages)






    



    

print("")
print("")
print("+++++++++++++++++++++++++++++++++++++++")
