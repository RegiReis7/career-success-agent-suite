import streamlit as st
from crewai import Crew
import os


def main():
    # Title and description
    st.title("🚀 Be a Good Fit for an Opportunity 🚀")
    st.caption("This app helps you boost your CV and increase your chances to land your desired job. Enter your API keys to get started.")

    # Sidebar inputs for API keys
    st.sidebar.header("API Keys")
    mistral_api_key = st.sidebar.text_input("Enter Mistral API Key")
    exa_search_api_key = st.sidebar.text_input("Enter Exa Search API Key")
    process_button = st.sidebar.button("Process")

    if process_button:
        os.environ["EXA_API_KEY"] = exa_search_api_key
        os.environ["OPENAI_API_KEY"] = mistral_api_key
        os.environ["OPENAI_API_BASE"] = "https://api.mistral.ai/v1"
        os.environ["OPENAI_MODEL_NAME"] = "mistral-small-2402"
        
        pdf_file = st.file_uploader("Upload Your CV", type=["pdf"])

        if pdf_file is not None:
            
            st.write("PDF file uploaded successfully!")
            # Main page inputs after processing button is hit
            st.subheader("Tell Us About Yourself")
            user_name = st.text_input("Your Name")
            job_opp_name = st.text_input("Job Opportunity Name")
            key_requirements = st.text_input("Key Requirements of the Opportunity")
            consult_button = st.button("CONSULT ME!")

            if consult_button:
                st.write("Processing your request...")

                # Further processing logic can be added here
                # Example: API calls, CV analysis, etc.

                # Placeholder response
                st.success("Your consultation request has been submitted!")


if __name__ == "__main__":
    main()