def manage_context(conversation_history, max_tokens=2048):
    current_length = sum(len(message["content"]) for message in conversation_history)
    while current_length > max_tokens:
        conversation_history.pop(0)
        current_length = sum(len(message["content"]) for message in conversation_history)
    return conversation_history 