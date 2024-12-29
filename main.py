import streamlit as st
import subprocess
import os

# Set up page
st.set_page_config(page_title="Python Code Runner IDE", layout="wide")

st.title("Python Code Runner IDE")

# Sidebar for File Management
st.sidebar.title("File Management")
file_name = st.sidebar.text_input("File Name", value="example.py")
save_file = st.sidebar.button("Save Code to File")
load_file = st.sidebar.button("Load Code from File")

# Code Editor with Syntax Highlighting
st.subheader("Code Editor")
code = st.text_area(
    "Write your Python code below:",
    height=400,
    help="Write or paste your Python code here."
)

# Save Code to File
if save_file and file_name.strip():
    with open(file_name, "w") as f:
        f.write(code)
    st.sidebar.success(f"Code saved to {file_name}!")

# Load Code from File
if load_file and file_name.strip() and os.path.exists(file_name):
    with open(file_name, "r") as f:
        code = f.read()
    st.experimental_rerun()  # Refresh UI with loaded code
elif load_file and not os.path.exists(file_name):
    st.sidebar.error("File not found!")

# Run Button with Console Output
if st.button("Run Code"):
    if code:
        st.subheader("Console Output")
        try:
            output = subprocess.check_output(
                ['python', '-c', code],
                stderr=subprocess.STDOUT,
                universal_newlines=True
            )
            st.text_area("Output", value=output, height=200)
        except subprocess.CalledProcessError as e:
            st.text_area("Error", value=e.output, height=200)

# Settings Section
# st.sidebar.title("Settings")
# dark_mode = st.sidebar.checkbox("Dark Mode")
# auto_save = st.sidebar.checkbox("Enable Auto-Save")

# Appearance based on Dark Mode
# Footer
st.sidebar.write("---")
st.sidebar.write("Developed with ❤️ by Adarsh Tayde")
