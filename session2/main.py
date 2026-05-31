from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def draw(self) -> str:
        raise NotImplementedError


class Circle(Shape):
    def draw(self) -> str:
        return "Drawing a circle"


class Square(Shape):
    def draw(self) -> str:
        return "Drawing a square"


def shape_factory(shape_type: str) -> Shape:
    shape_type = shape_type.lower()
    if shape_type == "circle":
        return Circle()
    if shape_type == "square":
        return Square()
    raise ValueError(f"Unknown shape type: {shape_type}")


def main() -> None:
    shapes = [shape_factory("circle"), shape_factory("square")]
    for shape in shapes:
        print(shape.draw())


if __name__ == "__main__":
    main()
