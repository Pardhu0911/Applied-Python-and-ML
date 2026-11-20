# Install the Hugging Face Transformers library

from transformers import pipeline, set_seed

# Initialize the text generation pipeline with GPT-2
# This satisfies Requirement 1: Download and install a pretrained model
chatbot = pipeline('text-generation', model='gpt2')
set_seed(42) # For consistent results
print("Model loaded successfully!")

# Requirement 2: Create a loop for user input and model output
print("Chatbot is ready! Type 'quit' to exit.")

while True:
    user_input = input("You: ")

    # Check for the special keyword to exit
    if user_input.lower() == 'quit':
        print("Chatbot: Goodbye!")
        break

    # Generate a response
    # max_length controls the size of the answer
    response = chatbot(user_input, max_new_tokens=30, num_return_sequences=1, truncation=True, pad_token_id=chatbot.tokenizer.eos_token_id)

    # Print the result
    print("Chatbot:", response[0]['generated_text'])
    print("-" * 30)
