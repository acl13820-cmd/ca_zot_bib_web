# ca_zot_bib_web
zotero bibliography web generator for IMPACT Lab

This is modified from [https://github.com/davidswelt/zot_bib_web.git](url) for compatibility with Python 3.13.
This program generates an HTML link for Zotero libraries and collections selected.

**## Note: ALL codes should be entered via the system terminal.##**

## 1. Prerequisites
- Python 3.13 
- Internet connection
- Zotero account with either a **user library** or **group library**
- Zotero API key:
  1. Go to [Zotero Settings → Feeds/API → Create new private key](https://www.zotero.org/settings/keys)
  2. Make sure “Allow library access” is checked

## 2. Clone the repository 

1. Open terminal
2. Download the repository into your desired location:


        git clone https://github.com/acl13820-cmd/ca_zot_bib_web.git "/Users/username/Documents/IMPACT-Zotero"
        cd ca_zot_bib_web


## 3. Create a Python environment 


    python3.13 -m venv env
    source env/bin/activate   # macOS/Linux

 
  OR

    
    env\Scripts\activate      # Windows


## 4. Install required packages


    pip install --upgrade pip
    pip install pyzotero python-dateutil


## 5. Enter Zotero settings (Zotero Web required) 
1. Copy the example settings file:


   cp settings_example.py settings.py


3. Open settings.py in a text editor and fill in:
- Your user ID or group ID (without quotation marks)
- Your Zotero API key (generated in step 1)
- Your collection key

Example: the url for the "TEST" folder in IMPACT_Lab_Psych:

https://www.zotero.org/groups/6217053/impact_lab_psych/collections/A67VDG8R

- 6217053 is the id 
- A67VDG8R is the collection key

## 6. Generate your bibliography HTML


    python zot.py --settings settings.py


- This creates zotero-bib.html in the repo folder.
- The site/ folder contains the required CSS/JS.
- The files/ folder contains any linked attachments.
