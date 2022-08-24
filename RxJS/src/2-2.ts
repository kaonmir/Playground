import {Observable, Observer} from "rxjs";

const observableCreated$ = new Observable<number>((observer) => {
  for (let i = 1; i <= 5; i++) {
    setTimeout(() => {
      observer.next(i);

      if (i === 10) {
        observer.complete();
      }
    }, 300 * i);
  }
});

const observer: Observer<number> = {
  next: (value: number) => console.log(value),
  error: (error: any) => console.log(error),
  complete: () => console.log("complete"),
};

observableCreated$.subscribe(observer);
observableCreated$.subscribe(observer);
setTimeout(() => observableCreated$.subscribe(observer), 700);
