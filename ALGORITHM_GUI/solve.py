import time

import coordcube, facecube
from facecube import FaceCube
from coordcube import CoordCube
from pieces import Color
from tables import Tables


class SolutionManager:
    def __init__(self, facelets):
        """
        facelets: chuỗi trạng thái màu đầu vào lấy từ xử lý ảnh, thứ tự lấy và mã hóa theo tên gọi các mặt (U, R, F, D, L, B)
        """
        self.tables = Tables()

        self.facelets = facelets.upper() # chuyen thanh chuoi in hoa

        status = self.verify()
        if status:
            error_message = {
                -1: "mỗi màu nên xuất hiện đúng 9 lần",
                -2: "không phải tất cả 12 cạnh đều tồn tại chính xác một lần",
                -3: "lỗi lật - một cạnh phải được lật",
                -4: "không phải tất cả các góc đều tồn tại chính xác một lần",
                -5: "lỗi xoắn (bẻ góc) - một góc phải được xoắn lại",
                -6: "Lỗi chẵn lẻ - phải đổi hai góc hoặc cạnh",
            }
            raise ValueError("Invalid cube: {}".format(error_message[status]))

    def solve(self, max_length=25, timeout=float("inf")):
        """
        max_length: giới hạn cho số lần di chuyển lớn nhất.
        max_time: thời gian giới hạn tìm kiếm
            ``time.time() > max_time``.
        """
        # prepare for phase 1
        self._phase_1_initialise(max_length)
        self._allowed_length = max_length
        self._timeout = timeout

        for depth in range(self._allowed_length):
            n = self._phase_1_search(0, depth)
            if n >= 0:
                # solution found
                return self._solution_to_string(n)
            elif n == -2:
                # time limit exceeded
                return -2

        # no solution found
        return -1

    def verify(self):
        count = [0] * 6
        try:
            for char in self.facelets:
                count[Color[char]] += 1
        except (IndexError, ValueError):
            return -1
        for i in range(6):
            if count[i] != 9:
                return -1

        fc = FaceCube(self.facelets)
        cc = fc.to_cubiecube()

        return cc.verify()

    def _phase_1_initialise(self, max_length):
        # List 'axis' và 'power' sẽ lưu lần di chuyển thứ n 
        # (chỉ số (index) của mặt được quay được lưu trong axis, 
        # số vòng 1/4 theo chiều kim đồng hồ được lưu trữ trong power). Nước đi thứ n được lưu ở vị trí n-1.
        self.axis = [0] * max_length
        self.power = [0] * max_length

        # danh sách twist, flip và udslice lưu trữ tọa độ pha 1 sau n lần di chuyển. 
        # vị trí 0 lưu trữ trạng thái ban đầu, tọa độ sau n lần di chuyển được lưu trữ ở vị trí n
        self.twist = [0] * max_length
        self.flip = [0] * max_length
        self.udslice = [0] * max_length

        # Những list dưới dây lưu trữ tọa độ pha 2 sau n lần di chuyển
        self.corner = [0] * max_length
        self.edge4 = [0] * max_length
        self.edge8 = [0] * max_length

        # Hai mảng sau lưu trữ số lần di chuyển tối thiểu cần thiết để đạt được pha 2 hoặc một nghiệm tương ứng 
        # sau n lần di chuyển. những ước tính này đến từ các bảng cắt tỉa và được sử dụng để loại trừ 
        # các nhánh trong cây tìm kiếm. 
        self.min_dist_1 = [0] * max_length
        self.min_dist_2 = [0] * max_length

        # initialise the arrays from the input
        self.f = FaceCube(self.facelets)
        self.c = CoordCube.from_cubiecube(self.f.to_cubiecube())
        self.twist[0] = self.c.twist
        self.flip[0] = self.c.flip
        self.udslice[0] = self.c.udslice
        self.corner[0] = self.c.corner
        self.edge4[0] = self.c.edge4
        self.edge8[0] = self.c.edge8
        self.min_dist_1[0] = self._phase_1_cost(0)

    def _phase_2_initialise(self, n):
        if time.time() > self._timeout:
            return -2
        # khởi tạo pha 2 từ lời giải của pha 1
        cc = self.f.to_cubiecube()
        
        # Xoay các bước đã thực hiện ở pha 1, để lấy các giá trị tọa độ ở pha 2
        for i in range(n):
            for j in range(self.power[i]):
                cc.move(self.axis[i])
        self.edge4[n] = cc.edge4
        self.edge8[n] = cc.edge8
        self.corner[n] = cc.corner
        self.min_dist_2[n] = self._phase_2_cost(n)
        for depth in range(self._allowed_length - n):
            m = self._phase_2_search(n, depth)
            if m >= 0:
                return m
        return -1

    def _phase_1_cost(self, n):
        """
        Chi phí của vị trí hiện tại để sử dụng trong giai đoạn 1. 
        Trả về giới hạn dưới về số lần di chuyển cần thiết để đến giai đoạn 2.
        """
        return max(
            self.tables.udslice_twist_prune[self.udslice[n], self.twist[n]],
            self.tables.udslice_flip_prune[self.udslice[n], self.flip[n]],
        )

    def _phase_2_cost(self, n):
        """
        Chi phí của vị trí hiện tại để sử dụng trong giai đoạn 2. 
        Trả về giới hạn dưới về số lần di chuyển cần thiết để đi đến một khối Rubik đã giải. 
        """
        return max(
            self.tables.edge4_corner_prune[self.edge4[n], self.corner[n]],
            self.tables.edge4_edge8_prune[self.edge4[n], self.edge8[n]],
        )

    def _phase_1_search(self, n, depth):
        if time.time() > self._timeout:
            return -2
        elif self.min_dist_1[n] == 0: # ở bước n ta có số bước ước tính để đi đến pha 2 = 0, khi đó khởi tạo pha 2 tại bước n
            return self._phase_2_initialise(n)
        elif self.min_dist_1[n] <= depth:
            for i in range(6):
                if n > 0 and self.axis[n - 1] in (i, i + 3):
                    continue
                for j in range(1, 4): # 1 --> X ; 2 --> X'; 3 --> X2
                    self.axis[n] = i
                    self.power[n] = j
                    mv = 3 * i + j - 1
                        
                    # update các tọa độ
                    self.twist[n + 1] = self.tables.twist_move[self.twist[n]][mv]
                    self.flip[n + 1] = self.tables.flip_move[self.flip[n]][mv]
                    self.udslice[n + 1] = self.tables.udslice_move[self.udslice[n]][mv]
                    self.min_dist_1[n + 1] = self._phase_1_cost(n + 1)
                    
                    # bắt đầu tìm kiếm node mới
                    m = self._phase_1_search(n + 1, depth - 1)
                    if m >= 0:
                        return m
                    if m == -2:
                        return -2
        # K có lời giải ở depth hiện tại, return -1
        return -1

    def _phase_2_search(self, n, depth):
        if self.min_dist_2[n] == 0:
            return n
        elif self.min_dist_2[n] <= depth:
            for i in range(6):
                if n > 0 and self.axis[n - 1] in (i, i + 3):
                    continue
                for j in range(1, 4):
                    if i in [1, 2, 4, 5] and j != 2: # # loại những bước xoay làm sai vị trí 4 cạnh lớp UD: R, F, L, B
                        continue
                    self.axis[n] = i
                    self.power[n] = j
                    mv = 3 * i + j - 1

                    # update các tọa độ
                    self.edge4[n + 1] = self.tables.edge4_move[self.edge4[n]][mv]
                    self.edge8[n + 1] = self.tables.edge8_move[self.edge8[n]][mv]
                    self.corner[n + 1] = self.tables.corner_move[self.corner[n]][mv]
                    self.min_dist_2[n + 1] = self._phase_2_cost(n + 1)

                    # bắt đầu tìm kiếm 1 node mới
                    m = self._phase_2_search(n + 1, depth - 1)
                    if m >= 0:
                        return m
        return -1

    def _solution_to_string(self, length):
        """
        Chuỗi lời giải:
            X: Xoay 90 độ theo chiều kim đồng hồ
            X': Xoay 90 độ ngược chiều kim đồng hồ
            X2: Xoay 180 độ theo chiều kim đồng hồ
        """

        def recover_move(axis_power):
            axis, power = axis_power
            if power == 1:
                return Color(axis).name
            if power == 2:
                return Color(axis).name + "2"
            if power == 3:
                return Color(axis).name + "'"
            raise RuntimeError("Invalid move in solution.")

        solution = map(
            recover_move, zip(self.axis[:length], self.power[:length])
        )
        return " ".join(solution)