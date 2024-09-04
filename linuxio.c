
#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <unistd.h>

int main() {
    // Define o caminho para o dispositivo LPT1
    const char *device = "/dev/lp0";
    const char *message = "Hello World\n";
    printf("\033[40;37m");
    // Abre o dispositivo em modo de escrita
    int fd = open(device, O_WRONLY);
    if (fd == -1) {
        perror("Error open  LPT1");
        return 1;
    }

    // Envia a mensagem para LPT1
    if (write(fd, message, sizeof(message)) == -1) {
        perror("Error sending message LPT1");
        close(fd);
        return 1;
    }

    // Fecha o dispositivo
    close(fd);

    printf("message send LPT1 ok.\n");
    return 0;
}
