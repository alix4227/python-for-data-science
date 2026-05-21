class calculator:
    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        product_list = [V1[i] * V2[i] for i in range(len(V1))]
        total = 0.0
        for item in product_list:
            total += item
        print(f'Dot product is: {total}')
    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        print(f'Add Vector is : {[float(V1[i] + V2[i]) for i in range(len(V1))]}')
    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        print(f'Sous Vector is: {[float(V1[i] - V2[i]) for i in range(len(V1))]}')