import glob
import matplotlib.pyplot as plt
from natsort import natsorted, ns
from time import time
from Algorithms import kmp, dynamic_lcss, naive_lcss, rabin_karp

kmp_times = []
naive_lcss_times = []
dynamic_lcss_times = []
rabin_karp_times = []

src_dataset = natsorted(
    glob.glob("Data\sources\*.txt"), alg=ns.IGNORECASE)

sus_dataset = natsorted(
    glob.glob("Data\sus\*.txt"), alg=ns.IGNORECASE)


def testAlgorithm(myFunction, time_array: list, algoName: str):
    for i in range(len(src_dataset)):
        src_file = src_dataset[i]
        sus_file = sus_dataset[i]

        # length of source file + length of sus file
        input_size = len(open(src_file, encoding="utf-8").read()) + \
            len(open(sus_file, encoding="utf-8").read())

        print("Running " + algoName + " on documents number " + str(i+1) + "\n")
        # Run algorithm and measure running time
        t0 = time()
        myFunction(src_file, sus_file)
        t1 = time()

        time_array.append([t1-t0, input_size])

    # Running time sorted by input size
    time_array.sort(key=lambda x: x[1])

    # Plotting the running times
    running_times = [x[0] for x in time_array]
    input_sizes = [x[1] for x in time_array]

    plt.plot(input_sizes, running_times, label=algoName)
    plt.xlabel("Input size (total characters))")
    plt.ylabel("Running time (seconds)")
    plt.legend()
    plt.savefig("Plots/" + algoName + ".png")


# TODO: Add comparison functions

testAlgorithm(rabin_karp.runRabinKarp, rabin_karp_times, "Rabin Karp")
testAlgorithm(kmp.runKMP, kmp_times, "KMP")
testAlgorithm(dynamic_lcss.runLCSS_dynamic, dynamic_lcss_times, "Dynamic LCSS")
testAlgorithm(naive_lcss.runLCSS_naive, naive_lcss_times, "Naive LCSS")
