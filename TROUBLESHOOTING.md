# BoloText PoC - Troubleshooting Poor Results

## If you're getting gibberish output, here's what to try:

### 1. Check the Devanagari Output First
Look at the "📝 Transcription (Devanagari)" line in the output.

**If the Devanagari is wrong:**
→ Problem is with Whisper transcription (ASR)

**If Devanagari is correct but Roman output is wrong:**
→ Problem is with transliteration

---

## Fixes for Poor Transcription

### Issue 1: Whisper Not Understanding Your Speech

**Solutions:**
1. **Use a larger model** - The script now asks you to choose:
   - Try `small` (500MB) for much better accuracy
   - Or `medium` (1.5GB) for best results

2. **Speak more clearly:**
   - Speak at moderate pace (not too fast)
   - Enunciate words clearly
   - Reduce background noise
   - Speak a bit louder (check the amplitude warning)

3. **Check microphone:**
   ```bash
   python -m sounddevice
   ```
   Make sure your default input device is correct

### Issue 2: Model Not Recognizing Hinglish

The updated script now:
- ✅ Adds Hinglish context hint to Whisper
- ✅ Uses better beam search (beam_size=5)
- ✅ More deterministic output (temperature=0.0)

---

## Fixes for Poor Transliteration

The script now shows **two transliteration schemes**:
- **ITRANS** - Technical (e.g., "jnaana")
- **ISO** - More natural (e.g., "jñāna")

**Current default: ISO**

If neither looks good, the problem is likely in the Whisper transcription step.

---

## Testing Steps

1. **Run the script:**
   ```bash
   source venv/bin/activate
   python poc_voice_to_hinglish.py
   ```

2. **Choose model size:**
   - Start with option 2 (base)
   - If results are bad, try option 3 (small)

3. **Test with clear phrases:**
   - "namaste dost"
   - "main kal office jaa raha hoon"
   - "aaj mausam kaisa hai"

4. **Check the complete output:**
   ```
   📝 Transcription (Devanagari): [Look at this first!]
      Language: hi
      Text: यार कल मुझे ऑफिस जाना है

   🔤 Transliterating to Roman script...
      ITRANS: yAra kala mujhe APhisa jAnA hai
      ISO: yāra kala mujhe ophisa jānā hai

   ✨ Final Output (Hinglish):
      yāra kala mujhe ophisa jānā hai
   ```

5. **Report back what you see:**
   - Is the Devanagari correct?
   - Which transliteration scheme looks better?
   - What's the max amplitude value?

---

## Common Issues

### Cyrillic or random characters appearing
→ Whisper is confused about language. Try:
- Larger model (small/medium)
- Speaking more clearly
- Better microphone

### Output is close but has weird characters (ā, ṇ, etc.)
→ That's the ISO scheme with diacritics. It's technically correct but you might prefer ITRANS.

### Silent or very quiet recording
→ Check the "Max amplitude" value. Should be > 0.01
- Increase mic volume
- Speak louder
- Check system audio permissions

---

## What to Report

Please test again and share:
1. Which model size you used
2. What you spoke (in English)
3. The **Devanagari output** (📝 line)
4. The final Hinglish output
5. Max amplitude value

This will help identify exactly where the issue is!
