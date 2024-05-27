import streamlit as st
from crewai import Crew
import os
from agents.loader import Agents
from tasks.loader import Tasks
from crewai.process import Process


def main():
    # Title and description
    st.title("🚀 Be a Good Fit for an Opportunity")
    st.caption("This app helps you boost your CV and increase your chances to land your desired job. Enter your API keys to get started.")

    os.environ["OPENAI_API_KEY"] = os.environ["MISTRAL_API_KEY"]
    os.environ["OPENAI_API_BASE"] = "https://api.mistral.ai/v1"
    os.environ["OPENAI_MODEL_NAME"] = "mistral-small-2402"

    pdf_file = st.file_uploader("Upload Your CV", type=["pdf"])

    if pdf_file is not None:

        st.write("PDF file uploaded successfully!")

        # Main page inputs after processing button is hit
        st.subheader("Tell Us About Yourself and the Job You're pursuing")
        user_name = st.text_input("Your Name")
        job_opp_name = st.text_input("Job Opportunity Name")
        key_requirements = st.text_input(
            "Key Requirements of the Opportunity")
        consult_button = st.button("CONSULT ME!")

        if consult_button:
            st.write("Processing your request...")

            crew = Crew(
                agents=Agents.load(),
                tasks=Tasks.load(
                    job_opp=job_opp_name, candidate_name=user_name, requirements=key_requirements, cv=pdf_file),
                verbose=2,
                process=Process.sequential
            )

            result = crew.kickoff()

            # Placeholder response
            st.success("Your consultation request has been submitted!")

            st.write(result)


if __name__ == "__main__":
    main()
