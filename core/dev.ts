import { MockSpeechService } from "../services/speech";
import { runPipeline } from "./pipeline";

(async () => {
  const result = await runPipeline(new MockSpeechService());
  console.log("OUTPUT:", result);
})();
