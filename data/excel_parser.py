import os
import win32com.client
import time


class ExcelParser(object):
    def __init__(self, file_name, sheet_number):
        self.file_name = file_name
        self.sheet_number = sheet_number
        self.RESOURCES_ROOT = "../resources/"

        self.excel = self.setup_excel_app()
        self.work_book = self.setup_workbook()
        self.work_sheet = self.setup_worksheet()

    @staticmethod
    def setup_excel_app():
        return win32com.client.Dispatch("Excel.Application")

    def setup_workbook(self):
        rel_path = r"" + self.RESOURCES_ROOT + self.file_name
        abs_path = os.path.abspath(rel_path)
        return self.excel.Workbooks.Open(abs_path)

    def setup_worksheet(self):
        return self.work_book.Sheets(3)

    def get_used_rows_count(self):
        work_sheet = self.work_sheet
        used_range = work_sheet.UsedRange
        return used_range.Rows.Count

    def get_used_cols_count(self):
        work_sheet = self.work_sheet
        used_range = work_sheet.UsedRange
        return used_range.Columns.Count

    def extract_row(self, row_number):
        work_sheet = self.work_sheet
        cols_count = self.get_used_cols_count()
        row_as_range = work_sheet.Range(work_sheet.Cells(row_number, 1), work_sheet.Cells(row_number, cols_count))
        return list(row_as_range.Value[0])

    def extract_data_rows(self, rows_count=None, verbose=False):
        data_rows_count = self.get_used_rows_count() - 1
        if rows_count is None:
            rows_count = data_rows_count
        else:
            rows_count = min(rows_count, data_rows_count)

        start = 0
        if verbose:
            print("Extracting", rows_count, "rows...")
            start = time.time()

        work_sheet = self.work_sheet
        cols_count = self.get_used_cols_count()
        data_range = work_sheet.Range(work_sheet.Cells(2, 1), work_sheet.Cells(rows_count + 1, cols_count))
        rows = [list(data_row) for data_row in data_range.Value]

        if verbose:
            end = time.time()
            print("Finished in %.2f seconds" % (end - start))

        return rows

    def extract_mapped_rows(self, rows_count=None, verbose=False):
        if rows_count is None:
            rows_count = self.get_used_rows_count()
        header = self.extract_row(1)
        rows = self.extract_data_rows(rows_count, verbose=verbose)
        data = [dict(zip(header, row)) for row in rows]
        return data

    def get_work_sheet(self):
        return self.work_sheet

    def save(self):
        self.work_book.Save()

    def close(self):
        self.work_book.Close()
        self.excel.Quit()
