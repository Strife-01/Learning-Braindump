function cl() {
  for (var i = 0; i < 5; i++) {
    function close(sec) {
      setTimeout(function () {
        console.log(sec);
      }, sec * 1000);
    }
    close(i);
  }
}

cl();
