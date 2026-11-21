//qo
// hgjfj
void selection_sort(int size, int arr[size]) {
    for (int i = 0; i < size - 1; i++) {
        int min_index = i;
        for (int j = i + 1; j < size; j++) {
            if (arr[j] < arr[min_index]) {
                min_index = j;
            }
        }
        int tmp = arr[i];
        arr[i] = arr[min_index];
        arr[min_index] = tmp;
    }
}
//
int main() {
    int a[] = {1, 6, 5};
    int n = sizeof(a) / sizeof(a[0]);
    selection_sort(n, a);
    return 0;
}