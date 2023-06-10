#include <stdio.h>

#define MAX_SIZE 100
int i;
// Function to display the elements of an array
void display(int arr[], int size)
{
    printf("Array elements are: ");
    for (i = 0; i < size; i++)
    {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

// Function to insert an element at a specific index in an array
int insert(int arr[], int size, int element, int index)
{
    if (index < 0 || index > size)
    {
        return size; // Return current size if index is invalid
    }
    for (i = size - 1; i >= index; i--)
    {
        arr[i + 1] = arr[i]; // Shift elements to right to create space for new element
    }
    arr[index] = element;
    return size + 1; // Return new size
}

// Function to update an element at a specific index in an array
void update(int arr[], int size, int element, int index)
{
    if (index < 0 || index >= size)
    {
        return; // Do nothing if index is invalid
    }
    arr[index] = element;
}

// Function to delete an element at a specific index in an array
int delete(int arr[], int size, int index)
{
    if (index < 0 || index >= size)
    {
        return size; // Return current size if index is invalid
    }
    for (i = index; i < size - 1; i++)
    {
        arr[i] = arr[i + 1]; // Shift elements to left to fill gap left by deleted element
    }
    return size - 1; // Return new size
}

// Function to search for an element in an array
int search(int arr[], int size, int element)
{
    for (i = 0; i < size; i++)
    {
        if (arr[i] == element)
        {
            return i; // Return index of element if found
        }
    }
    return -1; // Return -1 if element not found
}

// Main function to read input and call helper functions
int main()
{
    int arr[MAX_SIZE];
    int size = 0;
    int option = 0;

    do
    {
        printf("\nOperations on 1D-Array:\n");
        printf("1. Insert\n");
        printf("2. Update\n");
        printf("3. Delete\n");
        printf("4. Display\n");
        printf("5. Search\n");
        printf("6. Exit\n");
        printf("Enter your choice (1-6): ");
        scanf("%d", &option);

        switch (option)
        {
        case 1:
        {
            int element, index;
            printf("Enter element to insert: ");
            scanf("%d", &element);
            printf("Enter index to insert at: ");
            scanf("%d", &index);
            size = insert(arr, size, element, index);
            printf("New size of array is %d\n", size);
            break;
        }
        case 2:
        {
            int element, index;
            printf("Enter element to update: ");
            scanf("%d", &element);
            printf("Enter index to update at: ");
            scanf("%d", &index);
            update(arr, size, element, index);
            printf("Array updated successfully\n");
            break;
        }
        case 3:
        {
            int element, index;
            printf("Enter element to update: ");
            scanf("%d", &element);
            printf("Enter index to update at: ");
            scanf("%d", &index);
            delete (arr, size, index);
            printf("Array updated successfully\n");
            break;
        }
        case 4:
        {
            int element, index;
            printf("Enter element to update: ");
            scanf("%d", &element);
            printf("Enter index to update at: ");
            scanf("%d", &index);
            display(arr, size);
            printf("Array updated successfully\n");
            break;
        }
        case 5:
        {
            int element, index;
            printf("Enter element to update: ");
            scanf("%d", &element);
            printf("Enter index to update at: ");
            scanf("%d", &index);
            search(arr, size, element);
            printf("Array updated successfully\n");
            break;
        }
        case 6:
        {
            return 0;
            break;
        }
        default:
        {
            printf("Invalid input.");
            break;
        }
        }
    } while (1);
    return 0;
}
