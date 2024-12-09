// p1_status = true;
// p2_status = false;
// p3_status = true;

/*
const p1_fake = new Promise ((res, rej) => {
  setTimeout(() => {
    if (p1_status) {
      res({message: "p1 was successful!"});
    }

    rej(new Error("p1 was unsuccessful!"));
  }, 5000);  
});

const p2_fake = new Promise ((res, rej) => {
setTimeout(() => {
  if (p2_status) {
    res({message: "p2 was successful!"});
  }

  rej(new Error("p2 was unsuccessful!"));
}, 2000);
});

const p3_fake = new Promise ((res, rej) => {
setTimeout(() => {
  if (p3_status) {
    res({message: "p3 was successful!"});
  }

  rej(new Error("p3 was unsuccessful!"));
}, 3000);
});
*/

const p1 = fetch("https://api.netflix.com");
const p2 = fetch("https://api.wikipedia.com");
const p3 = fetch("https://api.facebook.com");

/*
p1().then((res) => {
  console.log(res.message);
})
.catch((err) => {
  console.log(err.message);
});

p2().then((res) => {
  console.log(res.message);
})
.catch((err) => {
  console.log(err.message);
});

p3().then((res) => {
  console.log(res.message);
})
.catch((err) => {
  console.log(err.message);
});
*/

/*
Promise.all([p1, p2, p3])
.then((pa) => {console.log(pa)})
.catch((err) => {console.log(err)});
*/

Promise.allSettled([p1, p2, p3])
.then((pa) => {console.log(pa)})
.catch((err) => {console.log(err.message)});

/*
Promise.race([p1, p2, p3])
.then((pa) => {console.log(pa)})
.catch((err) => {console.log(err)});

Promise.any([p1, p2, p3])
.then((pa) => {console.log(pa)})
.catch((err) => {console.log(err)});
*/
