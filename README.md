# Disclaimer

This repository contains a modified third-party software. Flickr image-scraping software developed by Ultralytics LLC, and **is freely available for redistribution under the GPL-3.0 license**. For more information please visit https://www.ultralytics.com.

# Requirements

- Python 3.8.3
- virtualenv package for python

# Instructions

### 1. Create virtual environment

```bash
virtualenv <name>
```

### 2. Navigate into the folder of virtual environment

```bash
cd <name>
```

### 3. Clone repository

```bash
git clone https://github.com/fanismahmalat/mga410_communicating_systems .
```

### 4. Activate virtual environment

```bash
Script\activate.bat
```

### 5. Install dependencies

```bash
pip install -U -r requirements.txt
```

# Use

Note: Use with activated virtual environment

### 1. Run python script

```python
python flickr_scraper.py
```

### 2. Input any the search term in the terminal

### 3. You should see the downloaded image in the folder /src/temp_image/**image.jpg** and the word output in /src/processing-system/executable/**singleWord.txt**
