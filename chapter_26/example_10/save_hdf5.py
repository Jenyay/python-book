import numpy as np
import h5py

x = np.linspace(0.0, 8.0e-9, 200)
y1 = np.sin(2e9 * x) * np.cos(5e9 * x)
y2 = np.sin(3e9 * x) * np.cos(7e9 * x)

filename = "example_26_10.h5"

with h5py.File(filename, "w") as f:
    print(f"{type(f)=}")
    f.attrs["description"] = "Пример данных, записанных в HDF5"
    f.attrs["date_created"] = "2025-05-15"

    examples_group = f.create_group("examples")
    print(f"{type(examples_group)=}")

    signals_group = examples_group.create_group("signals")
    signals_group.attrs["description"] = "Примеры сигналов"

    dataset1 = signals_group.create_dataset("signal1",
                                    data=np.column_stack([x, y1]))
    print(f"{type(dataset1)=}")
    dataset1.attrs["description"] = "sin(2e9 * x) * cos(5e9 * x)"

    dataset2 = signals_group.create_dataset("signal2",
                                    data=np.column_stack([x, y2]))
    dataset2.attrs["description"] = "sin(3e9 * x) * cos(7e9 * x)"

    other_group = examples_group.create_group("other")
    other_group["foo"] = np.arange(35).reshape(5, 7)
    other_group["foo"].attrs["description"] = "Пример массива данных"
