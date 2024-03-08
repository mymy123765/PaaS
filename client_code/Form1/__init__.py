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
                
                result, steps = self.decimal_to_binary(float(decimal_input))
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
        if decimal_num == 0:
            return "0", "Không có bước nào cần thực hiện vì số decimal là 0."
    
        binary_str = ""
        steps = []
        steps.append("Giải thuật:")
        step_count = 1
    
        sign = "-" if decimal_num < 0 else ""  # Dấu của số, mặc định là không có nếu là số dương
        decimal_num = abs(decimal_num)
    
        integer_part = int(decimal_num)
        fraction_part = decimal_num - integer_part
    
        # Chuyển phần nguyên sang nhị phân
        if integer_part == 0:
            binary_str += "0"
        else:
            while integer_part > 0:
                remainder = integer_part % 2
                steps.append(f" | Bước {step_count}: {integer_part} % 2 = {remainder} (phần dư) |")
                integer_part = integer_part // 2
                binary_str = str(remainder) + binary_str
                step_count += 1
    
        # Nếu có phần thập phân, chuyển phần thập phân sang nhị phân
        if fraction_part != 0:
            binary_str += "."  # Thêm dấu chấm để biểu diễn phần thập phân trong nhị phân
    
            max_precision = 20  # Số lần lặp tối đa để tránh vòng lặp vô hạn
            precision = 0
    
            while fraction_part != 0 and precision < max_precision:
                fraction_part *= 2
                integer_part = int(fraction_part)
                binary_str += str(integer_part)
                fraction_part -= integer_part
                precision += 1
    
                steps.append(f" | Bước {step_count}: {fraction_part} * 2 = {integer_part} (phần nguyên) |")
                step_count += 1
    
        return sign + binary_str, "\n".join(steps)



    def btn_copy1_click(self, **event_args):
        """Xử lý khi người dùng nhấp vào nút btn_copy1"""
        data = self.box_ketqua.text.strip()  # Lấy dữ liệu từ box_ketqua và loại bỏ khoảng trắng thừa

        if data:  # Kiểm tra xem dữ liệu có tồn tại không
            self.call_js('cpy')  # Gọi hàm JavaScript để sao chép dữ liệu từ box_ketqua vào clipboard
            alert("Đã sao chép kết quả thành công!")
        else:
            alert("Không có dữ liệu để sao chép!")


    def btn_copy2_click(self, **event_args):
        """Xử lý khi người dùng nhấp vào nút btn_copy2"""
        data = self.box_giaithuat.text.strip()  # Lấy dữ liệu từ box_giaithuat và loại bỏ khoảng trắng thừa

        if data:  # Kiểm tra xem dữ liệu có tồn tại không
            self.call_js('cpy1')  # Gọi hàm JavaScript để sao chép dữ liệu từ box_giaithuat vào clipboard
            alert("Đã sao chép giải thuật thành công!")
        else:
            alert("Không có dữ liệu để sao chép!")

