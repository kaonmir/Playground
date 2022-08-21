type Nums = number | Nums[];

const a: Nums = [1, 2, [3, 4], [[3, 4]]];

function func(a: number, b?: Nums) {
  return typeof b;
}
