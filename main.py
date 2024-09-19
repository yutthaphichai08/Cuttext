import tkinter as tk

def find_common_and_unique_sentences():
    # ดึงข้อความจาก Text widget
    content1 = text_box1.get("1.0", tk.END).strip()
    content2 = text_box2.get("1.0", tk.END).strip()

    # แบ่งข้อความเป็นประโยค
    sentences1 = content1.splitlines()
    sentences2 = content2.splitlines()

    # หาประโยคที่ซ้ำกันโดยรักษาลำดับ
    common_sentences = [sentence for sentence in sentences1 if sentence in sentences2]

    # ประโยคที่ไม่ซ้ำจากช่องที่ 2 โดยไม่รวมประโยคที่ซ้ำจากช่องที่ 3
    unique_sentences = [sentence for sentence in sentences2 if sentence not in common_sentences]

    # แสดงประโยคที่ซ้ำใน Text widget ช่องที่ 3
    common_words_box.delete("1.0", tk.END)  # ล้างข้อความก่อน
    common_words_box.insert(tk.END, "\n".join(common_sentences))  # แสดงประโยคที่ซ้ำ

    # แสดงประโยคที่ไม่ซ้ำใน Text widget ช่องที่ 4
    unique_words_box.delete("1.0", tk.END)  # ล้างข้อความก่อน
    unique_words_box.insert(tk.END, "\n".join(unique_sentences))  # แสดงประโยคที่ไม่ซ้ำ

    # อัปเดตจำนวนประโยค
    word_count_label1.config(text=f"จำนวนประโยคจาก Facebook: {len(sentences1)}")
    word_count_label2.config(text=f"จำนวนประโยคจาก Google Sheet: {len(sentences2)}")
    word_count_label3.config(text=f"จำนวนประโยคที่ซ้ำ: {len(common_sentences)}")
    word_count_label4.config(text=f"จำนวนประโยคที่ไม่ซ้ำจาก Google Sheet: {len(unique_sentences)}")

def copy_common_sentences():
    common_text = common_words_box.get("1.0", tk.END)
    root.clipboard_clear()
    root.clipboard_append(common_text)

def copy_unique_sentences():
    unique_text = unique_words_box.get("1.0", tk.END)
    root.clipboard_clear()
    root.clipboard_append(unique_text)

# สร้างหน้าต่างหลัก
root = tk.Tk()
root.title("โปรแกรมเปรียบเทียบประโยค V.2")
# 18/9/67 time 19.17 PM
# สร้าง Text widget ช่องที่ 1
text_box1 = tk.Text(root, height=10, width=80)
text_box1.pack(pady=10)

# สร้าง Label แสดงจำนวนประโยค ช่องที่ 1
word_count_label1 = tk.Label(root, text="จำนวนประโยคจาก Facebook: 0")
word_count_label1.pack()

# สร้าง Text widget ช่องที่ 2
text_box2 = tk.Text(root, height=10, width=80)
text_box2.pack(pady=10)

# สร้าง Label แสดงจำนวนประโยค ช่องที่ 2
word_count_label2 = tk.Label(root, text="จำนวนประโยคจาก Google Sheet: 0")
word_count_label2.pack()

# สร้าง Text widget ช่องที่ 3 สำหรับแสดงประโยคที่ซ้ำ
common_words_box = tk.Text(root, height=10, width=80)
common_words_box.pack(pady=10)
common_words_box.config(state=tk.NORMAL)  # ให้สามารถแก้ไขได้ (ถ้าต้องการ)

# สร้าง Label แสดงจำนวนประโยค ช่องที่ 3
word_count_label3 = tk.Label(root, text="จำนวนประโยคที่ซ้ำ: 0")
word_count_label3.pack()

# สร้าง Text widget ช่องที่ 4 สำหรับแสดงประโยคที่ไม่ซ้ำจาก Google Sheet
unique_words_box = tk.Text(root, height=10, width=80)
unique_words_box.pack(pady=10)
unique_words_box.config(state=tk.NORMAL)  # ให้สามารถแก้ไขได้ (ถ้าต้องการ)

# สร้าง Label แสดงจำนวนประโยค ช่องที่ 4
word_count_label4 = tk.Label(root, text="จำนวนประโยคที่ไม่ซ้ำจาก Google Sheet: 0")
word_count_label4.pack()

# สร้างปุ่มประมวลผล
process_button = tk.Button(root, text="ประมวลผลประโยคที่ซ้ำและไม่ซ้ำ", command=find_common_and_unique_sentences)
process_button.pack(pady=5)

# สร้างปุ่มคัดลอกประโยคที่ซ้ำ
copy_common_button = tk.Button(root, text="คัดลอกประโยคที่ซ้ำ", command=copy_common_sentences)
copy_common_button.pack(pady=5)

# สร้างปุ่มคัดลอกประโยคที่ไม่ซ้ำ
copy_unique_button = tk.Button(root, text="คัดลอกประโยคที่ไม่ซ้ำ", command=copy_unique_sentences)
copy_unique_button.pack(pady=5)

# เริ่มโปรแกรม
root.mainloop()
