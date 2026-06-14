class Password:
    @staticmethod
    def is_strong(p: str) -> bool:
        return (len(p) >= 8 and any(c.isdigit() for c in p) and any(c.isupper() for c in p) and any(c.islower() for c in p))