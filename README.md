# Learning Python — Early Software Development Projects

### My First Steps into Software Engineering | Microsoft Internship

This repository documents my early journey learning Python, including programming exercises, data visualization experiments, and graphical user interface development during my first internship at Microsoft.

The projects range from introductory programming concepts to a more ambitious desktop application designed to interface with electronic laboratory equipment.

## Featured Project: Varactor Test Board GUI

The most substantial project in this repository is a Python desktop application developed to support testing and measurement of a varactor circuit board.

The application explores how software can interface with laboratory instrumentation, automate measurements, and visualize experimental data.

### Features

- **Graphical User Interface:** Built using wxPython, with interactive controls for configuring measurement parameters.
- **Voltage Configuration:** Input fields for minimum, maximum, and step voltages.
- **Channel Selection:** Dropdown menu for selecting test channels.
- **Instrument Communication:** Uses QCoDeS drivers for a Keysight N5245A network analyzer and Yokogawa GS200 source.
- **Data Collection:** Implements voltage-sweep logic and measurement acquisition.
- **Data Visualization:** Uses Matplotlib to display measurement results.
- **Data Export:** Includes functionality for saving collected data to CSV files.

### Technologies

- Python
- wxPython
- Matplotlib
- NumPy
- Pandas
- QCoDeS
- GPIB instrument communication

### Relevant Files

**`GUI demo + varactor tester.py`**

The main instrument-control application, integrating a graphical interface, voltage-sweep configuration, measurement collection, and data visualization.

**`GUI demo.py`**

An earlier GUI prototype using simulated data to experiment with interactive controls and embedded Matplotlib graphs.

**`GUI practice.py`**

A simple introductory wxPython application exploring desktop window creation.

## Data Visualization Projects

**`Project #2.py` and `Project #2 part 2.py`**

Python scripts for importing experimental data from CSV files and visualizing multiple measurement channels using Matplotlib.

These projects helped me explore scientific data processing and the presentation of experimental results.

**`Plotting Graphs.py`**

An introductory visualization exercise modeling compound interest over time.

## Additional Python Exercises

### Secret Journal

A command-line journal application featuring password creation, password changes, message storage, and password-gated access to entries.

This was an early exercise in functions, conditional logic, user input, and program structure.

*Note: The password handling is educational and is not suitable for securing sensitive information.*

### Programming Fundamentals

Additional files document my early experiments with Python syntax, iteration, and programming concepts.

## Running the Projects

Clone the repository:

```bash
git clone https://github.com/michaelsamhume/Learning-Python.git
cd Learning-Python
```

Individual scripts can be executed with Python, provided their required dependencies are installed.

For example:

```bash
python "Secret Journal.py"
```

GUI and plotting projects require additional packages such as wxPython, Matplotlib, NumPy, and Pandas.

The varactor measurement application additionally depends on QCoDeS, compatible laboratory instrumentation, and the appropriate instrument communication drivers.

Some scripts reference local CSV files or hardware configurations that are not necessarily included in the repository.

## What I Learned

These projects introduced me to several areas of software development:

- Python programming and problem-solving
- Object-oriented programming and event-driven interfaces
- Desktop GUI development
- Scientific data visualization
- Working with CSV datasets
- Hardware-software communication
- Building tools for experimental research

My experience developing software for laboratory instrumentation was particularly valuable because it demonstrated how programming can support real-world scientific and engineering work.

## Project Background

This repository contains some of my earliest Python work, including projects from my first Microsoft internship.

I've preserved these projects as a record of my development as a programmer, from introductory exercises to experimenting with scientific instrumentation and desktop application development.

The code represents early learning and prototyping rather than polished, production-ready software.

## Author

**Michael Hume**

Computer Science | Software Engineering | Artificial Intelligence | Scientific Computing

[GitHub Profile](https://github.com/michaelsamhume)
