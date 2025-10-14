class MathUtils:
    @staticmethod
    def float_range(start: float, stop: float, step: float):
        values = []
        x = start
        while x <= stop + 1e-9:
            values.append(round(x, 1))
            x += step
        return values
