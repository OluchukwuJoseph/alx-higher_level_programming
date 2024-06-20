#!/usr/bin/node

const argv = process.argv;
const args = [];
let j = 0;
let i = 2;

for (; argv[i]; i++, j++) {
  args[j] = parseInt(argv[i]);
}

function partition (arr, low, high) {
  const pivot = arr[high];
  let i = low - 1;
  let j = low;

  for (; j < high; j++) {
    if (arr[j] < pivot) {
      i++;
      [arr[j], arr[i]] = [arr[i], arr[j]];
    }
  }
  [arr[i + 1], arr[high]] = [arr[high], arr[i + 1]];
  return (i + 1);
}

function quicksort (arr, low, high) {
  if (low < high) {
    const pivotIndex = partition(arr, low, high);

    // Recursively sort elements before and after pivot
    quicksort(arr, 0, pivotIndex - 1);
    quicksort(arr, pivotIndex + 1, high);
  }
}

if (args.length === 0 || args.length === 1) {
  console.log('0');
} else {
  quicksort(args, 0, args.length - 1);
  console.log(args[args.length - 2]);
}
