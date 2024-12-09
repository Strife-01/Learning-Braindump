const p = new Promise((res, rej) => {
  res("This is resolved!");
});

const a = async () => {
  return await fetch('https://api.github.com');
}

a().then(res => console.log(res));
