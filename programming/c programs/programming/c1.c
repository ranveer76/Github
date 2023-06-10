#include <stdio.h>
#include <stdbool.h>

int main()
{
    int np, nr, i, j, MP, MR;
    // np = number of processes, nr = number of resources, MP = maximum number of processes and MR = maximum number of resources
    printf("Enter the maximum number of processes: ");
    scanf("%d", &MP);

    printf("Enter the maximum number of resources: ");
    scanf("%d", &MR);

    // all = allocation matrix, mn = max need matrix, avail = available vector, need = need matrix, safe = safe sequence
    bool fin[MP];
    int all[MP][MR], mn[MP][MR], avail[MR], need[MP][MR], safe[MP];
    printf("Enter the number of processes: ");
    scanf("%d", &np);

    printf("Enter the number of resources: ");
    scanf("%d", &nr);

    printf("Enter the allocation matrix:\n");
    for (i = 0; i < np; i++)
    {
        for (j = 0; j < nr; j++)
        {
            scanf("%d", &all[i][j]);
        }
    }

    printf("Enter the max need matrix:\n");
    for (i = 0; i < np; i++)
    {
        for (j = 0; j < nr; j++)
        {
            scanf("%d", &mn[i][j]);
            need[i][j] = mn[i][j] - all[i][j];
        }
        fin[i] = false;
    }

    printf("Enter the available vector:\n");
    for (i = 0; i < nr; i++)
    {
        scanf("%d", &avail[i]);
    }

    int count = 0;
    bool is = true; // is = is safe

    while (count < np)
    {
        bool found = false;

        for (i = 0; i < np; i++)
        {
            if (!fin[i])
            {
                bool possible = true;

                for (j = 0; j < nr; j++)
                {
                    if (need[i][j] > avail[j])
                    {
                        possible = false;
                        break;
                    }
                }

                if (possible)
                {
                    for (j = 0; j < nr; j++)
                    {
                        avail[j] += all[i][j];
                    }
                    safe[count++] = i;
                    fin[i] = true;
                    found = true;
                }
            }
        }

        if (!found)
        {
            is = false;
            break;
        }
    }

    if (is)
    {
        printf("Safe sequence: ");
        for (i = 0; i < np; i++)
        {
            printf("%d ", safe[i]);
        }
        printf("\n");
    }
    else
    {
        printf("Unsafe state\n");
    }

    return 0;
}