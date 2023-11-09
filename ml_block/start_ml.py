#TODO make some code

from transformers import T5Tokenizer, T5ForConditionalGeneration

tokenizer = T5Tokenizer.from_pretrained("laituan245/molt5-large-caption2smiles", model_max_length=512)
model = T5ForConditionalGeneration.from_pretrained('laituan245/molt5-large-caption2smiles')

def generate_text(prompt: str) -> str:
  input_ids = tokenizer(prompt, return_tensors="pt").input_ids
  outputs = model.generate(input_ids, num_beams=5, max_length=512)
  
  smiles = tokenizer.decode(outputs[0], skip_special_tokens=True)
  
  return smiles
  