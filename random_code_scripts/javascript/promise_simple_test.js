const p = new Promise((res, rej) => {
  res("this is resolved");
});

function getData() {
  p.then(res => console.log(res));
  console.log("this is before");
}

getData();
