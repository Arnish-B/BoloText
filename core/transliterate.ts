export function toHinglish(input: string): string {
  return input
    .toLowerCase()
    .replace(/मुझे/g, "mujhe")
    .replace(/है/g, "hai")
    .replace(/क्यों/g, "kyon");
}
