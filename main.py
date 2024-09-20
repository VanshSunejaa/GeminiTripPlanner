import streamlit as st
import google.generativeai as genai
from PIL import Image
from io import BytesIO
import requests

# Retrieve the API key from secrets
GOOGLE_API_KEY = st.secrets["google_api_key"]

# Configure Google API key for Gemini
genai.configure(api_key=GOOGLE_API_KEY)

# Function to get response from Gemini
def get_gemini_response(prompt):
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(prompt)
        return response.text, response.images if 'images' in response else []  # Handle missing images gracefully
    except Exception as e:
        return f"An error occurred while generating the response: {str(e)}", []

# Streamlit UI
st.title("Personalized Travel Itinerary Planner")

# User inputs
destination = st.text_input("Enter your travel destination")
duration = st.number_input("Enter the duration of your trip (in days)", min_value=1)
preferences = st.text_area("Enter your travel preferences (e.g., interests, dietary restrictions, activities)")

if st.button("Generate Itinerary"):
    if destination and duration and preferences:
        # Create the prompt for Gemini
        prompt = (f"Generate a detailed travel itinerary for a {duration}-day trip to {destination}. "
                  f"Consider the following preferences: {preferences}. "
                  "Include recommendations for attractions, restaurants, and accommodations. "
                  "Provide a day-by-day breakdown and include images for each recommendation. "
                  "Ensure to provide a good balance between text and visual content.")

        # Get Gemini response
        st.write("Generating your travel itinerary...")
        itinerary_text, itinerary_images = get_gemini_response(prompt)

        # Display itinerary text
        st.subheader("Your Personalized Travel Itinerary")
        st.write(itinerary_text)

        # Display images
        if itinerary_images:
            st.subheader("Recommended Images")
            for img_url in itinerary_images:
                try:
                    response = requests.get(img_url)
                    img = Image.open(BytesIO(response.content))
                    st.image(img, caption="Recommended Image", use_column_width=True)
                except Exception as img_err:
                    st.write(f"Error loading image: {img_err}")
        else:
            st.write("No images available for this itinerary.")
    else:
        st.warning("Please fill in all the fields to generate the itinerary.")
