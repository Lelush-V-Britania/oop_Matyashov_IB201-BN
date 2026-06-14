class Document:
    def __init__(self, title: str, content: str):
        self.title = title
        self._content = content
        self.__audit_log = []

    def read(self) -> str:
        return self._content

    def history(self) -> tuple:
        return tuple(self.__audit_log)

    def _log(self, event: str) -> None:
        self.__audit_log.append(event)


class EditorDocument(Document):
    def edit(self, new_content: str) -> None:
        self._log(f"edit: {self._content} -> {new_content}")
        self._content = new_content


class AdminDocument(EditorDocument):
    def purge_history(self) -> None:
        self._Document__audit_log.clear()