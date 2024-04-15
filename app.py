import streamlit as st
import openai

# Set your API key
openai.api_key = ["enter your api key"]

def main():
    st.title("GenAI App - AI Code Reviewer")
    code_input = st.text_area("Enter your Python code here:")
    if st.button("Review Code"):
        # Call the function to review the code
        review_code(code_input)

def review_code(code):
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",
        prompt=f"for the given code identify the errors{code} and give the corrected code and give explanation for it also",
        max_tokens=200,
        temperature=0,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )

    st.write("API Response:")
    st.write(response)

    results = response.choices[0].text.strip().split("\n\n")
    
    for result in results:
        lines = result.strip().split("\n")
        if lines[0].startswith("Correction:"):
            corrected_code = '\n'.join(lines[1:])
            explanation = ""
            if len(lines) > 1 and lines[1].startswith("Explanation:"):
                explanation = lines[1]
            st.code(corrected_code)
            if explanation:
                st.write(explanation)


if __name__ == "__main__":
    main()

