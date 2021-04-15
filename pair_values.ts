const defaultTests = [
  {
    name: "Test 1",
    array: [1, 2, 3, 4],
    desiredSum: 5,
    expectedAnswer: [1, 4],
  },
  {
    name: "Test 2",
    array: [2, 5, 1, 3, 4, 6, 7],
    desiredSum: 8,
    expectedAnswer: [1, 7],
  },
  {
    name: "Test 3",
    array: [3, 3, 5, 6, 7],
    desiredSum: 11,
    expectedAnswer: null,
  },
  {
    name: "Test 4",
    array: [4, 2, 8, 25],
    desiredSum: 26,
    expectedAnswer: null,
  },
  {
    name: "Test 5",
    array: [0, 1, 2, 3, 4],
    desiredSum: 5,
    expectedAnswer: null,
  },
  {
    name: "Test 6",
    array: [[], [], [], []],
    desiredSum: 5,
    expectedAnswer: null,
  },
  {
    name: "Test 7",
    array: ["0", "1", "2", "3", "4"],
    desiredSum: 5,
    expectedAnswer: null,
  },
  {
    name: "Test 8",
    array: ["1", "2", "3", "4"],
    desiredSum: 5,
    expectedAnswer: [1, 4],
  },
];

// found on Stack overflow- I'm sure there is a library out there that does this
let isEqual = (value, other) => {
  // Get the value type
  var type = Object.prototype.toString.call(value);

  // If the two objects are not the same type, return false
  if (type !== Object.prototype.toString.call(other)) return false;

  // If items are not an object or array, return false
  if (["[object Array]", "[object Object]"].indexOf(type) < 0) return false;

  // Compare the length of the length of the two items
  var valueLen =
    type === "[object Array]" ? value.length : Object.keys(value).length;
  var otherLen =
    type === "[object Array]" ? other.length : Object.keys(other).length;
  if (valueLen !== otherLen) return false;

  // Compare two items
  var compare = function (item1, item2) {
    // Get the object type
    var itemType = Object.prototype.toString.call(item1);

    // If an object or array, compare recursively
    if (["[object Array]", "[object Object]"].indexOf(itemType) >= 0) {
      if (!isEqual(item1, item2)) return false;
    }

    // Otherwise, do a simple comparison
    else {
      // If the two items are not the same type, return false
      if (itemType !== Object.prototype.toString.call(item2)) return false;

      // Else if it's a function, convert to a string and compare
      // Otherwise, just compare
      if (itemType === "[object Function]") {
        if (item1.toString() !== item2.toString()) return false;
      } else {
        if (item1 !== item2) return false;
      }
    }
  };

  // Compare properties
  if (type === "[object Array]") {
    for (var i = 0; i < valueLen; i++) {
      if (compare(value[i], other[i]) === false) return false;
    }
  } else {
    for (var key in value) {
      if (value.hasOwnProperty(key)) {
        if (compare(value[key], other[key]) === false) return false;
      }
    }
  }

  // If nothing failed, return true
  return true;
};

// super inefficient time wise, nested for loops O(n^2)
// not too bad with memory because we only mess with and compare against one array/object
let findPairFirstIteration = (values, desiredSum) => {
  values.sort();
  for (let i = 0; i < values.length; i++) {
    for (let j = 1; j < values.length; j++) {
      if (values[i] === values[j] && i != j) {
        return;
      }
      if (values[i] + values[j] === desiredSum) {
        return [values[i], values[j]];
      }
    }
  }
  return null;
};

// uses Dynamic Programming/ memoization
// more efficient time wise, O(n)
// takes up more memory by writing pairs into the checkedValues object and results into an array
let findPairFinal = (values, desiredSum) => {
  values.sort();

  let checkedValues = {};
  let results = [];

  // this creates an object (checkedValues) that stores a checked value as the key and the desired sum - the checked value as it's value pair
  // if the value pair already exists in the object, we take the key and add it to the results array as an array [value, key]
  for (let i = 0; i < values.length; i++) {
    // check for invalid types
    if (typeof values[i] != "number" && typeof values[i] != "string") {
      return null;
    }

    // make sure any strings are converted to numbers
    let currentValue = parseInt(values[i]);

    // check if the value is greater than zero
    if (currentValue < 1) {
      return null;
    }
    // check if there are duplicates in the array
    if (values[i] === values[i + 1]) {
      return null;
    }

    if (checkedValues[currentValue]) {
      //format this as [smaller_value, greater_value]
      results.push([checkedValues[currentValue], currentValue]);
    } else {
      checkedValues[desiredSum - currentValue] = currentValue;
    }
  }

  // we then sort this array and return the first pair as our final result
  results.sort();
  return results.length > 0 ? results[0] : null;
};

let runTests = (tests) => {
  console.log("Test Results \n---------------");

  tests.map((test) => {
    let solution = findPairFinal(test.array, test.desiredSum);

    if (
      (!solution && !test.expectedAnswer) ||
      (solution && isEqual(solution, test.expectedAnswer))
    ) {
      console.log("\x1b[32m%s\x1b[0m", `  ${test.name} Passed`);
    } else {
      console.log("\x1b[31m%s\x1b[0m", `  ${test.name} Failed`);
    }
  });

  console.log("\nEnd Tests");
};

runTests(defaultTests);
