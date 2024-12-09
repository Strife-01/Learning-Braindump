// closure

function closure_function (/*callback,*/ message) {
  function callback(message) {
    console.log(`the message: ${message} is called inside the callback - sync`);
  }
  console.log(`the message: ${message} is outside the callback - sync`);
  callback(message);
}

// create callbacks sync

function callback (message) {
  console.log(`the message: ${message} is called inside the callback - sync`);
}

function make_call (callback, message) {
  callback(message);
  console.log(`the message: ${message} is outside the callback - async`);
}

// create callback async

async function callback_async (message) {
  setTimeout(() => callback(message), 500);
}

function make_call_async (callback, message) {
  callback(message);
  console.log(`the message: ${message} is outside the callback - async`)
}

//make_call_async(callback_async, "hello")

make_call((m) => {
  for (i = 0; i < 10; i++) {
    console.log("fuck you and your mama\n");
  }
}, "hello");
