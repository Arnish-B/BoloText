import { SpeechService } from "../services/speech";
import { toHinglish } from "./transliterate";

export async function runPipeline(speech: SpeechService) {
  const text = await speech.start();
  const hinglish = toHinglish(text);
  return hinglish;
}
