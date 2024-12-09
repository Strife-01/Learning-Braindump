const shoes = {
  model: "air max 1",
  price: 200,
};

const pants = {
  model: "jeens",
  price: 100,
};

const hat = {
  model: "nike",
  price: 50,
};

const test_outrageus_priced_product = {
  model: "expensive luxury",
  price: 2000,
};

const test_not_a_product = {
  model: "this is not a product",
  price: null,
}

const test_user = {
  name: "Andrei",
  email: "andreiursachi10@yahoo.com",
  password: "...enc...",
  wallet_ballance: 1000,
  user_cart: [shoes, pants, hat],
};

const AVAILABLE_PRODUCTS = [pants, shoes, hat, test_outrageus_priced_product];

const createOrder = (user) => new Promise ((resolve, reject) => {
    // validate cart
    const allowedProducts = user.user_cart.filter((product) => {
      for (const p of AVAILABLE_PRODUCTS) {
        if (product === p) {
          return true;
        }
      }
      return false;
    });
    
    if (user.user_cart.length != allowedProducts.length) {
      reject(new Error("Sorry some of your produts are not available at the moment"));
    }

    // If valid we resolve the order
    resolve({order_id: 1, items: user.user_cart, message: "All the products are in stock!"});
});

const proceedToPayment = (order, user) => new Promise ((resolve,reject) => {
  // validate payment
  let total_price = order.items.reduce((acc, curr) => acc += curr.price, 0);
  
  if (user.wallet_ballance < total_price) {
    reject(new Error(`Sorry you don't have enough money.\nThe total cost is ${total_price} but your ballance is ${user.wall}`));
  }

  resolve({message: "User has enough money", sum_to_be_wdthrawn: total_price, order: order});

});

const showOrderSummary = (payment_object) => new Promise ((resolve, reject) => {
  console.log("Your order:");
  payment_object.order.items.forEach((item) => {
    console.log(`${item.model} for the price of ${item.price}`);
  });

  resolve({total_sum: payment_object.sum_to_be_wdthrawn});
});

const updateWallet = (price_obj, user) => new Promise ((resolve, reject) => {
  user.wallet_ballance -= price_obj.total_sum;
  console.log(`Success, the total of ${price_obj.total_sum}$ has now been debited from your account.\nYou now have ${user.wallet_ballance}$ left.`);
});

createOrder(test_user)
  .then((order) => proceedToPayment(order, test_user))
  .then((payment) => showOrderSummary(payment))
  .then((price_obj) => updateWallet(price_obj, test_user))
  .catch((err) => {
    console.log(err.message);
  });

