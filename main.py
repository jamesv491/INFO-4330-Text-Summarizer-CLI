import sys
from google import genai

summmaryNum = 0

# intro text prompt
print("\n\nWelcome to the Text Summarizer. This Summarizer uses Gemini AI as its API"
      "\nPaste text below"
      "\nPress Ctrl+Z then Enter (Windows) or Ctrl+D (Mac/Linux) when done. To Exit Press Ctrl+C")

# used a while loop to allow users to repeatedly insert multiple text
while True:
# try block to read user input from stdin
    try:
        textfromUser = sys.stdin.read().strip() #stdin reads multiple lines (strip includes whitespace and new lines)

    except KeyboardInterrupt:  # Ctrl-C to exit
        print("\nExiting the CLI. Thank you for using the Text Summarizer\n\n")
        sys.exit()

    if not textfromUser: # stops when nothing is entered
        print("\nText box can't be empty. Try Again")
        continue

    if len(textfromUser.split()) < 30: #counts the number of words
        print("\nText has to be more than 30 words. Try Again")
        continue

    # Gemini Ai prompt
    genAIprompt = f"Summarize the following text in 4 to 5 sentences. \n{textfromUser}"

    try:
    # genai.Client() calls the requested model from the Gemini list
        apiClient = genai.Client()
    # Gemini 3.5 is called
        response = apiClient.models.generate_content(
            model = "gemini-3.5-flash",
            contents = genAIprompt
        )


        summmaryNum += 1 # just a counter that was inputted so a user can see what number outputs they are in
        print("\n---------------------------------------------------------------------------------------")
        print(f"|                                   Summary Output {summmaryNum}                                  |")
        print("---------------------------------------------------------------------------------------")
        print(response.text)
        print("\n\nDo you want to continue? To Exit Press Ctrl+C. To continue insert more text")

    except Exception as err:
        print("ERROR. Press Ctrl+C to Exit\n", err)

   