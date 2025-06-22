# 🚀 IPO Radar

A lightweight Python search engine for tracking high-potential companies predicted to go public.

IPO Radar is a simple yet powerful command-line tool that helps you explore startups and unicorns speculated to IPO soon. Built entirely with core Python (no web scraping, no APIs), it’s a fast and clean way to search curated company profiles using keyword queries.

------------------------------------------------------------

# 🔍 FEATURES

- Search by industry, valuation, investors, IPO year, or location
- Instant keyword matching across plain-text company files
- Clean CLI output with rich summaries
- Fully offline — no dependencies beyond Python 3
- Structured and scalable folder format

------------------------------------------------------------

# 📁 PROJECT STRUCTURE

ipo-radar/
├── companies/
│   ├── openai.txt
│   ├── stripe.txt
│   ├── databricks.txt
│   └── ...more
├── searchengine.py
├── README.md
└── thumbnail.jpg

Each .txt file in companies/ contains a profile like:

Company: OpenAI
Valuation: $90B
IPO Year: 2025
Investors: Microsoft, Khosla Ventures
Notes: Likely IPO in 2025.

------------------------------------------------------------

# 💡 EXAMPLE USAGE

$ python3 searchengine.py
Enter search query (or press Enter to exit): AI unicorn 2025

Results:
OpenAI: $90B valuation. Likely IPO in 2025. Backed by Microsoft, Khosla Ventures.
Anthropic: $18B valuation. Focused on AI safety. 2025 IPO speculation growing.

------------------------------------------------------------

# 🧠 BUILT WITH

- Python 3
- Terminal / Command Line
- Lists, Dictionaries, File I/O

------------------------------------------------------------

# 🎓 CREATED FOR

This project was created as the final submission for Code in Place 2025 — Stanford's global introductory Python course.

------------------------------------------------------------

# ✨ CONTRIBUTING & EXTENSIONS

While simple by design, IPO Radar could be expanded in many directions:
- Add sorting (by valuation or IPO year)
- Create a GUI with tkinter
- Add AI-generated summaries using an API
- Export matched results to CSV

Feel free to fork this project and build on it!

------------------------------------------------------------

# 📬 CONTACT

Made with 💻 by @polishgirlinnl
Questions or feedback? Open an issue or send a PR!
