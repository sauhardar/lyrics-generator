import json
from pprint import pprint
from tensorflow import keras
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
import numpy as np

# read from data.json
data = None
with open('data2.json', 'r') as f:
    data = json.load(f)

corpuses = {}

for artist, artist_data in data.items():
    corpuses[artist] = []
    for song, song_data in artist_data.items():
        sentences = [sentence for sentence in data[artist][song]['lyrics'].split('\n') if len(sentence) > 0][1:]
        corpuses[artist].extend(sentences)

# print(corpuses)

tokenizers = {}

for artist, artist_corpus in corpuses.items():
    tokenizer = Tokenizer()
    tokenizer.fit_on_texts(artist_corpus)
    tokenizers[artist] = tokenizer

input_sequences = {}

for artist, artist_corpus in corpuses.items():
    input_sequences[artist] = []
    for line in artist_corpus:
        token_list = tokenizers[artist].texts_to_sequences([line])[0]
        # print(token_list)
        for i in range(1, len(token_list)):
            n_gram_sequence = token_list[:i+1]
            input_sequences[artist].append(n_gram_sequence)

## Can use this block to check the value of each token in the input sequences

# for artist, artist_sequences in input_sequences.items():
#     for sequence in artist_sequences[:10]:
#         for token in sequence:
#             print(tokenizers[artist].index_word[token])

## Padding sequences for consistent sentence lengths

for artist, artist_sequences in input_sequences.items():
    print(artist)
    max_sequence_len = max([len(sequence) for sequence in artist_sequences])
    padded_artist_sequences = np.array(pad_sequences(artist_sequences, maxlen=max_sequence_len, padding='pre'))
    print(padded_artist_sequences)
    input_sequences[artist] = padded_artist_sequences
