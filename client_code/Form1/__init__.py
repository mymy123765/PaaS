from ._anvil_designer import Form1Template
from anvil import *

class Form1(Form1Template):
    def __init__(self, **properties):
        # Thiết lập các thành phần và ràng buộc dữ liệu cho Form.
        self.init_components(**properties)
        
        # Định nghĩa các hàm chuyển đổi và xử lý sự kiện
        def thap_phan_sang_nhi_phan(n):
            result = ""
            while n > 0:
                result = str(n % 2) + result
                n = n // 2
            return result

        def nhi_phan_sang_thap_phan(binary):
            result = 0
            for i in range(len(binary)):
                result += int(binary[i]) * 2**(len(binary) - 1 - i)
            return result

        def chuyen_doi_click(self, **event_args):
            input_value = int(self.box_nhapso.text)
            option = self.box_luachon.selected_value
            if option == "Chuyển số thập phân sang nhị phân":
                self.box_giaithuat.text = "Thập phân: {}\nQuá trình:\n".format(input_value)
                binary_result = thap_phan_sang_nhi_phan(input_value)
                for i in range(len(binary_result)):
                    self.box_giaithuat.text += "• {} % 2 = {} (phần dư)\n".format(input_value, binary_result[i])
                    input_value //= 2
                self.box_giaithuat.text += "Chuỗi nhị phân: {}".format(binary_result[::-1])
            elif option == "Chuyển số nhị phân sang thập phân":
                self.box_giaithuat.text = "Nhị phân: {}\nQuá trình:\n".format(input_value)
                decimal_result = nhi_phan_sang_thap_phan(str(input_value))
                binary_str = str(input_value)
                for i in range(len(binary_str)):
                    if binary_str[i] == '1':
                        self.box_giaithuat.text += "• 1 x 2^ {} = {}\n".format(len(binary_str) - 1 - i, 2 ** (len(binary_str) - 1 - i))
                self.box_giaithuat.text += "Kết quả: {}".format(decimal_result)
            else:
                self.box_giaithuat.text = "Vui lòng chọn một phương pháp chuyển đổi!"
                
        # Gán sự kiện cho nút chuyển đổi
        self.btn_chuyendoi.set_event_handler("click", chuyen_doi_click)
