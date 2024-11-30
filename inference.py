# example showing different inference approaches

class InferenceHandler:
    def __init__(self):
        self.local_model = None 
        self.groq_client = None 
    
    def streaming_inference(self, user_input):
        """Stream responses token by token"""
        for token in self.groq_client.generate_stream(user_input):
            yield token 
    
    def batch_inference(self, input_batch):
        """Process multiple inputs at once"""
        responses = self.groq_client.generate_batch(
            prompts=input_batch,
            max_tokens=100
        )
        return responses 
    
# example usage
class ApplicationServer:
    def __init__(self):
        self.inference_handler = InferenceHandler()
        self.request_queue = []

    async def handle_user_request(self, user_input):
        """Handle a single user request"""
        # For quick responses 
        if self.is_simple_request(user_input):
            return await self.inference_handler.optimized_inference(user_input)
        
        # for long, more complex responses
        if self.needs_streaming(user_input):
            return self.inference_handler.streaming_inference(user_input)
        
        # For multiple similar requests
        if len(self.reques_queue) > 5:
            responses = await self.inference_handler.batch_inference(self.request_queue)
            self.request_queue.clear() 
            return responses
        
        self.request_queue.append(user_input)
        return await self.inference_handler.basic_inference(user_input)
    
    def is_simple_request(self, request):
        """Determine if request can be handled quickly"""
        # Implementation depends on your use case
        return len(request.split()) < 20
    
    def needs_streaming(self, request):
        """Determine if request needs streaming"""
        # Implementation depends on your use case
        return len(request.split()) > 50