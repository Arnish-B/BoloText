# BoloText — Vision & Product Definition

## 1. Core Vision

BoloText exists to eliminate the friction between **how Indians speak** and **how they are forced to type**.

People in India do not communicate in pure Hindi or pure English.  
They speak **Hinglish** — fluid, mixed, fast, and informal.

Yet current tools force users into:
- Hindi script (hard to read in chat)
- English dictation (loses natural phrasing)
- Manual typing (slow and inefficient)

**BoloText bridges this gap.**

> Speak naturally → Get clean, readable Hinglish text → Instantly usable in any app

---

## 2. Problem Statement

### Current Reality

Users:
- Speak in Hindi or Hinglish
- Think in conversational, informal language
- Prefer typing in **English alphabets (Roman script)**

But existing tools:
- Output **Devanagari (Hindi script)** → not preferred in chats
- Struggle with **code-mixed speech**
- Lack seamless integration with **messaging apps like WhatsApp**

### Result

- Users fall back to typing manually
- Voice typing is underutilized
- Communication remains inefficient

---

## 3. Product Definition

BoloText is a:

> **Voice-first Hinglish typing system embedded inside a mobile keyboard**

### Core Flow

User taps mic
→ Speaks naturally (Hindi / Hinglish)
→ Speech is transcribed
→ Text is transliterated into Hinglish (Latin script)
→ Output is inserted into active input field (WhatsApp, etc.)

---

## 4. Key Features (MVP → Future)

### MVP (Phase 1)

- 🎤 Voice input (tap to speak)
- 🧠 Speech-to-text (Hindi / Hinglish)
- 🔤 Transliteration → Hinglish (Latin script)
- 📲 Output directly into any app (keyboard integration)

---

### Phase 2 (Refinement Layer)

- ✍️ Auto punctuation
- 🧹 Filler word removal (“uh”, “matlab”, etc.)
- ⚡ Low-latency streaming transcription
- 📋 Clipboard fallback mode

---

### Phase 3 (Differentiation)

- 🧠 Context-aware corrections
- 🗣️ Tone formatting (casual, formal, etc.)
- 💬 WhatsApp voice note → text conversion
- 🌐 Multi-language expansion (Tamil, Telugu, etc.)

---

## 5. Target Use Cases

### Primary

- WhatsApp messaging
- Casual conversations
- Quick replies

### Secondary

- Notes / journaling
- Social media comments
- Email drafting (informal)

---

## 6. Target Audience

- Indian smartphone users
- Hinglish speakers
- Users who prefer **speed over perfection**
- Users already using voice notes but willing to switch to text

---

## 7. Core Differentiation

BoloText is not just another speech-to-text app.

### It focuses on:

1. **Hinglish output (not Hindi script)**
2. **Messaging-first workflow**
3. **Keyboard-level integration (not separate app usage)**

---

## 8. Technical Philosophy

### Pipeline Architecture

Speech Input
→ ASR (Speech-to-Text)
→ Transliteration Engine
→ Post-processing (punctuation, cleanup)
→ Text Injection (keyboard)

---

### Key Technical Priorities

- Low latency (real-time feel)
- High tolerance for Indian accents
- Accurate transliteration (critical)
- Seamless app integration

---

## 9. Constraints & Challenges

- iOS keyboard limitations (restricted APIs)
- Latency vs accuracy trade-offs
- Handling code-mixed speech reliably
- Transliteration quality (core difficulty)

---

## 10. Success Criteria

BoloText succeeds if:

- Users prefer it over typing manually
- Output “feels natural” without editing
- It integrates invisibly into daily messaging habits

---

## 11. Future Scope

BoloText can extend beyond typing into **real-time conversational intelligence**.

### Potential directions:

- Call transcription → automatic **Moments of Meeting (MoM)** generation  
- Live note-taking during phone calls or meetings  
- Voice → structured summaries (tasks, decisions, highlights)  
- Passive listening mode for quick capture of spoken thoughts  

### Key considerations:

- Requires access to call audio streams (platform restrictions)  
- Strong **privacy and consent mechanisms** are mandatory  
- On-device processing vs cloud trade-offs  
- Legal and compliance implications across regions  

This direction is intentionally **not part of the MVP**, but represents a high-impact expansion path.

---

## 12. Long-Term Vision

BoloText evolves into:

> The default way India types and interacts with text using voice

Future possibilities:

- Voice-native operating layer  
- AI-assisted conversation rewriting  
- Regional language expansion  
- Deep integration with messaging and communication platforms  

---

## 13. One-Line Summary

> BoloText lets users speak naturally and instantly get clean Hinglish text wherever they type.