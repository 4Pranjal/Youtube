from transformers import WhisperProcessor, WhisperForConditionalGeneration
import librosa

def transcribe_audio(audio_path, model_name="openai/whisper-base"):
    processor = WhisperProcessor.from_pretrained(model_name)
    model = WhisperForConditionalGeneration.from_pretrained(model_name)

    audio, rate = librosa.load(audio_path, sr=16000)
    inputs = processor(audio, sampling_rate=16000, return_tensors="pt")
    input_features = inputs["input_features"]
    generated_ids = model.generate(input_features)
    transcription = processor.decode(generated_ids.sequences[0], skip_special_tokens=True)
    return transcription
