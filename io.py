
import os

def send_to_lpt1(message):
    try:
        # Abre o dispositivo LPT1 para escrita
        with open("LPT1:", "w") as lpt:
            lpt.write(message)
        print("send message to LPT1 .")
    except FileNotFoundError:
        print("Error: LPT1 not find. check conection.")
    except PermissionError:
        print("Erro: not acess to LPT1.")
    except Exception as e:
        print(f"Error on send message LPT1: {e}")

if __name__ == "__main__":
    print("\033c\033[47;30m")
    send_to_lpt1("Hello World\n")
