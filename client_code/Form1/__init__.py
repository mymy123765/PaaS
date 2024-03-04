from ._anvil_designer import Form1Template
from anvil import *

class Form1(Form1Template):
    def __init__(self, **properties):
        # Thiết lập thuộc tính và ràng buộc dữ liệu của Form.
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
                
                result, steps = self.binary_to_decimal(binary_input)
                self.box_ketqua.text = f"{result}\n"
                self.box_ketqua.enabled = True
                self.box_giaithuat.text = f"{steps}\n"
                self.box_giaithuat.enabled = True

            elif option == "Chuyển số thập phân sang nhị phân":
                # Kiểm tra tính hợp lệ của box_nhapso nếu chuyển thập phân sang nhị phân
                decimal_input = self.box_nhapso.text
                if not decimal_input.isdigit():
                    raise ValueError("Nhập không hợp lệ cho số thập phân.")
                
                result, steps = self.decimal_to_binary(int(decimal_input))
                self.box_ketqua.text = f"{result}\n"
                self.box_ketqua.enabled = True
                self.box_giaithuat.text = f"{steps}\n"
                self.box_giaithuat.enabled = True

            else:
                raise ValueError("Tùy chọn không hợp lệ.")

        except ValueError as e:
            # Hiển thị thông báo lỗi
            alert(e)
            
    def binary_to_decimal(self, binary_str):
        decimal_num = int(binary_str, 2)
        
        steps = []
        steps.append("Giải thuật:")
        for i, digit in enumerate(binary_str):
            power = len(binary_str) - i - 1
            if digit == '1':
                steps.append(f" | Bước {i + 1}: {digit} x 2^{power} = {int(digit) * (2 ** power)} |")
            else:
                steps.append(f" | Bước {i + 1}: {digit} x 2^{power} = 0 (bỏ qua) |")
        
        return decimal_num, "\n".join(steps)

    def decimal_to_binary(self, decimal_num):
        binary_str = ""
        
        steps = []
        steps.append("Giải thuật:")
        step_count = 1
        while decimal_num > 0:
            remainder = decimal_num % 2
            steps.append(f" | Bước {step_count}: {decimal_num} % 2 = {remainder} (phần dư) |")
            decimal_num = decimal_num // 2
            binary_str = str(remainder) + binary_str
            step_count += 1
        
        return binary_str, "\n".join(steps)

    def btn_copy1_click(self, **event_args):
        """Xử lý khi người dùng nhấp vào nút btn_copy1"""
        data = self.box_ketqua.text.strip()  # Lấy dữ liệu từ box_ketqua và loại bỏ khoảng trắng thừa

        if data:  # Kiểm tra xem dữ liệu có tồn tại không
            get_open_form().call_js('cpy')  # Gọi hàm JavaScript để sao chép dữ liệu từ box_ketqua vào clipboard
            alert("Đã sao chép dữ liệu thành công!")
        else:
            alert("Không có dữ liệu để sao chép!")


    def btn_copy2_click(self, **event_args):
        """Xử lý khi người dùng nhấp vào nút btn_copy2"""
        data = self.box_giaithuat.text.strip()  # Lấy dữ liệu từ box_giaithuat và loại bỏ khoảng trắng thừa

        if data:  # Kiểm tra xem dữ liệu có tồn tại không
            get_open_form().call_js('cpy1')  # Gọi hàm JavaScript để sao chép dữ liệu từ box_giaithuat vào clipboard
            alert("Đã sao chép dữ liệu thành công!")
        else:
            alert("Không có dữ liệu để sao chép!")

