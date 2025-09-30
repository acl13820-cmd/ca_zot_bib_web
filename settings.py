
group_collection(
    id=1234567,
    api_key='your_key',
    collection='your_collection'
)

# -------------------------------------------------
# Output configuration
# -------------------------------------------------

# Name of the generated HTML file
outputfile = "zotero-bib.html"

# Generate a full HTML page (header + body) or just the body fragment
write_full_html_header = True

# Paths to CSS and JS (these files are included in the 'site/' folder in the repo)
stylesheet_url = "site/style.css"
jquery_path = "site/jquery.min.js"

# Directory where attachment files (like PDFs) will be stored locally
file_outputdir = "files/"
# URL path where those files will be accessible on your webserver
file_output_path = "files/"

# -------------------------------------------------
# UI options
# -------------------------------------------------
# Show a search box on the page
show_search_box = True

# Show shortcuts (by collection, year, etc.)
show_shortcuts = ["collection", "year"]

# Optional: sort order (uncomment to use)
# sortby = "date"    # or "author", "title"
# sort_direction = "desc"

# -------------------------------------------------
# Done! Run zot_bib_web like this:
#   ./zot.py --settings settings.py
# ===========================================
