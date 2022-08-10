from multiprocessing.sharedctypes import Value
import os
import pandas
import sys

def summarize(file):
    peeps = {}
    df = pandas.read_excel(file)
    for row in df.iterrows():
        entry = row[1].values
        # Probably a better way to do this.
        if str(entry[0]) == "nan":
            continue
        if entry[0] not in peeps:
            peeps[entry[0]] = 0
        try:
            int(entry[2])
        except ValueError:
            print("Error for {} of: {}".format(entry[0], entry[2]))
            continue
        time = entry[2]
        if entry[3] == "Hours":
            time = time / 8
        peeps[entry[0]] = peeps[entry[0]] + time

    return peeps

def dump(peeps):
    longest_name = max([len(k) for k in peeps.keys()])
    print("|{}|{}|".format(
        str.ljust("Name", longest_name),
        "Days off"
    ))
    print("-{}-{}-".format(
        "-" * longest_name,
        "-" * 8
    ))
    for name, total in peeps.items():
        print("|{}|{}|".format(
            str.ljust(name, longest_name),
            str.ljust(str(total), 8))
        )

if __name__ == "__main__":
    if not len(sys.argv) == 2:
        print("Usage: python summary.py <file>")
        sys.exit(1)
    if not os.path.exists(sys.argv[1]):
        print("File does not exist")
        sys.exit(1)

    dump(summarize(sys.argv[1]))
