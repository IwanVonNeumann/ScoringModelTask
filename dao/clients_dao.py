from data.excel_parser import ExcelParser

FILE_NAME = "Task_scoring_modeller_Nov2016.xlsx"
WORKSHEET_NUMBER = 3


def get_clients_list(verbose=False):
    excel_parser = ExcelParser(FILE_NAME, WORKSHEET_NUMBER)
    data = excel_parser.extract_mapped_rows(verbose=verbose)
    excel_parser.close()
    return data
