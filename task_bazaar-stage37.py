# === Stage 37: Добавь мини-набор unit-тестов без внешних зависимостей ===
# Project: TaskBazaar
import unittest


class TestTaskBazaar(unittest.TestCase):
    def test_add_task(self):
        from task_bazaar import TaskBazaar
        app = TaskBazaar()
        app.add_task("Купить молоко", 50, "high")
        self.assertEqual(len(app.tasks), 1)
        self.assertEqual(app.tasks[0]["title"], "Купить молоко")

    def test_add_worker(self):
        from task_bazaar import TaskBazaar
        app = TaskBazaar()
        app.add_worker("Алексей", 100, "python")
        self.assertEqual(len(app.workers), 1)
        self.assertEqual(app.workers[0]["name"], "Алексей")

    def test_add_bid(self):
        from task_bazaar import TaskBazaar
        app = TaskBazaar()
        app.add_task("Сделать сайт", 500, "medium")
        app.add_worker("Мария", 300, "html")
        app.add_bid("Мария", "Сделать сайт", 200)
        self.assertEqual(len(app.bids), 1)
        self.assertEqual(app.bids[0]["worker"], "Мария")
        self.assertEqual(app.bids[0]["amount"], 200)

    def test_task_history(self):
        from task_bazaar import TaskBazaar
        app = TaskBazaar()
        app.add_task("Тест", 10, "low")
        app.add_worker("Петя", 5, "test")
        app.add_bid("Петя", "Тест", 3)
        app.complete_task("Тест", "Петя")
        self.assertEqual(len(app.history), 1)
        self.assertEqual(app.history[0]["task"], "Тест")
        self.assertEqual(app.history[0]["status"], "completed")

    def test_empty_app(self):
        from task_bazaar import TaskBazaar
        app = TaskBazaar()
        self.assertEqual(len(app.tasks), 0)
        self.assertEqual(len(app.workers), 0)
        self.assertEqual(len(app.bids), 0)
        self.assertEqual(len(app.history), 0)


if __name__ == "__main__":
    unittest.main()
