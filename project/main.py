tasks = []
categories = []

def show_menu():
    print("\n=== เมนูหลัก ===")
    print("1. เพิ่มงาน")
    print("2. แสดงงานทั้งหมด")
    print("3. ลบงาน")
    print("4. สรุปจำนวนงานแต่ละประเภท")
    print("5. ออกจากโปรแกรม")

def add_task():
    global tasks, categories
    name = input("กรอกชื่องาน: ")
    category = input("กรอกประเภทงาน (เช่น พืช, สัตว์): ")
    tasks.append(name)
    categories.append(category)
    print("เพิ่มงานเรียบร้อยแล้ว!")

def show_all_tasks():
    global tasks, categories
    if len(tasks) == 0:
        print("ยังไม่มีงานในระบบ")
    else:
        print("\nรายการงานทั้งหมด:")
        for i in range(len(tasks)):
            print(f"{i+1}. {tasks[i]} (ประเภท: {categories[i]})")

def delete_task():
    global tasks, categories
    show_all_tasks()
    if len(tasks) == 0:
        return
    try:
        number = int(input("กรอกเลขลำดับของงานที่ต้องการลบ: "))
        if number >= 1 and number <= len(tasks):
            print(f"ลบงาน: {tasks[number-1]}")
            del tasks[number-1]
            del categories[number-1]
        else:
            print("เลขลำดับไม่ถูกต้อง")
    except:
        print("กรุณากรอกตัวเลขเท่านั้น")

def summarize_tasks():
    global tasks, categories
    if len(tasks) == 0:
        print("ยังไม่มีงานในระบบ")
    else:
        print("\nสรุปจำนวนงานในแต่ละประเภท:")
        summary = {}
        for cat in categories:
            if cat in summary:
                summary[cat] += 1
            else:
                summary[cat] = 1

        for cat in summary:
            print(f"- {cat}: {summary[cat]} งาน")

while True:
    show_menu()
    choice = input("เลือกเมนู (1-5): ")
    if choice == "1":
        add_task()
    elif choice == "2":
        show_all_tasks()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        summarize_tasks()
    elif choice == "5":
        print("ออกจากโปรแกรมแล้ว")
        break
    else:
        print("กรุณาเลือกเลขเมนู 1 ถึง 5 เท่านั้น")