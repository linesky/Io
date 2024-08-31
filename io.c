#include <stdio.h>
#include <windows.h>

int main() {
    HANDLE hLPT;
    DWORD bytesWritten;
    const char *message = "Hello World\n";
    printf("\033c\033[47;30m");
    // Abre a porta LPT1 para escrita
    hLPT = CreateFile("LPT1:",            // Nome do dispositivo
                      GENERIC_WRITE,       // Acesso de escrita
                      0,                   // Modo de compartilhamento
                      NULL,                // Segurança padrão
                      OPEN_EXISTING,       // A porta LPT1 deve existir
                      FILE_ATTRIBUTE_NORMAL, // Atributos padrão
                      NULL);               // Sem modelo de arquivo

    if (hLPT == INVALID_HANDLE_VALUE) {
        printf("error LPT1. chek lpt1 on.\n");
        return 1;
    }

    // Envia a mensagem para LPT1
    if (!WriteFile(hLPT, message, strlen(message), &bytesWritten, NULL)) {
        printf("error write to LPT1.\n");
        CloseHandle(hLPT);
        return 1;
    }

    // Verifica se todos os bytes foram escritos
    if (bytesWritten != strlen(message)) {
        printf("not all bytes send to LPT1.\n");
    }

    // Fecha a porta LPT1
    CloseHandle(hLPT);

    printf("send msg to LPT1 OK.\n");
    return 0;
}

