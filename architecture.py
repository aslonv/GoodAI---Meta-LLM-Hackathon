class LlamaApplication:
    def __init__(self):
        self.model = initialize_model()
        self.conversation_history = []

    def preprocess_input(self, user_input):
        # clean & format user input
        # add any context || system prompts
        return formatted_input 
    
    def postprocess_output(self, model_output):
        # clean model response
        return processed_output
    
    def handle_request(self, user_input):
        processed_inpiut = self.preprocess_input(user_input)
        self.conversation_history.append({
            "role": "user",
            "content": processed_input
        })

        response = self.generate_response(
            self.model,
            self.conversation_history
        )

        processed_response = self.postprocess_output(response)
        self.conversation_history.append({
            "role": "assistant",
            "content": processed_response
        })

        return processed_response