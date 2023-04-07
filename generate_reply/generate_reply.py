import os
import openai

def generate(input_email):
    # get api key from env vars
    OPEN_AI_KEY = os.environ.get('OPEN_AI_KEY')

    system_prompt = (
        f"You are a helpful assistant that helps startup founders reply to Venture Capitalists that reach out to them "
        f"to politely decline requests for meetings. The replies you generate should decline the meeting, "
        f"notify the venture capitalist that the founder is not fundraising any time soon and that it would be "
        f"best to check back down the line. Include some personalization in the response and don't make it sound overly formal.\n"
    )
    system_prompt += (
        f"Here are a few example responses I have sent for previous emails: \n"
        f"Example 1: Hey X, appreciate you reaching out! We are very heads down on product at least through the end of this year. \n"
        f"Would be happy to circle back when the timing is better on our end."
        f"Example 2: Hey X -- I think we’re still a few quarters from thinking about fundraising, so let’s check in again in a few months. \n"
    )

    # var for chat conversation
    messages = [
        {"role": "system", "content": system_prompt},
    ]

    user_message = "Please reply to this email: " + input_email

    messages.append({"role": "user", "content": user_message})

    # generate email from OpenAI 
    system_response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages,
        api_key=OPEN_AI_KEY,
    )
    return system_response['choices'][0]['message']['content']
