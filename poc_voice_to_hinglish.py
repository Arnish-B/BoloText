#!/usr/bin/env python3
"""
BoloText PoC: Voice to Hinglish Converter
Records audio from microphone and converts Hindi/Hinglish speech to Roman script
"""

import os
import sys
import wave
import numpy as np
from datetime import datetime
import ssl

# SSL workaround for macOS certificate issues when downloading Whisper model
ssl._create_default_https_context = ssl._create_unverified_context

try:
    import sounddevice as sd
    import whisper
    from indic_transliteration import sanscript
    from indic_transliteration.sanscript import transliterate
except ImportError as e:
    print(f"Missing dependency: {e}")
    print("\nPlease install required packages:")
    print("pip install sounddevice openai-whisper indic-transliteration numpy scipy")
    sys.exit(1)


class VoiceToHinglish:
    def __init__(self, model_size="base"):
        """
        Initialize the voice to Hinglish converter

        Args:
            model_size: Whisper model size (tiny, base, small, medium, large)
                       'base' is a good balance of speed and accuracy
        """
        print(f"Loading Whisper model ({model_size})...")
        self.whisper_model = whisper.load_model(model_size)

        # Audio recording parameters
        self.sample_rate = 16000  # Whisper uses 16kHz
        self.channels = 1  # Mono audio

        print("✓ Initialization complete!\n")

    def record_audio(self, duration=5):
        """
        Record audio from the microphone

        Args:
            duration: Recording duration in seconds

        Returns:
            numpy array of audio data
        """
        print(f"🎤 Recording for {duration} seconds...")
        print("Speak now in Hindi/Hinglish!")
        print("TIP: Speak clearly and a bit slowly for better accuracy")
        print("-" * 40)

        # Record audio
        audio_data = sd.rec(
            int(duration * self.sample_rate),
            samplerate=self.sample_rate,
            channels=self.channels,
            dtype='float32'
        )
        sd.wait()  # Wait until recording is finished

        print("✓ Recording complete!")

        # Check audio quality
        max_amplitude = np.max(np.abs(audio_data))
        print(f"   Max amplitude: {max_amplitude:.3f} (should be > 0.01)")
        if max_amplitude < 0.01:
            print("   ⚠️  WARNING: Audio seems very quiet! Speak louder or check mic.")

        return audio_data.flatten()

    def save_audio(self, audio_data, filename="temp_recording.wav"):
        """
        Save audio data to a WAV file (for Whisper processing)

        Args:
            audio_data: numpy array of audio data
            filename: output filename

        Returns:
            path to saved file
        """
        filepath = os.path.join(os.path.dirname(__file__), filename)

        # Convert float32 to int16 for WAV file
        audio_int16 = (audio_data * 32767).astype(np.int16)

        with wave.open(filepath, 'w') as wf:
            wf.setnchannels(self.channels)
            wf.setsampwidth(2)  # 2 bytes for int16
            wf.setframerate(self.sample_rate)
            wf.writeframes(audio_int16.tobytes())

        return filepath

    def transcribe(self, audio_data):
        """
        Transcribe audio using Whisper

        Args:
            audio_data: numpy array of audio data (float32)

        Returns:
            dict with transcription results
        """
        print("\n🧠 Transcribing audio...")

        # Whisper can accept numpy arrays directly (no ffmpeg needed)
        # Audio should be float32 between -1 and 1, at 16kHz
        result = self.whisper_model.transcribe(
            audio_data,
            language='hi',  # Hindi language code
            task='transcribe',
            fp16=False,  # Use FP32 for CPU compatibility
            initial_prompt="यह एक Hinglish वाक्य है।",  # Hint for Hinglish context
            temperature=0.0,  # More deterministic output
            beam_size=5  # Better beam search for accuracy
        )

        return result

    def transliterate_to_roman(self, text):
        """
        Convert Devanagari text to Roman script (Hinglish)

        Args:
            text: Input text (may contain Hindi in Devanagari)

        Returns:
            Transliterated text in Roman script
        """
        print("🔤 Transliterating to Roman script...")

        # Try multiple transliteration schemes for comparison
        # ISO is more readable than ITRANS for natural Hinglish
        result_itrans = transliterate(text, sanscript.DEVANAGARI, sanscript.ITRANS)
        result_iso = transliterate(text, sanscript.DEVANAGARI, sanscript.ISO)

        print(f"   ITRANS: {result_itrans}")
        print(f"   ISO: {result_iso}")

        # Return ISO as it's more natural
        return result_iso

    def process(self, duration=5):
        """
        Complete pipeline: Record -> Transcribe -> Transliterate

        Args:
            duration: Recording duration in seconds

        Returns:
            Final Hinglish text in Roman script
        """
        # Step 1: Record audio
        audio_data = self.record_audio(duration)

        # Step 2: Transcribe using Whisper (pass numpy array directly, no ffmpeg needed)
        transcription_result = self.transcribe(audio_data)

        # Extract the transcribed text
        devanagari_text = transcription_result['text']
        detected_language = transcription_result.get('language', 'unknown')

        print(f"\n📝 Transcription (Devanagari):")
        print(f"   Language: {detected_language}")
        print(f"   Text: {devanagari_text}")

        # Step 3: Transliterate to Roman script
        hinglish_text = self.transliterate_to_roman(devanagari_text)

        print(f"\n✨ Final Output (Hinglish):")
        print(f"   {hinglish_text}")

        return hinglish_text


def main():
    print("="*60)
    print("BoloText PoC - Voice to Hinglish Converter")
    print("="*60)
    print()

    # Ask user for model size
    print("Choose Whisper model size:")
    print("1. tiny   (~75MB)  - Fastest, least accurate")
    print("2. base   (~150MB) - Good balance [RECOMMENDED]")
    print("3. small  (~500MB) - Better accuracy")
    print("4. medium (~1.5GB) - High accuracy")

    model_choice = input("\nEnter choice (1-4) [default: 2]: ").strip()

    model_map = {
        "1": "tiny",
        "2": "base",
        "3": "small",
        "4": "medium",
        "": "base"  # default
    }

    model_size = model_map.get(model_choice, "base")
    print()

    # Initialize the converter
    converter = VoiceToHinglish(model_size=model_size)

    while True:
        print("\n" + "="*60)
        print("Options:")
        print("1. Record and convert (5 seconds)")
        print("2. Record and convert (10 seconds)")
        print("3. Record and convert (custom duration)")
        print("4. Exit")
        print("="*60)

        choice = input("\nEnter your choice (1-4): ").strip()

        if choice == "1":
            converter.process(duration=5)
        elif choice == "2":
            converter.process(duration=10)
        elif choice == "3":
            try:
                duration = int(input("Enter duration in seconds: "))
                converter.process(duration=duration)
            except ValueError:
                print("Invalid duration. Please enter a number.")
        elif choice == "4":
            print("\nGoodbye! 👋")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
