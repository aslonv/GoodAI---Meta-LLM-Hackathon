from llama import Llama

def initialize_model():
    model = Llama(
        model_path="path/to/model/weights",
        n_ctx=2048, 
        n_threads=4
    )
    return model 

def generate_response(model, prompt, max_tokens=100):
    response = model.generate(
        prompt,
        max_tokens=max_tokens,
        temperature=0.7,
        top_p=0.9
    )
    return response 

