import torch
from sklearn.metrics.pairwise import cosine_similarity
from transformers import BertTokenizer, BertModel, RobertaTokenizer, RobertaModel

MAX_TEXT_LENGTH = 2048

# tokenizer = RobertaTokenizer.from_pretrained('roberta-large')
# model = RobertaModel.from_pretrained('roberta-large')

tokenizer = BertTokenizer.from_pretrained('bert-large-uncased')
model = BertModel.from_pretrained('bert-large-uncased')


def calculate_similarity(text_a, text_b):
    inputs = tokenizer([text_a, text_b], padding=True, truncation=True, return_tensors="pt", max_length=MAX_TEXT_LENGTH)

    with torch.no_grad():
        outputs = model(**inputs)
    embeddings = outputs.last_hidden_state.mean(dim=1)

    # Calculate the cosine similarity between the embeddings
    similarity = cosine_similarity(embeddings[0].reshape(1, -1), embeddings[1].reshape(1, -1))
    return round(similarity[0][0], 2)
