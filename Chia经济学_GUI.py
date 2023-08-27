import tkinter as tk
from tkinter import ttk

def calculate():
    global HDD, HDD_price, CNY_revenue_per_oneHDD, Monthly_total,HDD_lable_TB,toTiB,COMPRESS
    HDD = int(e1.get())
    toTiB = float(e2.get())
    COMPRESS = float(e3.get())
    HDD_price = float(e4.get())
    XCHUSDT = float(e5.get())
    USDtoCNY = float(e6.get())
    HDD_lable_TB = int(e7.get())
    XCH_revenue_per_10TiB = float(e8.get())
    addHDD_MODE = addHDD_mode_var.get()
    XCH_revenue_per_thisHDD = (HDD_lable_TB * toTiB / COMPRESS) / 10 * XCH_revenue_per_10TiB
    CNY_revenue_per_oneHDD = XCH_revenue_per_thisHDD * XCHUSDT * USDtoCNY
    Monthly_total = 0

    speed(int(e9.get()), addHDD_MODE)

def speed(mon, addHDD_MODE):
    global HDD, HDD_price, CNY_revenue_per_oneHDD, Monthly_total,HDD_lable_TB,toTiB,COMPRESS
    Monthly_list = []
    this_month = 0
    Remaining_money = 0
    output_str = ""
    for i in range(mon):
        this_month = HDD * 30 * CNY_revenue_per_oneHDD
        Monthly_total += this_month
        output_str += f"——————第{i+1}个月收入：{this_month:.2f}元——————\n"
        output_str += f"CNY_revenue_per_oneHDD={CNY_revenue_per_oneHDD:.2f}\n"

        if addHDD_MODE:
            output_str += f"开启新增算力方案：\n"
            Monthly_list.append(this_month)
            HDD += int((this_month + Remaining_money) / HDD_price)
            output_str += f"总硬盘数量：{HDD}\n"
            output_str += f"总硬盘可用空间：{HDD * HDD_lable_TB * toTiB:.2f}(TiB)\n"
            output_str += f"总算力空间：{HDD * HDD_lable_TB * toTiB / COMPRESS:.2f}(TiB)\n"
            Remaining_money = (this_month + Remaining_money) % HDD_price
            output_str += f"剩余金额：{Remaining_money:.2f}元\n"
        output_str += f"累计总收入：{Monthly_total:.2f}元\n"
        output_str += "\n"
    text_box.delete(1.0, tk.END)
    text_box.insert(tk.END, output_str)

root = tk.Tk()
root.title("Chia Calculator")

# 输入参数的文本框和标签
input_entries = {}
for idx, (label, default_value) in enumerate([
    ("HDD", "65"),
    ("toTiB", "0.9"),
    ("COMPRESS", "0.77"),
    ("HDD_price", "590"),
    ("XCHUSDT", "30"),
    ("USDtoCNY", "7.2"),
    ("HDD_lable_TB", "14"),
    ("XCH_revenue_per_10TiB", "0.00298"),
    ("Months", "12")
]):
    entry = ttk.Entry(root)
    entry.insert(0, default_value)
    entry.grid(row=idx, column=1)
    input_entries[label] = entry
    ttk.Label(root, text=label).grid(row=idx, column=0)

e1, e2, e3, e4, e5, e6, e7, e8, e9 = [
    input_entries[label]
    for label in [
        "HDD", "toTiB", "COMPRESS", "HDD_price", "XCHUSDT", "USDtoCNY",
        "HDD_lable_TB", "XCH_revenue_per_10TiB", "Months"
    ]
]

# addHDD_MODE Checkbutton
addHDD_mode_var = tk.IntVar()
chk = ttk.Checkbutton(root, text="addHDD_MODE", variable=addHDD_mode_var)
chk.grid(row=9, column=0)

# 按钮
ttk.Button(root, text="Calculate", command=calculate).grid(row=10, column=1)

# 输出的文本框
text_box = tk.Text(root, height=15, width=50)
text_box.grid(row=11, columnspan=2)

root.mainloop()
