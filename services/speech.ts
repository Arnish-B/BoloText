export interface SpeechService {
  start(): Promise<string>;
}

export class MockSpeechService implements SpeechService {
  async start(): Promise<string> {
    return "mujhe kal meeting attend karni hai";
  }
}
