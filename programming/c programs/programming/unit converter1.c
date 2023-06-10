#include <stdio.h>

int main()
{
	int loop = 1;

	printf("Welcome to Unit Converter! \n");

	while (loop)
	{
		char category;
		int tempChoice, currencyChoice, massChoice;
		float result, userinput;

		printf("\nHere is a list of conversions to choose from: \n");
		printf("Temperature(T), Currency(C), Mass(M), or exit(E) \n");
		printf("Please enter the letter you want to convert:\n");

		// Read input and clear input buffer

		while (scanf(" %c", &category) != 1 || (category != 'T' && category != 'C' && category != 'M' && category != 'E'))
		{

			// Check if input is valid
			if (category != 'T' && category != 'C' && category != 'M' && category != 'E')
			{
				printf("Invalid input. Please try again.\n");
			}
		}

		switch (category)
		{
		case 'T':
			printf("\nWelcome to Temperature Converter!\n");
			printf("Enter 1 for Fahrenheit to Celsius.\n");
			printf("Enter 2 for Celsius to Fahrenheit.\n");
			// input validation for temperature choice
			while (scanf("%d", &tempChoice) != 1 || (tempChoice != 1 && tempChoice != 2))
			{
				printf("Invalid input. Please enter 1 or 2: ");
				// consume newline character left in the input stream
				getchar();
			}

			printf("Please enter the temperature value: ");

			// input validation for temperature value
			while (scanf("%f", &userinput) != 1)
			{
				printf("Invalid input. Please enter a number: ");
				// consume newline character left in the input stream
				getchar();
			}
			printf("\n");
			if (tempChoice == 1)
			{
				result = (userinput - 32) * (5.0 / 9.0);
				printf("%.2f Fahrenheit is equal to %.2f Celsius.\n", userinput, result);
			}
			else if (tempChoice == 2)
			{
				result = (userinput * 9.0 / 5.0) + 32;
				printf("%.2f Celsius is equal to %.2f Fahrenheit.\n", userinput, result);
			}
			else
			{
				printf("Invalid choice.\n");
			}
			break;
		case 'C':
			printf("\nWelcome to Currency Converter! \n");
			printf("Enter 1 for USD to Euro. \n");
			printf("Enter 2 for USD to JPY. \n");
			printf("Enter 3 for USD to GBP. \n");
			scanf("%d", &currencyChoice);

			// input validation for currency choice
			while (scanf("%d", &currencyChoice) != 1 || (currencyChoice < 1 || currencyChoice > 3))
			{
				printf("Invalid input. Please enter a number between 1 and 3: ");
				// consume newline character left in the input stream
				getchar();
			}
			printf("Please enter the currency amount: ");
			// input validation for currency value
			while (scanf("%f", &userinput) != 1)
			{
				printf("Invalid input. Please enter a number: ");
				// consume newline character left in the input stream
				getchar();
			}
			printf("\n");

			if (currencyChoice == 1)
			{
				result = userinput * 0.92;
				printf("%.2f USD is equal to %.2f EURO\n", userinput, result);
			}
			else if (currencyChoice == 2)
			{
				result = userinput * 111.38;
				printf("%.2f USD is equal to %.2f JPY\n", userinput, result);
			}
			else if (currencyChoice == 3)
			{
				result = userinput * 0.76;
				printf("%.2f USD is equal to %.2f GBP\n", userinput, result);
			}
			else
			{
				printf("Invalid choice.\n");
			}
			break;
		case 'M':
			printf("\nWelcome to Mass Converter!\n");
			printf("Enter 1 for ounces to pounds.\n");
			printf("Enter 2 for grams to pounds.\n");
			// input validation for currency choice
			while (scanf("%d", &massChoice) != 1 || (massChoice < 1 || massChoice > 2))
			{
				printf("Invalid input. Please enter a number between 1 and 3: ");
				// consume newline character left in the input stream
				getchar();
			}
			printf("Please enter the currency amount: ");
			// input validation for currency value
			while (scanf("%f", &userinput) != 1)
			{
				printf("Invalid input. Please enter a number: ");
				// consume newline character left in the input stream
				getchar();
			}
			printf("\n");
			if (massChoice == 1)
			{
				result = userinput / 16.0;
				printf("%.2f ounces is equal to %.2f pounds\n", userinput, result);
			}
			else if (massChoice == 2)
			{
				result = userinput / 453.592;
				printf("%.2f grams is equal to %.2f pounds\n", userinput, result);
			}
			else
			{
				printf("Invalid choice.\n");
			}
			break;
		case 'E':
			loop = 0;
			printf("Goodbye!\n");
			return 0;
		default:
			printf("Invalid choice try again.\n");
			break;
		}
	}
	return 0;
}
