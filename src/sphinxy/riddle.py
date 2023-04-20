from dataclasses import dataclass
from typing import Iterator


@dataclass(frozen=True)
class Riddle:
    """Class Riddle

    Returns:
        _type_: _description_

    Yields:
        _type_: _description_
    """
    question: str
    answer: str

    def check_answer(self, answer: str) -> bool:
        """Converts provided string to lower case

        Args:
            answer (str): string

        Returns:
            lower case string as answer object
        """
        return answer.lower() == self.answer.lower()

    def get_hint(self) -> Iterator[str]:
        """Returns hint from answer function

        Yields:
            Iterator[str]: 
        """
        yield from iter(self.answer)
