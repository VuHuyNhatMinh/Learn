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

int main(void)
{
    unsigned int n;
    scanf("%u", &n);
    
    unsigned int x[n];
    for(unsigned int i = 0 ; i < n ; i = i + 1)
    {
        scanf("%u", &x[i]);
    }

    mergeSort(x, 0, n - 1);

    unsigned int q;
    scanf("%u", &q);
    for(unsigned int i = 0 ; i < q ; i = i + 1)
    {
        unsigned int temp;
        scanf("%u", &temp);
        unsigned int res = 0;
        for(unsigned int j = 0 ; j < n ; j = j + 1)
        {
            if (temp >= x[j])
            {
                res = res + 1;
            }
            else
            {
                break;
            }
        }
        printf("%u\n", res);
    }
}