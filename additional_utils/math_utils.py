class MathUtils:
    @staticmethod
    def float_range(start: float, stop: float, step: float):
        values = [start]
        x = start
        while x <= stop + 1e-9:
            x += step
            values.append(round(x, 1))
        return values
