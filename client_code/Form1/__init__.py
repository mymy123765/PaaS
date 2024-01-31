from ._anvil_designer import Form1Template
from anvil import *

class Form1(Form1Template):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

    def btn_chuyendoi_click(self, **event_args):
        try:
            # Kiểm tra xem người dùng đã nhập và không để trống
            if not self.box_nhapso.text:
                raise ValueError("Vui lòng nhập số nhị phân hoặc thập phân.")
            
            # Kiểm tra tùy chọn từ DropDown
            option = self.box_luachon.selected_value

            if option == "Chuyển số nhị phân sang thập phân":
                # Kiểm tra tính hợp lệ của box_nhapso nếu chuyển nhị phân sang thập phân
                binary_input = self.box_nhapso.text
                if not set(binary_input).issubset({'0', '1'}):
                    raise ValueError("Nhập không hợp lệ cho số nhị phân.")
                
                result = self.binary_to_decimal(binary_input)
                self.box_ketqua.text = str(result)
                self.box_ketqua.enabled = False

            elif option == "Chuyển số thập phân sang nhị phân":
                # Kiểm tra tính hợp lệ của box_nhapso nếu chuyển thập phân sang nhị phân
                decimal_input = self.box_nhapso.text
                if not decimal_input.isdigit():
                    raise ValueError("Nhập không hợp lệ cho số thập phân.")
                
                result = self.decimal_to_binary(int(decimal_input))
                self.box_ketqua.text = result
                self.box_ketqua.enabled = False

            else:
                raise ValueError("Tùy chọn không hợp lệ.")

        except ValueError as e:
            # Hiển thị thông báo lỗi
            alert(e)
            
    # Any code you write here will run before the form opens.
    def binary_to_decimal(self, binary_str):
        decimal_num = int(binary_str, 2)
        return decimal_num
    
    def decimal_to_binary(self, decimal_num):
        binary_str = bin(decimal_num).replace("0b", "")
        return binary_str
