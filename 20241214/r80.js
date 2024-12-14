const fs = require("node:fs");

function do80() {
  let arr = [];
  let total = 0;
  for (let i = 0; i < 12; i++) {
    ra = Math.round((Math.random() * 10) / 2);
    total += ra;
    arr.push(ra);
    // fs.writeFileSync("r80.txt", String(ra));
    // console.log(ra);
  }
  arr.push(total);
  // console.log(arr, total);
  // fs.writeFileSync("r80.txt", String(arr));
  return arr;
}

for (let i = 0; i < 1; i++) {
  const arr = do80();
  console.log(arr);
  // if (arr.pop() > 50) {
  //   console.log(arr);
  // }
}
