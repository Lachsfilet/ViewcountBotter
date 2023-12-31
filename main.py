import requests
import multiprocessing

def makeRequest(url, iterations, shared_counter):
    for _ in range(iterations):
        try:
            requests.get(url)
            with shared_counter.get_lock():
                shared_counter.value += 1
                print(shared_counter.value)
        except Exception as e:
            print(f"Error making request: {e}")

if __name__ == "__main__":
    url = input('Please input your Viewcount API URL (for help enter h): ')
    total_iterations = int(input('Total iterations eg 100: '))
    threads = int(input('Threads eg 10: '))

    iterations_per_thread = total_iterations // threads
    remaining_iterations = total_iterations % threads

    shared_counter = multiprocessing.Value('i', 0)
    processes = []

    for _ in range(threads):
        iterations = iterations_per_thread
        if remaining_iterations > 0:
            iterations += 1
            remaining_iterations -= 1

        p = multiprocessing.Process(target=makeRequest, args=(url, iterations, shared_counter))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()
