import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("SeaCalc")
        master.config(bg="#F8FAFF")

        # Membuat variable untuk inputan berupa string
        self.input_string = tk.StringVar()
        # input string akan di set kosong
        self.input_string.set("")

        # Membuat display label Kalkulator
        self.display = tk.Label(master, textvariable=self.input_string, anchor="e", bg="#F8FAFF", font=("Bahnschrift", 32, "bold"), fg="#25265E",)
        self.display.grid(row=0, column=0, columnspan=20, pady=40,padx=20,sticky="nsew")

        # Membuat Button yang ada di Kalkulator
        self.create_buttons()

        # Membuat window dapat diperluas
        master.columnconfigure(0, weight=1)
        master.rowconfigure(0, weight=1)

    # function untuk membuat button
    def create_buttons(self):
        # Membuat Button angka dan Button operator
        button_texts = ["C", "(", ")", "/",
        "7", "8", "9", "*", 
        "4", "5", "6", "-",
        "1", "2", "3", "+",
        ".", "0", "Ce", "=",]
        # Custom background warna yang ada pada button
        button_colors = {
            "7": "#568FB0", "8": "#568FB0", "9": "#568FB0", "/":"#568FB0", 
            "C": "#568FB0", "4": "#568FB0", "5": "#568FB0", 
            "6": "#568FB0", "*":"#568FB0", "Ce":"#568FB0",
            "1": "#568FB0", "2": "#568FB0", "3": "#568FB0", "-":"#568FB0",
            "(":"#568FB0", "0": "#568FB0", ".":"#568FB0", ")":"#568FB0", 
            "+":"#568FB0", "=": "#568FB0"
        }

        # inisialisasi awal variable row dan col
        row = 1
        col = 0

        # Memasukan Button ke dalam row dan column
        # yang ada di button text akan di simpan pada var text
        for text in button_texts:
            # membuat button menggunakan tk.button
            # fungsi ini juga akan mengupdate nilai pada objek input sesuai dengan text pada tombol yang di klik
            button = tk.Button(self.master,font=("Bahnschrift", 16, "bold"), fg="#F8FAFF", bg=button_colors[text] ,text=text, command=lambda t=text: self.update_input(t))
            button.grid(row=row, column=col, sticky="nsew")
            # Col = col + 1, artinya col akan bertambah 1 terus menerus
            col += 1
            # Jika col lebih dari 3 maka . . .
            if col > 3:
                # col = 0, artinya nilai col akan kembali ke 0
                col = 0
                # dan row akan menambah satu
                row += 1
        # perulangan in digunakan untuk membuat display keseluruhan button

        # Perulangan ini digunakan agar button yang dihasilkan  akan resizeable jika di perbesar
        # untuk i, dalam range 1 sampai 4
        for i in range(1, 4):
            # configurasi column dalam objek master
            # parameter i untuk menentukan kolom yang akan di konfigurasi
            # nilai pada weight diatur 1 agar dapat merespon jika tampilan di reposisi
            self.master.columnconfigure(i, weight=1)
        # fungsi yang sama untuk mengatur row
        for i in range(1, 6):
            self.master.rowconfigure(i, weight=1)

    def update_input(self, text):
        # Update display lable jika button di klik

        if text == "=":
            # Error handling untuk pembagian yang tidak memiliki hasil
            try:
                # ini berarti result akan dipanggil menggunakan method get
                # kemudian hasilnya akan di evaluasi dan di bulatkan dengan fungsi round dengan 5 digit di belakang koma
                # dan diubah ke bentuk string
                result = str(round(eval(self.input_string.get()), 5))
            except:
                # jika ada kesalahan maka akan menampilkan error
                result = "Error"

            # kemudian input string akan menampilkan hasil result
            self.input_string.set(result)

        elif text == "C":
            # jika button ini di klik maka input string akan kosong kembali
            self.input_string.set("")
        elif text == "Ce":
            # fungsi ini untuk mengambil karakter terakhir dan memotongnya
            self.input_string.set(self.input_string.get()[:-1])
        else:
            if self.input_string.get() == "":
                # jika input stringnya kosong, maka akan di set dengan text inputan yang baru
                self.input_string.set(text)
            else:
                # jika kondisi diatas tidak terpenuhi, maka
                # akan memanggil input string dengan method get dan ditambahkan dengan text yang baru di inputkan
                self.input_string.set(self.input_string.get() + text)

# memebuat objek root yang dibuat dengan Tkinter
root = tk.Tk()
# memanggil class calculator
calculator = Calculator(root)
# mengatur display windows
root.geometry("380x667")
# untuk menjalankan loop program
root.mainloop()