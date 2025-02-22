"""
Install these pips on cmd to run the code to access this program

To run the code you've provided, you need to install the required Python packages using pip. Here's a list of the packages you'll need:

speech_recognition: This package is for speech recognition.

Install with:

Copy code
pip install SpeechRecognition
pyttsx3: This package is for text-to-speech conversion.

Install with:

Copy code
pip install pyttsx3
requests: This package is for making HTTP requests.

Install with:

Copy code
pip install requests
Make sure to install these packages in your Python environment before running your code.

"""



# Import necessary libraries
import speech_recognition as sr  # Import the SpeechRecognition library for audio input
import pyttsx3  # Import the pyttsx3 library for text-to-speech conversion
import random  # Import the random library for generating random elements
import string  # Import the string library for working with strings
import requests  # Import the requests library for making HTTP requests

# Assign your ChatGPT API key here
#MAKE SURE YOU HAVE CREDIT AND AN API KEY BEFORE CONTUING
chatgpt_api_key = "INSERT OWN KEY, YOU AINT USING MINE!"

# Initialize text-to-speech engine
engine = pyttsx3.init()  # Initialize the text-to-speech engine

# Function to generate a random username
def generate_username():
    word_count = random.randint(1, 5)  # Generate a random word count for the username
    total_length = random.randint(10, 25)  # Generate a random total length for the username
    words = [random.choice(string.ascii_letters) * random.randint(1, 10) for _ in range(word_count)]  # Generate random words
    username = ' '.join(words)[:total_length]  # Combine words to create the username
    return username

# Create speech recognizer object
r = sr.Recognizer()  # Create a speech recognizer object

# Loop to listen for audio input
while True:  # Run the following code indefinitely

    # Listen for input using the microphone
    with sr.Microphone() as source:
        print("Speak now:")
        audio = r.listen(source)  # Listen for audio input from the microphone

    try:
        # Try to recognize the audio using Google's speech recognition
        prompt = r.recognize_google(audio, language="en-EN", show_all=False)  # Recognize the audio and convert it to text
        print("You Said:", prompt)  # Print the recognized text (what you said)

        # Generate a random username or use #username if not generated
        username = generate_username()  # Generate a random username or use a default if not generated

        # Use ChatGPT API to create a response
        headers = {
            "Authorization": f"Bearer {chatgpt_api_key}",  # Set the API authorization header with the ChatGPT API key
            "Content-Type": "application/json",  # Specify the content type as JSON
        }
        data = {
            "messages": [{"role": "system", "content": '''You Must generate answers in the format username: comment. 
                          You are a group of twitch chatters, each with a diffrent username and personality.
                          Messages have to be within 175 charatars
                          please deploy the chat line by line with a short 0.6 second delay between each person
                          have some chatters talk about the stream involving
                          (random)
                          chat responds (or talks) to mic input and input about the topic
                          U all disagree with each other, sometimes asking followup questions (1 in 100 chance of happening).
                          U love gaming and reacting to funny moment. you also make dodgy jokes about kids or women at times.
                          Keep each message 
                          Sometimes u spam emotes or hashtags at the end of you comment'''},
            #"messages": [{"role": "system", "content": "You are a helpful assistant who is also the great war general napoleon. You must give any resposne to any question as your true war general self and you must come up with any excuse if you are accused of something. You must also not dodge questions or refuse to answer else you loose rank of general and die."},
                        {"role": "user", "content": prompt}],
             "model": "gpt-3.5-turbo"
        }
        response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=data)  # Make a POST request to the ChatGPT API

        if response.status_code == 200:  # Check if the API request was successful (status code 200)
            response_data = response.json()  # Parse the API response as JSON
            response_text = response_data["choices"][0]["message"]["content"]  # Extract the response text from the API response
        else:
            response_text = f"API request failed with status code {response.status_code}: {response.text}"  # Handle API request failure

        # Display output with username
        formatted_output = f"({username}) : {response_text}"  # Combine the username and response text
        print(formatted_output)  # Print the formatted output

        # Remove the comment # for next 2 lines to have text to speech enabled
        # engine.say(formatted_output)
        # engine.runAndWait()  # Convert the response to speech and play it

        print()  # Print an empty line for formatting

    # Catch if recognition fails
    except sr.UnknownValueError:
        response_text = "Sorry, I didn't get that."  # Handle the case where audio recognition fails
        formatted_output = f"({username}) : {response_text}"  # Combine the username and response text
        print(formatted_output)  # Print the formatted output

        # Comment out the following lines to stop text-to-speech
        # engine.say(response_text)
        # engine.runAndWait()  # Convert the response to speech and play it

        print()  # Print an empty line for formatting
