
import tkinter as tk
import os

class GDIApp:
    def __init__(self, root):
        self.root = root
        self.root.title("GDI Data Sender")
        self.root.geometry("300x300")
        self.root.configure(bg='black')

        # Variáveis para as checkboxes
        self.check_vars = [tk.IntVar() for _ in range(8)]

        # Cria checkboxes com nome "data + número"
        for i in range(8):
            cb = tk.Checkbutton(
                root, text=f"data{i}", variable=self.check_vars[i], 
                bg='black', fg='white', command=self.send_data
            )
            cb.pack()

        # Enviar byte inicial de 0x00 para o dispositivo
        self.send_byte(0x00)

    def send_data(self):
        # Constrói o byte a partir do estado das checkboxes
        byte_value = 0
        for i, var in enumerate(self.check_vars):
            byte_value |= (var.get() << i)

        # Envia o byte para o dispositivo
        self.send_byte(byte_value)

    def send_byte(self, byte_value):
        try:
            # Abre o dispositivo /dev/usb/lp0 para escrever
            with open('/dev/usb/lp0', 'wb') as device:
                device.write(byte_value.to_bytes(1, byteorder='big'))
            print(f"Byte enviado: {byte_value:#04x}")
        except FileNotFoundError:
            print(f"Erro: Dispositivo '/dev/usb/lp0' não encontrado.")
        except PermissionError:
            print(f"Erro: Permissão negada para acessar '/dev/usb/lp0'.")

if __name__ == "__main__":
    root = tk.Tk()
    app = GDIApp(root)
    root.mainloop()
