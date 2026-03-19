# BoloText PoC - Voice to Hinglish Converter

## Quick Start

### 1. Create Virtual Environment

```bash
# Navigate to project directory
cd /Users/dominus/Documents/Arnish/Dev/BoloText

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate
```

**Note:** You'll see `(venv)` prefix in your terminal when activated.

To deactivate later:
```bash
deactivate
```

### 2. Install Dependencies

Make sure your virtual environment is activated, then:

```bash
pip install -r requirements_poc.txt
```

**Note:** First run will download the Whisper model (~150MB for base model)

### 3. Run the PoC

```bash
python poc_voice_to_hinglish.py
```

### 4. Test It

- Choose option 1 to record for 5 seconds
- Speak in Hindi, Hinglish, or code-mixed (e.g., "Yaar mujhe kal meeting mein jana hai")
- See the output in Roman script!

---

## How It Works

```
Your Voice (Hindi/Hinglish)
    ↓
🎤 Audio Recording (sounddevice)
    ↓
🧠 Speech-to-Text (Whisper AI)
    ↓
    Output: Text in Devanagari + English
    ↓
🔤 Transliteration (indic-transliteration)
    ↓
✨ Final: Clean Hinglish in Roman Script
```

---

## Model Options

You can change the Whisper model size in the script:

- `tiny` - Fastest, least accurate (~75MB)
- `base` - **Default**, good balance (~150MB)
- `small` - Better accuracy (~500MB)
- `medium` - High accuracy (~1.5GB)
- `large` - Best accuracy (~3GB)

Edit line 134:
```python
converter = VoiceToHinglish(model_size="base")
```

---

## Test Phrases

Try these to validate accuracy:

1. **Pure Hindi**: "मुझे आज बाजार जाना है"
2. **Pure Hinglish**: "Yaar kal meeting hai na?"
3. **Code-mixed**: "Aaj weather kaisa hai? Mujhe lagta hai barish hogi"
4. **Complex**: "Boss ne bola ki presentation ready rakho by evening"

---

## Expected Output Format

**Input (spoken):** "Yaar mujhe kal meeting mein jana hai"

**Step 1 - Whisper Output (Devanagari):** "यार मुझे कल मीटिंग में जाना है"

**Step 2 - Transliteration (Roman):** "yaar mujhe kal meeting mein jana hai"

---

## Troubleshooting

### SSL Certificate Error (macOS)
If you see `SSL: CERTIFICATE_VERIFY_FAILED` error:

**Solution:** The script now includes an automatic SSL workaround. If it still fails:
```bash
# Option 1: Run the certificate installer
/Applications/Python\ 3.*/Install\ Certificates.command

# Option 2: Use the helper script
python download_model.py
```

### No microphone detected
- Check system audio permissions
- Verify your mic is working: `python -m sounddevice`

### Poor transcription quality
- Speak clearly and at moderate pace
- Try a larger model (`small` or `medium`)
- Reduce background noise

### FFmpeg not needed
This PoC passes audio data directly to Whisper, so ffmpeg is NOT required for basic functionality.

### Module not found errors
- Ensure all dependencies installed: `pip install -r requirements_poc.txt`
- Use a virtual environment if needed

---

## Next Steps After Validation

Once this PoC proves the concept:

1. ✅ Validates ASR accuracy for Hinglish
2. ✅ Confirms transliteration quality
3. ✅ Measures latency

Then move to:
- Android keyboard integration
- Optimize for mobile (model size, latency)
- Add post-processing (punctuation, filler removal)
- Build the full BoloText keyboard app

---

## Sample Models ( already existing )
- https://huggingface.co/Oriserve/Whisper-Hindi2Hinglish-Apex