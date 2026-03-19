#!/usr/bin/env python3
"""
Simple audio recorder that captures microphone input and saves as WAV file.
"""

import sounddevice as sd
import numpy as np
from scipy.io import wavfile
import os
from datetime import datetime

# Recording parameters
SAMPLE_RATE = 44100  # Hz (CD quality)
CHANNELS = 1  # Mono recording
DTYPE = np.int16  # 16-bit audio

# Output directory
OUTPUT_DIR = "Sample Recordings"


def record_audio(duration_seconds: int = 5):
    """
    Record audio from the microphone for specified duration.

    Args:
        duration_seconds: How long to record in seconds (default: 5)
    """
    print(f"\nRecording for {duration_seconds} seconds...")
    print("Speak into your microphone now!\n")

    # Record audio
    audio_data = sd.rec(
        int(duration_seconds * SAMPLE_RATE),
        samplerate=SAMPLE_RATE,
        channels=CHANNELS,
        dtype=DTYPE
    )

    # Wait for recording to complete
    sd.wait()

    print("Recording finished!\n")
    return audio_data


def save_audio(audio_data, output_dir: str = OUTPUT_DIR):
    """
    Save recorded audio to a WAV file with timestamp.

    Args:
        audio_data: NumPy array containing audio data
        output_dir: Directory to save the file
    """
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Generate filename with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"recording_{timestamp}.wav"
    filepath = os.path.join(output_dir, filename)

    # Save as WAV file
    wavfile.write(filepath, SAMPLE_RATE, audio_data)

    print(f"✓ Audio saved to: {filepath}")
    return filepath


def main():
    """Main function to run the audio recorder."""
    print("=" * 50)
    print("Audio Recorder")
    print("=" * 50)

    # Get duration from user
    try:
        duration = input("Enter recording duration in seconds (default: 5): ")
        duration = int(duration) if duration.strip() else 5
    except ValueError:
        print("Invalid input. Using default duration of 5 seconds.")
        duration = 5

    # Record audio
    audio_data = record_audio(duration)

    # Save audio
    save_audio(audio_data)

    print("\nDone!")


if __name__ == "__main__":
    main()
