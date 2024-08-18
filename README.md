# 🧠🤖 AI-Generated Content Poster to GitHub 📂🚀

This Python project automates the process of generating content using OpenAI's GPT models and then posting that content to a GitHub repository. It's perfect for anyone looking to streamline content creation and version control. ✨

## Features 🎯

- **AI-Powered Content Generation**: Utilizes OpenAI's GPT-3 model to generate content based on a custom prompt. 📝
- **Automated GitHub Integration**: Automatically commits and pushes the generated content to a specified GitHub repository. 🗂️

## How It Works ⚙️

1. **Set Up Environment Variables**: 
   - `OPENAI_API_KEY`: Your OpenAI API key.
   - `GITHUB_TOKEN`: Your GitHub Personal Access Token.

2. **Generate Content**:
   - The script sends a prompt to OpenAI's API and receives generated text as a response.
   - Customize the `prompt` variable in the `main()` function to tailor the content to your needs. 🎨

3. **Post Content to GitHub**:
   - The script checks if the specified file exists in the GitHub repository.
   - If the file exists, it updates the file with the new content.
   - If the file does not exist, it creates a new file in the repository. 💾

## Prerequisites 🛠️

- Python 3.x 🐍
- [OpenAI Python SDK](https://github.com/openai/openai-python) 📦
- [PyGithub Library](https://pygithub.readthedocs.io/en/latest/) 🛠️

Install the necessary libraries:

```bash
pip install openai PyGithub
```

## Usage 🚀

1. Clone the repository:

   ```bash
   git clone https://github.com/hu5o-dev/GPT-Github-Uploader.git
   ```

2. Set up environment variables for your OpenAI API key and GitHub token:

   ```bash
   export OPENAI_API_KEY="your-openai-api-key"
   export GITHUB_TOKEN="your-github-token"
   ```

3. Run the script:

   ```bash
   python GPTUP.py
   ```

## Example Prompt 🧩

In the script, you can customize the `prompt` variable. For example:

```python
prompt = "Write a brief README file for a Python project that analyzes weather data."
```

The generated content will be saved to the specified file and committed to your GitHub repository.

## Contributing 🤝

Feel free to open an issue or submit a pull request if you find any bugs or have suggestions for improvements. Contributions are always welcome! 🎉

## License 📄

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Enjoy automating your GitHub content with AI! 🚀💡

