class Report:
    def render(self, data) -> str:
        return self._format_header() + self._format_body(data) + self._format_footer()

    def _format_header(self) -> str:
        pass

    def _format_body(self) -> str:
        pass

    def _format_footer(self) -> str:
        pass

class HtmlReport(Report):
    def _format_header(self) -> str:
        return '<h1>Report</h1>'

    def _format_body(self, data: list) -> str:
        return '<ul><li>' + '</li><li>'.join(data) + '</li></ul>'

    def _format_footer(self) -> str:
        return '<p>End</p>'