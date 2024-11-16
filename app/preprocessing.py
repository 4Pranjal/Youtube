import pandas as pd
import spacy

def load_and_preprocess(file_path, top_n=1000):
    """Load dataset and preprocess the lyrics."""
    nlp = spacy.load('en_core_web_sm')

    def preprocess_text_spacy(text):
        doc = nlp(text.lower())
        tokens = [token.lemma_ for token in doc if not token.is_stop and not token.is_punct]
        return ' '.join(tokens)

    df = pd.read_csv(file_path)
    df['cleaned_lyrics'] = df['lyrics'].apply(preprocess_text_spacy)
    return df.nlargest(top_n, 'views')
