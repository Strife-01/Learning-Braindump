const p1 = new Promise((res, rej) => {
  setTimeout(() => {
    res(Date.now());
  }, 10000);
});

const p2 = new Promise((res, rej) => {
  setTimeout(() => {
    res(Date.now());
  }, 1000);
});


// async function getData() {
//  const data = await p;
//  console.log(data);
//  console.log("this is yes");
//  return data;
// }

// getData();

// console.log('yayayaya');

async function getData() {
  let start = Date.now();
  const data1 = await p1;
  console.log("P1 finished");
  console.log(data1 - start);

  const data2 = await p2;
  console.log("P2 finished");
  console.log(data2 - start);
}

getData();
