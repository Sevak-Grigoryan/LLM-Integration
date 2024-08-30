import telebot
import openai

TOKEN = 'Your Token'
bot = telebot.TeleBot(TOKEN)

openai.api_base = "http://localhost:1234/v1"
openai.api_key = "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"

LLM_MODEL = "TheBloke/CodeLlama-7B-Instruct-GGUF"

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Hello! Send me a question.")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    try:
        print("Received message: ", message.text)
        completion = openai.ChatCompletion.create(
            model=LLM_MODEL,
            messages=[
                {"role": "system", "content": "Always answer in rhymes."},
                {"role": "user", "content": message.text}
            ],
            temperature=0.7,
        )
        print("OpenAI response: ", completion)
        reply = completion.choices[0].message['content']
        bot.reply_to(message, reply)

    except Exception as ex:
        print("Error: ", ex)
        bot.send_message(message.chat.id, f"An error occurred: {ex}")

bot.polling()