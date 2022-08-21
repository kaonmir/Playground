import {Observable, Observer} from "rxjs";

const observableCreated$ = new Observable<number>((observer) => {
  console.log("BEGIN Observable");
  observer.next(1);
  observer.next(2);
  observer.complete();
  console.log("END Observable");

  return () => console.log("disposed");
});

const observer: Observer<number> = {
  next: (value: number) => console.log(value),
  error: (error: any) => console.log(error),
  complete: () => console.log("complete"),
};
const subscription = observableCreated$.subscribe(observer);
