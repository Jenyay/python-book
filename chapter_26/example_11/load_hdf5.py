import h5py

filename = "example_26_10.h5"

with h5py.File(filename, "r") as f:
    print("Описание:", f.attrs["description"])
    print("Дата создания:", f.attrs["date_created"])

    signal1 = f["examples/signals/signal1"]
    print("Тип signal1:", type(signal1))
    print("Описание сигнала 1:", signal1.attrs["description"])
    print("Размер массива данных:", signal1.shape)
    print(signal1[:10, :], "\n")

    signal2 = f["examples/signals/signal2"]
    print("Описание сигнала 2:", signal2.attrs["description"])
    print("Размер массива данных:", signal2.shape)
    print(signal1[:10, :], "\n")

    foo = f["examples/other/foo"]
    print("Описание массива данных:", foo.attrs["description"])
    print("Размер массива данных:", foo.shape)
    print(foo[:, :])
