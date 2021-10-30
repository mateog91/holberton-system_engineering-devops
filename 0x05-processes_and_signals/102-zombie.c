#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>
#include <stdio.h>

int infinite_while(void);
/**
 * main function that creates zombie process
 * 
 * @return int 
 */
int main()
{
    pid_t child_pid;
    int i;

    for (i = 0; i < 5; i++)
    {
        child_pid = fork();
        if (child_pid > 0)
        {
            printf("Zombie process created, PID: %i\n", child_pid);
            sleep(1);
        }
        else
            exit(0);
    }

    infinite_while();

    return (0);
}

int infinite_while(void)
{
    while (1)
    {
        sleep(1);
    }
    return (0);
}