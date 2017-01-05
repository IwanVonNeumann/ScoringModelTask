from data.excel_parser import ExcelParser

FILE_NAME = "Task_scoring_modeller_Nov2016.xlsx"
WORKSHEET_NUMBER = 3
excel_parser = ExcelParser(FILE_NAME, WORKSHEET_NUMBER)

data = excel_parser.extract_mapped_rows(verbose=True)
STATUS = 'status'

good_clients = [c for c in data if c[STATUS] == "GOOD"]
indetermined_clients = [c for c in data if c[STATUS] == "INDETERMINED"]
bad_clients = [c for c in data if c[STATUS] == "BAD"]

good_total = len(good_clients)
bad_total = len(bad_clients)

print("Good clients:", good_total)
print("Indetermined clients:", len(indetermined_clients))
print("Bad clients:", bad_total)

print("Good rate:", good_total / (good_total + bad_total))
