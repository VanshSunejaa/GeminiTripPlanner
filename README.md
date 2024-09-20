

# Gemini-Trip-Planner

**Gemini-Trip-Planner** is a personalized travel itinerary generator that leverages Google's Gemini API to provide tailored travel plans based on user preferences. The project allows users to input their travel destination, trip duration, and specific interests or preferences, generating a custom day-by-day itinerary complete with recommendations for attractions, restaurants, accommodations, and visual content. This project serves as a demonstration of AI-powered content generation using natural language inputs, offering users a unique blend of text and images to enhance their travel planning experience.

## Features
- **Personalized Itinerary**: Generates travel itineraries based on user input, including the destination, duration, and preferences.
- **Day-by-Day Breakdown**: Provides detailed recommendations for each day of the trip, balancing activities, dining, and relaxation.
- **Visual Recommendations**: Includes images for key recommendations, giving users a visual guide to their travel destinations.
- **AI-Powered**: Uses Google's Gemini model to create rich and engaging content, combining text and images.

## File Structure
```
Gemini-Trip-Planner/
│
├── main.py               # Main Streamlit application file
├── requirements.txt      # Required Python packages
├── README.md             # Project documentation
└── .gitignore            # File to exclude API keys and unnecessary files from version control
```

## Code Explanation

### `main.py`
This file contains the core logic of the application. Here's a breakdown of the key sections:

- **Imports**:
  - `streamlit` is used for the web interface.
  - `google.generativeai` is the library used to interact with Google's Gemini API.
  - `PIL` and `requests` handle image fetching and display.
  
- **API Key Configuration**:
  - The API key for accessing Google's Gemini API is configured but should be kept secret (not hardcoded in public repositories).

- **Main Functions**:
  - `get_gemini_response(prompt)`: This function sends a prompt to the Gemini API and returns both text and images in the response.
  - The user inputs (destination, duration, preferences) are processed to form a detailed prompt sent to the Gemini model for generating an itinerary.

- **Streamlit UI**:
  - The UI gathers user input and presents the generated itinerary in both text and image formats.
  - The itinerary is shown in a day-by-day format, with visual recommendations for a richer travel experience.

### `requirements.txt`
This file lists the necessary libraries for the project. You can install them with:

```bash
pip install -r requirements.txt
```

Contents of `requirements.txt`:
```
streamlit
google-generativeai
Pillow
requests
```

### `.gitignore`
This file is used to exclude sensitive data (like the API key) and unnecessary files from being uploaded to version control, ensuring that credentials are kept secure.

## Instructions

### Prerequisites
- Python 3.x
- A Google Gemini API key (obtainable from Google Cloud)

### Setup
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/Gemini-Trip-Planner.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Gemini-Trip-Planner
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set your Google API key:
   Replace the `GOOGLE_API_KEY` in the `main.py` file with your actual API key, or securely store it as an environment variable.

5. Run the application:
   ```bash
   streamlit run main.py
   ```

### Usage
- Open the web interface in your browser.
- Enter your travel destination, trip duration, and preferences.
- Click "Generate Itinerary" to get a personalized travel plan with text and images.

## Disclaimer
This project is built for learning purposes and is not designed for actual user use. Some limitations may exist due to API constraints or incomplete feature implementations.

