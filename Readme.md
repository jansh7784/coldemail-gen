# Cold Email Generator

This project is a Cold Email Generator that uses AI to generate tailored cold emails for job applications. The application is built using Streamlit and leverages various AI and machine learning libraries to extract job descriptions, clean text, and generate personalized emails.

## Features

- Extract job descriptions from job URLs
- Clean and process job descriptions
- Generate personalized cold emails using AI
- Display job descriptions and generated emails
- Provide feedback on generated emails

## Requirements

- Python 3.7 or higher
- `smtplib` library
- `email` library

## Installation

Follow these steps to set up and run the project:

1. **Clone the repository**:
   ```sh
   git clone https://github.com/yourusername/coldemail.git
   cd coldemail
   ```
2. Navigate to the project directory:
    ```sh
    cd coldemail
    ```
3. Install the required libraries:
    ```sh
    pip install -r requirements.txt
    ```

## Configuration

1. Create a `config.json` file in the root directory with the following structure:
    ```json
    {
        "smtp_server": "smtp.example.com",
        "smtp_port": 587,
        "email": "your-email@example.com",
        "password": "your-email-password",
        "subject": "Your Email Subject",
        "templates": ["template1.txt", "template2.txt"]
    }
    ```
2. Create your email templates in the root directory (e.g., `template1.txt`, `template2.txt`).

## Usage

Run the script with the following command:
```sh
python send_emails.py
```

## Project Structure

```markdown
coldemail/
├── app/
│   ├── main.py
│   ├── chains.py
│   ├── portfolio.py
│   ├── utils.py
├── requirements.txt
├── README.md
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## Contact

For any inquiries, please contact [your-email@example.com](mailto:your-email@example.com).

## About the Author

This project was created by [Ansh Jain](https://linkedin.com/in/ansh--jain). The script leverages the power of Python and the `smtplib` library to automate the process of sending cold emails. The project showcases the use of Generative AI to create personalized email templates, making it easier to reach out to potential clients or contacts.

## Boost Your Profile

By contributing to this project, you can enhance your GitHub profile and demonstrate your skills in Python, automation, and the use of AI in practical applications. Feel free to fork the repository, make improvements, and submit pull requests.

## Mini Description

A Python script to automate sending personalized cold emails using configurable templates and logging capabilities. Ideal for reaching out to potential clients or contacts efficiently.

## License

MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.