import unittest
import time_series_visualizer
import matplotlib as mpl

class DataCleaningTestCase(unittest.TestCase):
    def test_data_cleaning(self):
        actual = int(time_series_visualizer.df.count())
        expected = 1238
        self.assertEqual(actual, expected)

class LinePlotTestCase(unittest.TestCase):
    def setUp(self):
        self.fig = time_series_visualizer.draw_line_plot()
        self.ax = self.fig.axes[0]

    def test_line_plot_title(self):
        self.assertEqual(self.ax.get_title(), "Daily freeCodeCamp Forum Page Views 5/2016-12/2019")

    def test_line_plot_labels(self):
        self.assertEqual(self.ax.get_xlabel(), "Date")
        self.assertEqual(self.ax.get_ylabel(), "Page Views")

    def test_line_plot_data_quantity(self):
        self.assertEqual(len(self.ax.lines[0].get_ydata()), 1238)

class BarPlotTestCase(unittest.TestCase):
    def setUp(self):
        self.fig = time_series_visualizer.draw_bar_plot()
        self.ax = self.fig.axes[0]

    def test_bar_plot_legend_labels(self):
        actual = [label.get_text() for label in self.ax.get_legend().get_texts()]
        expected = ['January', 'February', 'March', 'April', 'May', 'June',
                    'July', 'August', 'September', 'October', 'November', 'December']
        self.assertEqual(actual, expected)

    def test_bar_plot_labels(self):
        self.assertEqual(self.ax.get_xlabel(), "Years")
        self.assertEqual(self.ax.get_ylabel(), "Average Page Views")
        actual = [label.get_text() for label in self.ax.get_xaxis().get_majorticklabels()]
        self.assertEqual(actual, ['2016', '2017', '2018', '2019'])

    def test_bar_plot_number_of_bars(self):
        actual = len([rect for rect in self.ax.get_children() if isinstance(rect, mpl.patches.Rectangle)])
        self.assertEqual(actual, 49)

class BoxPlotTestCase(unittest.TestCase):
    def setUp(self):
        self.fig = time_series_visualizer.draw_box_plot()
        self.ax1 = self.fig.axes[0]
        self.ax2 = self.fig.axes[1]

    def test_box_plot_number(self):
        self.assertEqual(len(self.fig.get_axes()), 2)

    def test_box_plot_labels(self):
        self.assertEqual(self.ax1.get_xlabel(), "Year")
        self.assertEqual(self.ax1.get_ylabel(), "Page Views")
        self.assertEqual(self.ax2.get_xlabel(), "Month")
        self.assertEqual(self.ax2.get_ylabel(), "Page Views")

    def test_box_plot_titles(self):
        self.assertEqual(self.ax1.get_title(), "Year-wise Box Plot (Trend)")
        self.assertEqual(self.ax2.get_title(), "Month-wise Box Plot (Seasonality)")

    def test_box_plot_number_of_boxes(self):
        self.assertEqual(len(self.ax1.lines) / 6, 4)
        self.assertEqual(len(self.ax2.lines) / 6, 12)

if __name__ == "__main__":
    unittest.main()