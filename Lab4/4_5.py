def count_elements(numbers):
    counts = {}

    for item in numbers:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1

    for key, value in counts.items():
        print(key, "occurs", value, "time(s)")


sample_list = [10, 20, 30, 30, 30, 30, 20, 40]


count_elements(sample_list)