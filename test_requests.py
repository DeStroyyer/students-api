# import requests
# import sys

# BASE_URL = 'http://127.0.0.1:5000'
# OUTPUT_FILE = 'results.txt'

# def log_result(message, file_handler):
#     print(message)
#     file_handler.write(message)

# def run_test():
#     with open(OUTPUT_FILE, 'w') as f:
#         response = requests.get(f'{BASE_URL}/students')
#         log_result(response.text, f)
#         log_result('\n', f)

#         response = requests.get(f'{BASE_URL}/students/2')
#         log_result(response.text, f)
#         log_result('\n', f)

#         response = requests.delete(f'{BASE_URL}/students/3')
#         log_result("Student was deleted", f)
#         log_result('\n', f)



# if __name__ == "__main__":
#     run_test()