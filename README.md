# Python Concurrent Programming

## Table of Contents

 - [Concurrence and Parallelism](#concurrence-and-parallelism)
 - [The `threading` Module](#the-threading-module)
   - [Thread Objects](#thread-objects)
     - [Attributes](#attributes)
     - [Methods](#methods)
   - [Example](#example)
 - [The Lock Object](#the-lock-object)

## Concurrence and Parallelism

**Concurrence** refers to many tasks concurring for the time of a single entity that is responsible for executing them.
In other hand, **parallelism** is when many entities are responsible 
In programming, those entities are the CPU cores.

## The `threading` Module

The threading module allows the creation of multiple threads to run tasks [concurrently](#Concurrency).

### Thread Objects

Represent a task or activity that runs in a separate thread of control (the thread that started it). See the Thread
class definition:

- `class threading.Thread(group=None, target=None, name=None, args=(), kwargs={}, *, daemon=None)`
  - This constructor should always be called with keyword arguments;
  - `group`: reserved for future extension when a ThreadGroup class is implemented;
  - `target`: is the function or other callable piece of code to be invoked by the `run()` method;
  - `name`: the thread name. By default, is set to a unique name in the form of "Thread-*N* (<`target.__name__`>)";
  - `args`: list or tuple of arguments for the target call;
  - `kwargs`: a dictionary of keyword arguments for the target call;
  - `daemon`: by default, inherits from the creating thread. Daemon threads are stopped by force at shutdown. The python 
  program exits when there are only daemon threads left running.

#### Attributes
- `ident`: identifies running threads, may be recycled after the thread is terminated;
- `native_id`: the thread's TID, assigned by the kernel. `native_id` and `ident` both are `None` if the thread has not
started;
- `daemon`: a boolean indicating if this thread is *daemonic* or not. Must be set before `start()`, otherwise raises a
`RunTime` error. Defaults to the value in the parent thread (the main thread is not a daemon).

#### Methods

  - `start()`: starts the thread activity. If called more than once by the same thread raises a `RuntimeError`;
  - `run()`: invokes the callable object passed to the constructor. May be overriden in a subclass;
  - `join()`: blocks the thread that started other threads, until the one that `join()` is called from terminates,
either by normal means or by an unhandled exception;
  - `is_alive()`: returns `True` just before `run()` starts until it is finished. 

### Example

Let's start with an example without threading:

```Python
import time

def task(num):
    print(f"Running thread {num}")
    time.sleep(1)

def no_threads(): 
    for index in range(5):
        task(index)

if __name__ == "__main__":
    start = time.perf_counter()
    print(f"> program start ")

    no_threads()

    end = time.perf_counter()
    print(f"> total execution time {end-start:.2}s")
```

The code above simulates an async operation that takes 1 second to complete. When a thread execution is interrupted by
`time.sleep()` the next one starts, and so on. The thread resumes when the timeout is over. That isolated operation
takes 5 seconds to run (you can test it on your own machine).

Let's try using threads this time:

```Python
from threading import Thread
import time


def task(num):
    print(f"> Running thread {num}")
    time.sleep(1)

def with_threads():
    threads = []
    for index in range(5):
        threads.append(Thread(target=task, args=(index, )))

    for t in threads:
        t.start()

    for t in threads:
        t.join()


if __name__ == "__main__":
    start = time.perf_counter()
    print(f"> program start ")

    with_threads()

    end = time.perf_counter()
    print(f"> total execution time {end-start:.2}s")
```

This time the whole operation took 1 second to execute. That happens because `time.sleep()` interrupts the current
thread, so the next one takes place and starts executing until it is interrupted too, until all the 5 threads are on 
timeout. When one of the threads wakes up it is immediately put back to the execution line.

[//]: # (TODO: ### The Lock Object)