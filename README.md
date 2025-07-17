# Simple Chatbot with Llama 3.3

A beginner-friendly chatbot implementation using the Together.xyz API and Meta's Llama 3.3 70B model. This project serves as an introduction to working with Large Language Models (LLMs) and API integration.

## Features

- Interactive command-line chat interface
- Persistent conversation history during the session
- Uses Meta's Llama 3.3 70B Instruct Turbo model
- Simple and clean Python implementation
- Environment variable configuration for API security

## Prerequisites

- Python 3.6 or higher
- A Together.xyz API account and API key
- Basic understanding of Python and command-line usage

## Installation

1. Clone this repository:
```bash
git clone [<repository-url>](https://github.com/KalashThakare/Basic-ChatBot)
cd Basic-ChatBot
```

2. Install required dependencies:
```bash
pip install requests python-dotenv
```

3. Create a `.env` file in the project root directory:
```env
API_KEY=your_together_xyz_api_key_here
```

4. Get your API key from [Together.xyz](https://api.together.xyz/) and add it to the `.env` file.

## Usage

Run the chatbot:
```bash
python chatbot.py
```

Once started:
- Type your messages and press Enter to chat
- The bot will respond using the Llama 3.3 model
- Type `exit` to quit the conversation

## Example Conversation

```
Chatbot: Hello! Type 'exit' to quit.

You: What is machine learning?
Chatbot: Machine learning is a subset of artificial intelligence that enables computers to learn and improve from experience without being explicitly programmed...

You: Can you explain it simply?
Chatbot: Sure! Think of machine learning like teaching a computer to recognize patterns...

You: exit
Chatbot: Goodbye!
```

## Configuration

The chatbot uses the following default settings:
- **Model**: `meta-llama/Llama-3.3-70B-Instruct-Turbo-Free`
- **Temperature**: 0.7 (controls response creativity)
- **System prompt**: "You are a helpful assistant."

You can modify these settings in the `chatbot.py` file:
```python
MODEL = "meta-llama/Llama-3.3-70B-Instruct-Turbo-Free"
temperature = 0.7  # Adjust in the payload dictionary
```

## File Structure

```
project-root/
├── chatbot.py          # Main chatbot script
├── .env               # Environment variables (create this)
└── README.md          # This file
```

## How It Works

1. **Environment Setup**: Loads API key from `.env` file using `python-dotenv`
2. **Message Management**: Maintains conversation history in a messages list
3. **API Communication**: Sends requests to Together.xyz API with conversation context
4. **Response Handling**: Processes API responses and displays them to the user
5. **Loop**: Continues until user types 'exit'

## Error Handling

The chatbot includes basic error handling for:
- API request failures
- HTTP status code errors
- Network connectivity issues

## Learning Notes

This project demonstrates:
- API integration with external services
- Environment variable management
- JSON payload construction
- HTTP request/response handling
- Basic chat loop implementation
- Conversation context management

## Troubleshooting

**Common Issues:**

1. **API Key Error**: Ensure your API key is correctly set in the `.env` file
2. **Module Not Found**: Install required packages using `pip install requests python-dotenv`
3. **API Rate Limits**: The free tier may have usage limitations
4. **Network Issues**: Check your internet connection

## Contributing

This is a learning project, but feel free to suggest improvements or report issues!

## License

This project is open source and available under the MIT License.

## Acknowledgments

- Together.xyz for providing the API
- Meta for the Llama 3.3 model
- The open-source community for inspiration and learning resources
