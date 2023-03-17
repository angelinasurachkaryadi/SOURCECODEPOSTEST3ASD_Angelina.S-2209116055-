class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class ToDoList:
    def __init__(self):
        self.head = None
        self.history = []
        
    def add_task(self, task):
        new_node = Node(task)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self.history.append(f"Tugas/Kegiatan'{task}' Ditambahkan Ke Daftar To Do List.")

    def remove_task(self, task):
        if self.head is None:
            return
        if self.head.data == task:
            self.head = self.head.next
            self.history.append(f"Tugas/Kegiatan '{task}' Telah Dihapus.")
            return
        current = self.head
        while current.next is not None:
            if current.next.data == task:
                current.next = current.next.next
                self.history.append(f"Tugas/Kegiatan '{task}' Telah Dihapus.")
                return
            current = current.next

    def display_tasks(self):
        if self.head is None:
            print("Maaf! Tidak Ada Daftar Tugas/Kegiatan =>")
        else:
            current = self.head
            print("Daftar Tugas/Kegiatan Anda => ")
            while current is not None:
                print(f" - {current.data}")
                current = current.next
    
    def display_history(self):
        print("History To Do List => ")
        for riwayat in self.history:
            print(f"- {riwayat}")

todo_list = ToDoList()

while True:
    print("\n###########################################")
    print("\n##### <<<<< APLIKASI TO DO LIST >>>>> #####")
    print("\n###########################################")
    print("(1). Tambah Daftar Tugas/Kegiatan ")
    print("(2). Tampilkan Daftar Tugas/Kegiatan ")
    print("(3). Hapus Daftar Tugas/Kegiatan")
    print("(4). Tampilkan History To Do List ")
    print("(5). Keluar")
    pilih = input("Pilih Sesuai Yang Di Inginkan (1-5) => ")
    
    if pilih == "1":
        task = input("Masukkan Tugas/Kegiatan Baru => ")
        todo_list.add_task(task)
        print(f"Tugas/Kegiatan '{task}' Anda Sudah Ditambahkan.")
    elif pilih == "2":
         todo_list.display_tasks()
    elif pilih == "3":
        task = input("Tugas/Kegiatan Yang Ingin Dihapus => ")
        todo_list.remove_task(task)
        print(f"Tugas/Kegiatan '{task}' Anda berhasil dihapus.")
    elif pilih == "4":
        todo_list.display_history()
    elif pilih == "5":
        print("##################################################")
        print("Terimakasih Sudah Menggunakan Aplikasi To do list!")
        print("##################################################")
        break
    else :
        print("##############################################")
        print("Pilihan Tidak Tersedia,Silahkan Coba Kembali. ")
        print("##############################################")



