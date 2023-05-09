#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <unistd.h>
#include <sys/stat.h>

#define BUFFER_SIZE 1024

void error(char *str, const char *message, int code)
{
dprintf(STDERR_FILENO, "%s %s\n", str, message);
exit(code);
}

int main(int argc, char *argv[])
{
size_t br, bw;
char dplace[BUFFER_SIZE];
char str;
char *msg;

 const char *file_to;
 const char *file_from;
FILE *fp_from;
FILE *fp_to;

msg = &str;


file_to = argv[2];
file_from = argv[1];
if (argc != 3)
{
msg = "Usage: cp file_from ";
error(msg, file_to, 97);
}


fp_from = fopen(file_from, "r");
if (fp_from == NULL)
{
msg = "Error: Can't read from file ";
error(msg, file_from, 98);
}

fp_to = fopen(file_to, "w");
if (fp_to == NULL)
{
msg = "Can't write to ";
error(msg, file_to, 99);
}



while ((br = fread(dplace, 1, sizeof(dplace), fp_from)) > 0)
{
   bw = fwrite(dplace, 1, br, fp_to);
        if (bw < br)
		{
msg = "Can't write to ";
error(msg, file_to, 99);
        }
    }

    if (ferror(fp_from))
        {
      msg = "Error: Can't close fd ";
error(msg, file_from, 100);
    }

    if (fclose(fp_from) != 0)
        {
      msg = "Error: Can't close fd ";
error(msg, file_from, 100);
    }

    if (fclose(fp_to) != 0)
        {
       msg = "Error: Can't close fd ";
error(msg, file_from, 100);
    }

    return 0;
}
