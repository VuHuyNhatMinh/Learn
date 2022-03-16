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

int max(int x, int y)
{
    if (x >= y)
    {
        return x;
    }
    else
    {
        return y;
    }
}

void solve()
{
    unsigned int n;
    scanf("%u", &n);

    int a[n + 1];
    for(unsigned int i = 0 ; i < n ; i = i + 1)
    {
        scanf("%d", &a[i]);
    }

    mergeSort(a, 0, n - 1);

    int res = a[0];
    for (unsigned int i = 1 ; i < n ; i = i + 1)
    {
        res = max(res, a[i] - a[i - 1]);
    }

    printf("%d\n", res);
}

int main(void)
{
    unsigned int t;
    scanf("%u", &t);
    while (t > 0)
    {
        t = t - 1;
        solve();
    }
}