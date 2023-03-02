from tables import Tables
from cubiecube import CubieCube


class CoordCube:
    """
    Biểu diễn tọa độ của hình lập phương. Cập nhật tọa độ bằng cách sử dụng 
    bảng di chuyển được tính toán trước.
    """

    def __init__(self, twist=0, flip=0, udslice=0, edge4=0, edge8=0, corner=0):
        self.tables = Tables()

        # 
        self.twist = twist
        self.flip = flip
        self.udslice = udslice
        self.edge4 = edge4
        self.edge8 = edge8
        self.corner = corner

    @classmethod
    def from_cubiecube(cls, cube):
        """
        Tạo 1 CoordCube từ 1 CubieCube hiện có
        """
        if not isinstance(cube, CubieCube):
            raise TypeError("Expected argument of type CubieCube")
        return cls(
            cube.twist,
            cube.flip,
            cube.udslice,
            cube.edge4,
            cube.edge8,
            cube.corner,
        )

    def move(self, mv):
        """
        Cập nhật tất cả các tọa độ sau khi áp dụng "mv" di chuyển bằng cách sử dụng các bảng di chuyển.
        mv: int              
        Số nguyên đại diện cho một trong 18 lần quay mặt không nhận dạng. 
        Tính toán như 3 * i + j trong đó i = 0, 1, 2, 3, 4, 5 cho U, R, F, D, L, B tương ứng, 
        và j = 0, 1, 2 tương ứng X, X', X2
        """
        self.twist = self.tables.twist_move[self.twist][mv]
        self.flip = self.tables.flip_move[self.flip][mv]
        self.udslice = self.tables.udslice_move[self.udslice][mv]
        self.edge4 = self.tables.edge4_move[self.edge4][mv]
        self.edge8 = self.tables.edge8_move[self.edge8][mv]
        self.corner = self.tables.corner_move[self.corner][mv]