function outer() {
    let a = 10;
    function inner() {
        console.log(a, b);
    }
    var b = 12;
    inner();
}

outer();

function outer_max() {
    function outer2() {
        function inner() {
            console.log(a, b);
        }
        // inner();
        var b = 22;
        let a = 20;
        return inner;
    }
    return outer2;
}

outer_max()()();
