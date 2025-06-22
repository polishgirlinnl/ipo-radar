import os

# Loads all company profiles from the 'companies/' folder.
# Returns a dictionary mapping filenames to their content.
def load_company_profiles(folder_path):
    profiles = {}
    for filename in os.listdir(folder_path):
        if filename.endswith('.txt'):
            with open(os.path.join(folder_path, filename), 'r') as file:
                content = file.read()
                profiles[filename] = content
    return profiles

# Searches the profiles for matches with the query.
# Only returns profiles that match ALL query words (case-insensitive).
def search_profiles(profiles, query):
    query_words = query.lower().split()  # Split input into lowercase words
    results = []
    for filename, content in profiles.items():
        # Check if all query words are present in the profile text
        if all(word in content.lower() for word in query_words):
            results.append(format_profile(content))  # Format matched profile nicely
    return results

# Formats a profile's text into a single summary line.
# Extracts structured info like Company, Valuation, IPO Year, etc.
def format_profile(content):
    lines = content.strip().split('\n')  # Split file content into lines
    info = {}
    for line in lines:
        if ':' in line:
            key, value = line.split(':', 1)  # Split each line into key-value pair
            info[key.strip()] = value.strip()

    # Get specific fields from the info dictionary
    name = info.get('Company', 'Unknown Company')
    valuation = info.get('Valuation', 'Unknown Valuation')
    ipo_year = info.get('IPO Year', 'Unknown Year')
    notes = info.get('Notes', '')
    investors = info.get('Investors', '')

    # Return a single-line summary
    return f"{name}: {valuation}. {notes} {ipo_year} IPO. Backed by {investors}."

# Main loop: prompts the user for queries and shows results
def main():
    profiles = load_company_profiles('companies')  # Load all .txt files in companies/
    while True:
        query = input("Enter search query (or press Enter to exit): ").strip()
        if not query:
            break  # Exit if query is empty
        matches = search_profiles(profiles, query)
        if matches:
            print("Results:")
            for result in matches:
                print(result)  # Print each formatted result
        else:
            print("No results found.")  # No match case

# This tells Python to run main() when the script is executed directly
if __name__ == "__main__":
    main()
