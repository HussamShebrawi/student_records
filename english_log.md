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

## 2026-09-11 (S9)

### New Words
36. **handler** (n.) — الجزء الذي يتعامل مع حدث أو خطأ. Example: "except FileNotFoundError: is an error handler."
37. **format** (n.) — قالب شكل الرسالة. Example: "format='%(levelname)s - %(message)s'"
38. **level** (n.) — درجة خطورة رسالة الـ logging. Example: "level=logging.DEBUG shows all messages."
39. **stream** (n.) — تدفق البيانات للترمنال أو ملف. Example: "By default, logging streams to the console."
40. **append** (v.) — إضافة للنهاية بدون مسح. Example: "The log file appends every new run."

### Shadowing from my code
"logging.info(f'Cleaned file written successfully: {len(valid_rows)} valid rows saved to {output_filename}')"

### Framed sentence
"The level and format settings in basicConfig decide what gets logged and how it looks, whether the output goes to a stream (console) or a file."

## 2026-09-12 (S10)

### New Words
41. **argument** (n.) — وسيطة / مُدخَل. Example: "--input is an argument passed from the command line."
42. **parser** (n.) — محلّل / قارئ التعليمات. Example: "ArgumentParser is the parser that reads flags."
43. **default** (n.) — القيمة الافتراضية. Example: "default='data/students.csv'"
44. **flag** (n.) — علَم / مؤشّر. Example: "--help is a flag."
45. **summary** (n.) — ملخّص. Example: "print_summary() logs the summary."

### Shadowing from my code
"Clean and validate a CSV file of student records."

### Completions
1. The --input flag has a **default** of data/students.csv.
2. argparse is a **parser** that reads flags from the command line.
3. print_summary() logs a **summary** of total, valid, and invalid rows.

### Free Sentences (E2)
1. "Every argument in my script has a clear name, so the parser can read it without confusion."
2. "When the user forgets to pass a flag, the default value keeps the program running smoothly and the final summary stays correct."

## 2026-09-12 (S11)

### New Words
46. **environment** (n.) — البيئة (السياق الذي يعمل فيه البرنامج). Example: "I created a local **environment** inside .venv to isolate my project's dependencies."
47. **dependency** (n.) — اعتمادية / مكتبة خارجية يعتمد عليها المشروع. Example: "My requirements.txt is currently empty because the project has no external **dependency**."
48. **reproduce** (v.) — يُعيد إنتاج / يُكرّر نفس النتيجة. Example: "The requirements.txt comment explains how to **reproduce** the environment: generate it with `pip freeze > requirements.txt`, then install it elsewhere with `pip install -r requirements.txt`."
49. **resolve** (v.) — يُحلّ / يُحدّد (أي ملف سيُنفَّذ). Example: "When I type `python`, the shell **resolve**s it to /c/Users/PC/Desktop/student_records/.venv/Scripts/python."
50. **ignore** (v.) — يتجاهل. Example: "Because .venv/ is listed in .gitignore, git will **ignore** the whole folder."

### Shadowing from my code
"# .venv/ — Local virtual environment: recreated from requirements.txt; excluded because it holds OS-specific binaries and absolute paths."
".venv/"
"pip 24.3.1 from C:\Users\PC\Desktop\student_records\.venv\Lib\site-packages\pip (python 3.13)"

### Completions
1. Because .venv/ is listed in .gitignore, git will **ignore** the whole folder.
2. pip freeze prints every installed **dependency** with its exact version.
3. The shell **resolve**s a command name to the first matching file in PATH.

### Free Sentences (E2)
1. "Today I learned that .venv/ must be **ignore**d because it contains OS-specific binaries."
2. "The project has zero external dependencies now, so requirements.txt is empty."