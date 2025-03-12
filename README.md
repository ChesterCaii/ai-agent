# AI Task Assistant

An intelligent task management assistant powered by OpenAI's GPT models. This agent can understand natural language commands and help manage tasks through conversation.

## Features

- Natural language command processing
- Modular architecture for extensibility
- Async support for better performance
- Rich console output with status messages
- Comprehensive error handling

## Requirements

- Python 3.12+
- OpenAI API key

## Installation

1. Clone the repository:
```bash
git clone https://github.com/ChesterCaii/ai-agent.git
cd ai-agent
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root and add your OpenAI API key:
```
OPENAI_API_KEY=your_api_key_here
```

## Usage

Run the assistant:
```bash
python src/main.py
```

The assistant will prompt you for commands. Type your task-related commands in natural language, and the assistant will interpret and execute them.

## Project Structure

```
ai-agent/
├── src/
│   ├── agent.py      # Core agent implementation
│   ├── main.py       # Entry point
│   └── modules/      # Task modules
├── tests/            # Test files
├── requirements.txt  # Project dependencies
└── README.md        # This file
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. 