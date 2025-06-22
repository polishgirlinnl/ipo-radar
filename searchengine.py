import os

def load_company_profiles(folder_path):
    profiles = {}
    for filename in os.listdir(folder_path):
        if filename.endswith('.txt'):
            with open(os.path.join(folder_path, filename), 'r') as file:
                content = file.read()
                profiles[filename] = content
    return profiles

def search_profiles(profiles, query):
    query_words = query.lower().split()
    results = []
    for filename, content in profiles.items():
        if all(word in content.lower() for word in query_words):
            results.append(format_profile(content))
    return results

def format_profile(content):
    lines = content.strip().split('\n')
    info = {}
    for line in lines:
        if ':' in line:
            key, value = line.split(':', 1)
            info[key.strip()] = value.strip()
    
    name = info.get('Company', 'Unknown Company')
    valuation = info.get('Valuation', 'Unknown Valuation')
    ipo_year = info.get('IPO Year', 'Unknown Year')
    notes = info.get('Notes', '')
    investors = info.get('Investors', '')
    
    return f"{name}: {valuation}. {notes} {ipo_year} IPO. Backed by {investors}."

def main():
    profiles = load_company_profiles('companies')
    while True:
        query = input("Enter search query (or press Enter to exit): ").strip()
        if not query:
            break
        matches = search_profiles(profiles, query)
        if matches:
            print("Results:")
            for result in matches:
                print(result)
        else:
            print("No results found.")

if __name__ == "__main__":
    main()
