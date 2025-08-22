import os
import re

# Thư mục gốc (chính là thư mục đang chạy script)
SRC_DIR = "."

# Domain gốc cần thay
OLD_DOMAIN = r"https://thebloomhair.com/"

# Regex: match link bắt đầu từ domain gốc
pattern = re.compile(rf"{OLD_DOMAIN}([^\s\"')]+)", re.IGNORECASE)

def replace_links_in_file(filepath):
    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

    # Bỏ domain, chỉ giữ lại path local
    new_content, count = pattern.subn(lambda m: m.group(1), content)

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
