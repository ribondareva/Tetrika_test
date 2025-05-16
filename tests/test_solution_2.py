import unittest
from unittest.mock import patch, mock_open
from task2.solution_2 import get_html, get_animals_and_next, write_csv


class TestAnimalParser(unittest.TestCase):

    @patch("task2.solution_2.urllib.request.urlopen")
    def test_get_html(self, mock_urlopen):
        mock_urlopen.return_value.__enter__.return_value.read.return_value = (
            b"<html><body>Test</body></html>"
        )
        html = get_html("/wiki/Категория:Животные_по_алфавиту")
        self.assertIn("Test", html)

    @patch("task2.solution_2.get_html")
    def test_get_animals_and_next(self, mock_get_html):
        html = """
        <div class="mw-category-group">
            <ul><li>Аист</li><li>Бобр</li></ul>
        </div>
        <a href="/next" title="Следующая страница">Следующая страница</a>
        """
        mock_get_html.return_value = html
        animals, next_url = get_animals_and_next("/fake-url")
        self.assertEqual(animals, ["Аист", "Бобр"])
        self.assertEqual(next_url, "/next")

    @patch("builtins.open", new_callable=mock_open)
    def test_write_csv(self, m_open):
        stats = {"А": 2, "Б": 3, "В": 7}
        write_csv(stats)

        m_open.assert_called_once_with(
            "beasts.csv", "w", encoding="utf-8", newline=""
        )
        handle = m_open()
        written = "".join(call.args[0] for call in handle.write.call_args_list)
        self.assertIn("А,2", written)
        self.assertIn("Б,3", written)
        self.assertIn("В,7", written)


if __name__ == "__main__":
    unittest.main()
