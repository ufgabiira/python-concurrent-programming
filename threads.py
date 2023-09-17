from threading import Thread
import time


def task(num):
    print(f"> Running thread {num}")
    time.sleep(1)


def no_threads():
    for index in range(5):
        task(index)


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

    # no_threads()
    with_threads()

    end = time.perf_counter()
    print(f"> total execution time {end-start:.2}s")
