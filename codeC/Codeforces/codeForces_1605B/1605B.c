#include <stdio.h>

void merge(int *Arr, int start, int mid, int end)
{
	// create a temp array
	int temp[end - start + 1];

	// crawlers for both intervals and for temp
	int i = start, j = mid+1, k = 0;

	// traverse both arrays and in each iteration add smaller of both elements in temp 
	while(i <= mid && j <= end) {
		if(Arr[i] <= Arr[j]) {
			temp[k] = Arr[i];
			k += 1; i += 1;
		}
		else {
			temp[k] = Arr[j];
			k += 1; j += 1;
		}
	}

	// add elements left in the first interval 
	while(i <= mid) {
		temp[k] = Arr[i];
		k += 1; i += 1;
	}

	// add elements left in the second interval 
	while(j <= end) {
		temp[k] = Arr[j];
		k += 1; j += 1;
	}

	// copy temp to original interval
	for(i = start; i <= end; i += 1) 
    {
		Arr[i] = temp[i - start];
	}
}

// Arr is an array of integer type
// start and end are the starting and ending index of current interval of Arr

void mergeSort(int *Arr, int start, int end) {

	if(start < end) {
		int mid = (start + end) / 2;
		mergeSort(Arr, start, mid);
		mergeSort(Arr, mid+1, end);
		merge(Arr, start, mid, end);
	}
}

void push(unsigned int i, unsigned int* a, unsigned int* len)
{
    a[*len] = i;
    *len = *len + 1;
}

void solve()
{
    unsigned int n;
    scanf("%u", &n);

    char s[n + 1];
    scanf("%s", s);

    unsigned int i, j;
    i = 0; 
    j = n - 1; 
    unsigned int a[n + 1];
    unsigned int len = 0; 
    for (; i < n ; i = i + 1)
    {
        if (s[i] == '1')
        {
            for (; j > i ; j = j - 1)
            {
                if (s[j] == '0')
                {
                    push(i + 1, a, &len);
                    push(j + 1, a, &len);
                    j = j - 1;
                    break;
                }
            }
        }

        if (i >= j)
        {
            break;
        }
    }

    mergeSort(a, 0, len - 1);

    if (len > 0)
    {
        printf("1\n");
    }
    printf("%u ", len);
    for (i = 0 ; i < len ; i = i + 1)
    {
        printf("%u ", a[i]);
    }
    printf("\n");
}

int main(void)
{
    unsigned int t;
    scanf("%u", &t);
    while (t > 0)
    {
        solve();
        t = t - 1;
    }
}