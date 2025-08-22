import os
import re

SRC_DIR = "."
OLD_DOMAIN = r"https://thebloomhair.com/"

# Regex: match domain gốc hoặc relative dẫn tới wp-content
pattern = re.compile(rf"(?:{OLD_DOMAIN}|(\.\./)*)wp-content/uploads/([^\s\"')]+)", re.IGNORECASE)

def replace_links_in_file(filepath):
    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

    # Luôn thay thành absolute từ root
    new_content, count = pattern.subn(lambda m: f"/wp-content/uploads/{m.group(2)}", content)

    if count > 0:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"✔ Đã sửa {count} link trong {filepath}")

def main():
    for root, dirs, files in os.walk(SRC_DIR):
        for file in files:
            if file.endswith((".html", ".css", ".js")):
                replace_links_in_file(os.path.join(root, file))

if __name__ == "__main__":
    main()
