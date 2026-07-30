from __future__ import annotations

import unittest
from pathlib import Path
from unittest.mock import patch

from fastapi.testclient import TestClient

from backend import main


class TicketFlowTest(unittest.TestCase):
    def setUp(self) -> None:
        self.database_path = Path(__file__).parent / "_ticket_flow.sqlite3"
        self.database_path.unlink(missing_ok=True)
        self.db_patch = patch.object(main.config, "TICKET_DB", self.database_path)
        self.db_patch.start()
        main.init_ticket_database()
        self.client = TestClient(main.app)

    def tearDown(self) -> None:
        self.db_patch.stop()
        self.database_path.unlink(missing_ok=True)

    def test_escalated_question_is_visible_and_answerable(self) -> None:
        with (
            patch.object(main, "retrieve", return_value={"found": False}),
            patch.object(
                main,
                "generate",
                return_value={
                    "answer": "Mình chưa tìm thấy kiến thức này.",
                    "grounded": False,
                    "mode": "none",
                },
            ),
        ):
            chat = self.client.post(
                "/api/chat", json={"question": "Deadline chính thức là khi nào?"}
            )
        self.assertEqual(chat.status_code, 200)
        payload = chat.json()
        self.assertEqual(payload["status"], "escalated")
        self.assertTrue(payload["ticket_id"])

        pending = self.client.get("/api/questions?status=pending").json()
        self.assertEqual(len(pending), 1)
        self.assertEqual(pending[0]["question"], "Deadline chính thức là khi nào?")

        answered = self.client.post(
            f"/api/questions/{payload['ticket_id']}/answer",
            json={"answer": "Deadline chính thức là 23:59 hôm nay."},
        )
        self.assertEqual(answered.status_code, 200)
        self.assertEqual(
            self.client.get("/api/questions?status=pending").json(), []
        )
        answered_rows = self.client.get("/api/questions?status=answered").json()
        self.assertEqual(len(answered_rows), 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
