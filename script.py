# Load model directly
from transformers import AutoTokenizer, AutoModelForCausalLM
from transformers import pipeline

tokenizer = AutoTokenizer.from_pretrained("AUTOMATIC/promptgen-lexart")
model = AutoModelForCausalLM.from_pretrained("AUTOMATIC/promptgen-lexart")


