# Disclaimer

This repository contains a modified third-party software. Flickr image-scraping software developed by Ultralytics LLC, and **is freely available for redistribution under the GPL-3.0 license**. For more information please visit https://www.ultralytics.com.

# Requirements

- Python 3.8.3
- pip package manager
- virtualenv package for python

# Instructions

### 1. Clone repository

```bash
git clone https://github.com/fanismahmalat/mga410_communicating_systems
```

### 2. Navigate into the folder of virtual environment

```bash
cd mga410_communicating_systems
```

### 3. Activate virtual environment

```bash
Scripts\activate.bat
```

Note: The above command is used on Windows systems

### 4. Install dependencies

```bash
pip install -U -r requirements.txt
```

# Use

Note: Use with activated virtual environment

### 1. Navigate into src folder

```bash
cd src
```

### 2. Run python script

```python
python communicate.py
```

3. Input any the search term in the terminal

4. You should see the downloaded image in the folder /src/temp_image/**image.jpg** and the word output in /src/processing-system/executable/**singleWord.txt**
