# import openpyxl module
import openpyxl
import os
import PyQt5 as pqt

# import BarChart class from openpyxl.chart sub_module
from openpyxl.chart import BarChart,Reference

# Call a Workbook() function of openpyxl
# to create a new blank Workbook object
wb = openpyxl.Workbook()

# Get workbook active sheet
# from the active attribute.
sheet = wb.active

# write o to 9 in 1st column of the active sheet
for i in range(13):
	sheet.append([i])

# create data for plotting
values = Reference(sheet, min_col = 1, min_row = 1,
						max_col = 1, max_row = 13)

# Create object of BarChart class
chart = BarChart()

# adding data to the Bar chart object
chart.add_data(values)

# set the title of the chart
chart.title = " BAR-CHART "

# set the title of the x-axis
chart.x_axis.title = " AXIS one "

# set the title of the y-axis
chart.y_axis.title = " AXIS TWO"

# add chart to the sheet
# the top-left corner of a chart
# is anchored to cell E2 .
sheet.add_chart(chart, "I6")

# save the file
wb.save("W:\DFS\GNA/barChart.xlsx")

#
# os.umask(0)
# os.chmod(mode, '0o777')
# # print (os.getcwd())