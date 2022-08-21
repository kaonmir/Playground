import {interval} from "rxjs";

const observable1 = interval(400);
const observable2 = interval(300);

const subscription = observable1.subscribe((value: number) =>
  console.log(value)
);

const childSubscription = observable2.subscribe((value: number) =>
  console.log(value)
);

subscription.add(childSubscription);

setTimeout(() => {
  subscription.unsubscribe();
}, 2000);
