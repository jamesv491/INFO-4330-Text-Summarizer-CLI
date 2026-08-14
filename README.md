# AI TEXT SUMMARIZER CLI - INFO 4330
## Project by James Viola (100436508) + Sahib Nijjar (100390348)
### Step 1) Install the package

    pip install google-genai

### <br>Step 2) Get a Gemini API key
Go to 

    aistudio.google.com/apikey

Make an account/sign in and obtain an API Key

### <br>Step 3) Set the API key as an environment variable

Copy and paste the given key into the "your-key-here" portion of the line code

  **Windows (PowerShell):**
  
    $env:GEMINI_API_KEY="your-key-here"
  
  **Mac/Linux:**
  
    export GEMINI_API_KEY="your-key-here" 

**NOTE:** the given key will need to be inputted if the terminal is reset. For example, the VS Code application is closed.
  
### <br>Step 4. Run the script:
  
    python main.py
