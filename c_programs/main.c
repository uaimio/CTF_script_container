#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

void rotate(int* nums, int numsSize, int k) {
	k = k % numsSize;
	if (k == 0) {
		return;
	}

	size_t index1, index2;
	size_t j;
	int temp[] = { 0, 0 };

	for (size_t i = 0; i < k; i++)
	{
		j = 0;
		index2 = i;

		do
		{
			index1 = index2;
			index2 = (index1 + k) % numsSize;

			temp[j % 2] = nums[index2];
			if (j == 0) {
				nums[index2] = nums[index1];
			}
			else {
				nums[index2] = temp[(j + 1) % 2];
			}

			j++;
		} while (index2 != i);
	}
}

void rotate1(int* nums, int numsSize, int k) {
	if (k == 0) {
		return;
	}

	int* p = (int*) malloc(numsSize * sizeof(int));
	k = k % numsSize;

	if (k < 0) {
		int i = numsSize + k;
		memcpy(&(p[i]), nums, (numsSize - i) * sizeof(int));
		memcpy(p, &(nums[numsSize - i]), i * sizeof(int));

	}
	else {
		memcpy(&(p[k]), nums, (numsSize - abs(k)) * sizeof(int));
		memcpy(p, &(nums[numsSize - k]), abs(k) * sizeof(int));
	}
	
	memcpy(nums, p, numsSize * sizeof(int));

	free(p);
	return;
}

int main() {
	int vec[] = { 2, 3, 6, 7, 1 };
	int vec1[] = { 2, 3, 6, 7, 1 };
	int vec2[] = { 2, 3, 6, 7, 1 };


	rotate(vec, 5, 2);
	rotate1(vec1, 5, 2);
	rotate1(vec2, 5, -1);


	return 0;
}