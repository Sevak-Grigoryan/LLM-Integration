# LLM Chat Bot

This project is a Telegram bot powered by a locally hosted LLM (Large Language Model) using LM Studio and OpenAI’s API framework. The bot responds to user messages with answers in rhymes, providing a fun and creative experience.

## Features
- Telegram bot integration using `telebot`
- Locally hosted LLM via LM Studio
- Custom instructions for the model to always reply in rhymes
- Handles user messages gracefully with error management

## Requirements
- Python 3.7+
- Telegram Bot API token
- LM Studio with a compatible LLM model installed
- Required Python packages:
  - `pyTelegramBotAPI`
  - `openai`

## Installation
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Sevak-Grigoryan/LLM-Integration.git
   cd LLM-Integration
   ```

2. **Install Dependencies:**
   ```bash
   pip install telebot openai
   ```

3. **Configure API Keys:**
   - Replace `Your Token` with your actual Telegram bot token.
   - Update the `openai.api_key` field with your LM Studio key.

4. **Run the Bot:**
   ```bash
   python main.py
   ```

## Usage
- Start the bot on Telegram by sending `/start`.
- Send any message, and the bot will respond in rhymes.

## Code Overview
```python
@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Hello! Send me a question.")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    try:
        completion = openai.ChatCompletion.create(
            model=LLM_MODEL,
            messages=[
                {"role": "system", "content": "Always answer in rhymes."},
                {"role": "user", "content": message.text}
            ],
            temperature=0.7,
        )
        reply = completion.choices[0].message['content']
        bot.reply_to(message, reply)
    except Exception as ex:
        bot.send_message(message.chat.id, f"An error occurred: {ex}")

bot.polling()
```

## Customization
- Modify the `LLM_MODEL` variable to point to any compatible model.
- Update system instructions to change the bot’s behavior.
- Adjust `temperature` for more creative or focused responses.

## Troubleshooting
- **Connection Error:** Ensure that LM Studio is running and accessible at the specified URL.
- **Invalid API Key:** Verify your `openai.api_key`.
- **Telegram Errors:** Check that your bot token is correct.

## License
This project is licensed under the MIT License.

---

Feel free to contribute by submitting issues or pull requests.

