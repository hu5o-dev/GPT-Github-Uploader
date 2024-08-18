import os
import openai
import requests
from github import Github

# Load API keys from environment variables
openai.api_key = os.getenv('OPENAI_API_KEY')
github_token = os.getenv('GITHUB_TOKEN')

# Function to generate content using OpenAI GPT
def generate_content(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150  # Adjust the length according to your need
    )
    content = response.choices[0].text.strip()
    return content

# Function to commit and push content to GitHub
def post_to_github(repo_name, file_path, content, commit_message):
    # Authenticate to GitHub
    g = Github(github_token)
    repo = g.get_user().get_repo(repo_name)
    
    try:
        # Check if the file already exists in the repository
        file = repo.get_contents(file_path)
        repo.update_file(file.path, commit_message, content, file.sha)
    except:
        # If the file does not exist, create a new file
        repo.create_file(file_path, commit_message, content)

    print(f"Content posted to {repo_name}/{file_path}")

# Main function
def main():
    # Define your prompt for AI content generation
    prompt = "Write a brief README file for a Python project that analyzes weather data."

    # Generate content
    content = generate_content(prompt)
    print(f"Generated Content:\n{content}\n")

    # Define your GitHub repository details
    repo_name = "your-repo-name"
    file_path = "README.md"
    commit_message = "Auto-generated README file"

    # Post content to GitHub
    post_to_github(repo_name, file_path, content, commit_message)

if __name__ == "__main__":
    main()
