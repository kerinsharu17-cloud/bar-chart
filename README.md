# Bar Chart Visualization using Python

## Project Title
Bar Chart Visualization

## Aim
To create a bar chart using Python and Matplotlib for visualizing categorical data.

## Objective
The objective of this project is to understand data visualization techniques and represent data using a bar chart.

## Description
A bar chart is a graphical representation of data using rectangular bars. It is used to compare different categories of data. This project demonstrates how to create a simple bar chart using Python's Matplotlib library.

## Requirements
- Python 3.x
- Matplotlib

## Installation

Install Matplotlib using the following command:

```bash
pip install matplotlib
```

## Program

```python
import matplotlib.pyplot as plt

categories = ['A', 'B', 'C', 'D', 'E']
values = [10, 20, 15, 25, 18]

plt.bar(categories, values)

plt.title("Bar Chart Example")
plt.xlabel("Categories")
plt.ylabel("Values")

plt.show()
```

## Sample Output

A window will open displaying a bar chart with:

| Category | Value |
|----------|--------|
| A | 10 |
| B | 20 |
| C | 15 |
| D | 25 |
| E | 18 |

## Algorithm

1. Import the Matplotlib library.
2. Define the categories and their values.
3. Create a bar chart using `plt.bar()`.
4. Add chart title and labels.
5. Display the chart using `plt.show()`.

## Applications

- Data Analysis
- Business Reports
- Academic Projects
- Survey Results Visualization
- Statistical Analysis

## Result

The bar chart was successfully created and displayed using Python and Matplotlib. The chart clearly visualizes the comparison between different categories.

## Author

Kerin Sharu

## Repository

GitHub Repository: bar-chart
