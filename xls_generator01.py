# coding: utf-8

import xlsxwriter

# Create an new Excel file and add a worksheet.
workbook = xlsxwriter.Workbook('demo.xlsx')
worksheet = workbook.add_worksheet()

# Widen the first column to make the text clearer.
worksheet.set_column('A:A', 20)

# Add a bold format to use to highlight cells.
bold = workbook.add_format({'bold': True})

# Write some simple text.
worksheet.write('A1', 'Hello')

# Text with formatting.
worksheet.write('A2', 'World', bold)

worksheet.write('A6', '測試', bold)

# Write some numbers, with row/column notation.
worksheet.write(2, 0, 123)
worksheet.write(3, 0, 123.456)
worksheet.write(4, 0, 1000)

# Insert an image.
worksheet.insert_image('B5', 'logo.jpg')

# Set column format
# format1 = workbook.add_format({'num_format': '#,##0.00'})
# worksheet.set_column('A:B', 100, format1)
# worksheet.set_column(0, 0, 100)  # Width of columns B:D set to 30.

workbook.close()
