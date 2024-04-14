#!/usr/bin/node

function partition (arr, low, high) {
  let j = low;
  let i = low - 1;
  const pivot = arr[high];

  for (; j < high; j++) {
    if (arr[j] < pivot) {
      i++;
      [arr[j], arr[i]] = [arr[i], arr[j]];
    }
  }
  [arr[i + 1], arr[high]] = [arr[high], arr[i + 1]];
  return i + 1;
}

function quicksort (arr, low, high) {
  if (low < high || arr.length <= 1) {
    const pivotIndex = partition(arr, low, high);

    // Recursively sort elements before and after pivot
    quicksort(arr, 0, pivotIndex - 1);
    quicksort(arr, pivotIndex + 1, high);
  }
}

const arr = process.argv.slice(2);
const sortedArray = arr.map(num => parseInt(num));
if (sortedArray.length !== 0) {
  quicksort(sortedArray, 0, sortedArray.length - 1);
  if (sortedArray.length === 1) {
    console.log('0');
  } else {
    let secondBiggestIndex = sortedArray.length - 2;
    console.log(sortedArray[secondBiggestIndex]);
  }
} else {
  console.log('0');
}
