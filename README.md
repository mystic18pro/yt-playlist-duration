# YouTube Playlist Duration 
---
## To build the program Yourself

### Step 1: Clone this repository.

- Use this command to the clone the repo.
```bash
git clone https://github.com/mystic18pro/yt-playlist-duration.git
```
### Step 2: Get an API key.

- Go to [Google Cloud Console](https://console.cloud.google.com)
- Create a project or go to an existing one if you have created it already
- Click on 'APIs and Services' -> Library
- Search for "YouTube Data API V3" 
- Click on the first result and click 'Enable' or 'Manage' (Manage will appear if you have already enabled the API)
- Go to Credentials
- Click on 'Create Credentials' -> 'API Key'
- A dialog box will appear containing your API key, copy it and keep it somewhere safe for later.

### Step 3: Setup .env

- Go to the folder containing repository files. It will look like this
```
yt-playlist-duration
|-- requirements.txt
|-- main.py
|-- .gitignore
|-- README.md
```
- Create a .env file in the same directory
- Create a variable and enter the API key copied like this:
```shell
YOUTUBE_API_KEY=<your-api-key>
```

### Step 4: Install the required packages

- Enter this command to install the required packages.
```bash
pip install -r requirements.txt
```

This is for MacOS:
```bash
pip3 install -r requirements.txt
```
### Step 5: Run the Program

- Run the program by entering this command
```bash
python main.py
```
This is for MacOS:
```bash
python3 main.py
```

