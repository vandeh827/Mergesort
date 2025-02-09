public class MergeSort {

    // Main function to perform merge sort
    public void mergeSort(int[] arr) {
        if (arr == null || arr.length <= 1) {
            return; // Already sorted or empty
        }
        mergeSortHelper(arr, 0, arr.length - 1);
    }

    // Recursive helper function for merge sort
    private void mergeSortHelper(int[] arr, int low, int high) {
        if (low < high) {
            int mid = low + (high - low) / 2; // Calculate midpoint to avoid overflow
            mergeSortHelper(arr, low, mid); // Sort the left half
            mergeSortHelper(arr, mid + 1, high); // Sort the right half
            merge(arr, low, mid, high); // Merge the sorted halves
        }
    }


    // Merge function to combine two sorted subarrays
    private void merge(int[] arr, int low, int mid, int high) {
        int n1 = mid - low + 1; // Size of the left subarray
        int n2 = high - mid;     // Size of the right subarray

        // Create temporary arrays
        int[] left = new int[n1];
        int[] right = new int[n2];

        // Copy data to temporary arrays
        for (int i = 0; i < n1; ++i) {
            left[i] = arr[low + i];
        }
        for (int j = 0; j < n2; ++j) {
            right[j] = arr[mid + 1 + j];
        }

        // Merge the temporary arrays back into the original array
        int i = 0, j = 0, k = low;
        while (i < n1 && j < n2) {
            if (left[i] <= right[j]) {
                arr[k] = left[i];
                i++;
            } else {
                arr[k] = right[j];
                j++;
            }
            k++;
        }

        // Copy any remaining elements from the left subarray
        while (i < n1) {
            arr[k] = left[i];
            i++;
            k++;
        }

        // Copy any remaining elements from the right subarray
        while (j < n2) {
            arr[k] = right[j];
            j++;
            k++;
        }
    }


    public static void main(String[] args) {
        MergeSort ms = new MergeSort();
        int[] data = {9, 5, 1, 4, 3, 2, 7, 8, 6};

        System.out.println("Unsorted array:");
        printArray(data);

        ms.mergeSort(data);

        System.out.println("\nSorted array:");
        printArray(data);

    }

    // Helper function to print an array
    static void printArray(int arr[]) {
        int n = arr.length;
        for (int i = 0; i < n; ++i)
            System.out.print(arr[i] + " ");
        System.out.println();
    }
}