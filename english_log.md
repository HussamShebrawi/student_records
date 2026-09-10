# English Log

## 2026-09-08 (S7)

### New Words
1. **precedence** (n.) — الأسبقية. Example: "EMPTY ROW has precedence over length guard."
2. **duplicate** (adj./n.) — مكرر. Example: "The DUPLICATE ID detector uses a set."
3. **iterator** (n.) — مكرر. Example: "csv.reader returns an iterator."
4. **whitespace** (n.) — مسافة بيضاء. Example: "strip() removes whitespace."
5. **guard** (n.) — حارس/شرط حماية. Example: "The length guard prevents IndexError."

### Shadowing from my code
1. The EMPTY ROW check has **precedence** over the length guard.
2. The **duplicate** detector uses a set() to remember IDs.
3. The strip() method removes all leading and trailing **whitespace**.

### Framed sentence
"When I write validation code, I must give **precedence** to the **guard** checks, or I might get an IndexError when the **iterator** reaches a row with **whitespace** fields or a **duplicate** ID."

## S8

1. writer — a tool that writes rows into a CSV file.
2. valid — a row that passed every detector.
3. output — the cleaned CSV file we write at the end.
4. buffer — a list that holds valid rows before writing.
5. raise — to throw a custom error instead of a raw traceback.