#include <sys/types.h>
#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

/**
 * infinite_while - function that sleeps
 *
 * Return: 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - main program
 *
 * Return: 0 if successful
 */
int main(void)
{
	pid_t i, child_pid;

	for (i = 0; i < 5; i++)
	{
		child_pid = fork();
		if (child_pid == -1)
		{
			perror("fork");
			exit(1);
		}
		else if (child_pid == 0)
		{
			printf("Zombie process created, PID: %d\n", getpid());

			exit(0);
		}
	}
	infinite_while();
}
