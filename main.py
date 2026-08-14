import sys
from google import genai

# intro text prompt
print("\n\nWelcome to the Text Summarizer. This Summarizer uses Gemini AI as its API"
      "\nPaste text below"
      "\nPress Ctrl+Z then Enter (Windows) or Ctrl+D (Mac/Linux) when done")

# try block to read user input from stdin
try:
    textfromUser = sys.stdin.read().strip() #stdin reads multiple lines (strip includes whitespace and new lines)

except KeyboardInterrupt:  #
    print("\nRequest cancelled by user")
    sys.exit()

if not textfromUser:
    print("\nText box can't be empty")
    sys.exit()

if len(textfromUser.split()) < 30:
    print("\nText has to be more than 30 words")
    sys.exit()

# Gemini Ai prompt
genAIprompt = f"Summarize the following text in 4 to 5 sentences. Keep it easy to read.\n{textfromUser}"

try:
# genai.Client() calls the requested model from the Gemini list
    apiClient = genai.Client()
# Gemini 3.5 is called
    response = apiClient.models.generate_content(
        model = "gemini-3.5-flash",
        contents = genAIprompt
    )

    print("\nSummary Output\n")
    print(response.text)

except Exception as err:
    print("ERROR", err)