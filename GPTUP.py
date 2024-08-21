import os
import openai
import requests
from github import Github


openai.api_key = os.getenv('OPENAI_API_KEY')
github_token = os.getenv('GITHUB_TOKEN')


def generate_content(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150 
    )
    content = response.choices[0].text.strip()
    return content


def post_to_github(repo_name, file_path, content, commit_message):
    
    g = Github(github_token)
    repo = g.get_user().get_repo(repo_name)
    
    try:
       
        file = repo.get_contents(file_path)
        repo.update_file(file.path, commit_message, content, file.sha)
    except:
        
        repo.create_file(file_path, commit_message, content)

    print(f"Content posted to {repo_name}/{file_path}")


def main():
    
    prompt = "Write a brief README file for a Python project that analyzes weather data."

   
    content = generate_content(prompt)
    print(f"Generated Content:\n{content}\n")

    
    repo_name = "your-repo-name"
    file_path = "README.md"
    commit_message = "Auto-generated README file"

   
    post_to_github(repo_name, file_path, content, commit_message)

if __name__ == "__main__":
    main()
