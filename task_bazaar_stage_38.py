# === Stage 38: Добавь расширенный набор тестов для ошибок и пограничных случаев ===
# Project: TaskBazaar
import unittest
from taskbazaar.tasks import Task
from taskbazaar.workers import Worker
from taskbazaar.offers import Offer
from taskbazaar.history import History

class TestTaskEdgeCases(unittest.TestCase):
    def test_task_with_zero_budget(self):
        t = Task("test", 0, 1, 0)
        t.validate()
        self.assertEqual(t.status, "pending")

    def test_task_with_negative_budget(self):
        t = Task("test", -5, 1, 0)
        with self.assertRaises(ValueError):
            t.validate()

    def test_task_with_priority_out_of_range(self):
        t = Task("test", 10, 1, 0)
        with self.assertRaises(ValueError):
            t.validate()

    def test_worker_with_zero_skills(self):
        w = Worker("test", "test", 0, 0)
        w.validate()
        self.assertEqual(w.status, "idle")

    def test_offer_with_zero_budget(self):
        o = Offer(0, "test", 1, 0)
        o.validate()
        self.assertEqual(o.status, "pending")

    def test_offer_with_negative_budget(self):
        o = Offer(-5, "test", 1, 0)
        with self.assertRaises(ValueError):
            o.validate()

    def test_offer_with_priority_out_of_range(self):
        o = Offer(10, "test", 1, 0)
        with self.assertRaises(ValueError):
            o.validate()

    def test_history_with_empty_data(self):
        h = History()
        h.add("test", "test", 0, "success")
        self.assertEqual(len(h.data), 1)

    def test_history_with_negative_value(self):
        h = History()
        with self.assertRaises(ValueError):
            h.add("test", "test", -5, "success")

    def test_history_with_invalid_status(self):
        h = History()
        with self.assertRaises(ValueError):
            h.add("test", "test", 0, "invalid")

if __name__ == "__main__":
    unittest.main()
