function canSellCookie(bills) {
  let five = 0;
  let ten = 0;
  let twenty = 0

  for (let i = 0; i < bills.length; i++) {
    const bill = bills[i];

    if (bill === 5) {
      five++;
    } else if (bill === 10) {
      if (five === 0) return false;
      five--;
      ten++;
    } else if (bill === 20) {
      if (ten > 0 && five > 0) {
        ten--;
        five--;
        twenty++;
      } else if (five >= 3) {
        five -= 3;
        twenty++;
      } else {
        return false;
      }
    }
  }

  return true;
}

console.log(canSellCookie([5, 5, 5, 10, 20]));
console.log(canSellCookie([5, 5, 10, 10, 20]));
console.log(canSellCookie([5, 5, 5, 10, 10, 20]));
console.log(canSellCookie([5, 5, 5, 5, 20]));
