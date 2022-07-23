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
			break;
		else if (child_pid == 0)
			exit(0);
		else
			printf("Zombie process created, PID: %d\n", child_pid);
	}
	infinite_while();
	return (0);
}
