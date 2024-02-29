from tenacity import retry, stop_after_attempt, wait_random_exponential, wait_exponential


@retry(wait=wait_exponential(min=20, max=120), stop=stop_after_attempt(100))
def call_palm_with_backoff(chat, message, mode='chat'):
    temperature = 0.4
    top_p = 0.95
    max_output_tokens = 700
    top_k = 30
    if mode == 'chat':
        return chat.send_message(message,
                                 temperature=temperature,
                                 max_output_tokens=max_output_tokens,
                                 top_p=top_p,
                                 top_k=top_k
                                 )
    else:
        return chat.predict(message,
                            temperature=temperature,
                            max_output_tokens=max_output_tokens,
                            top_p=top_p,
                            top_k=top_k
                            )
