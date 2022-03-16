#include <stdio.h>

void merge(int *Arr, int start, int mid, int end)
{
	int temp[end - start + 1];

	int i = start, j = mid+1, k = 0;

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

	while(i <= mid) {
		temp[k] = Arr[i];
		k += 1; i += 1;
	}

	while(j <= end) {
		temp[k] = Arr[j];
		k += 1; j += 1;
	}

	for(i = start; i <= end; i += 1) 
    {
		Arr[i] = temp[i - start];
	}
}

void mergeSort(int *Arr, int start, int end) {

	if(start < end) {
		int mid = (start + end) / 2;
		mergeSort(Arr, start, mid);
		mergeSort(Arr, mid+1, end);
		merge(Arr, start, mid, end);
	}
}

unsigned int findMax(unsigned int a, unsigned int b)
{
	if (a > b)
	{
		return a;
	}
	else
	{
		return b;
	}
}

void solve(unsigned int* arr, unsigned int len, unsigned int l)
{
	unsigned int max;
	max = 2 * findMax(arr[0], l - arr[len - 1]);

	for (unsigned int i = 1 ; i < len ; i = i + 1)
	{
		max = findMax(max, arr[i] - arr[i - 1]);
	}

	printf("%f\n", max * 1.0 / 2);
}

int main(void)
{
    unsigned int n, l;
    scanf("%u%u", &n, &l);

    unsigned int a[n + 1];
    for (unsigned int i = 0 ; i < n ; i = i + 1)
    {
        scanf("%u", &a[i]);
    }

    mergeSort(a, 0, n - 1);

    solve(a, n, l);
}