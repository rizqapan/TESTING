# === Stage 33: Добавь откат последнего действия там, где это разумно ===
# Project: TaskBazaar
class Action:
    def __init__(self, action_type, data, actor):
        self.action_type = action_type
        self.data = data
        self.actor = actor
        self.timestamp = datetime.now()

    def undo(self):
        if self.action_type == "create_task":
            return {"tasks": [], "task_id": self.data.get("task_id")}
        elif self.action_type == "create_bid":
            return {"bids": [], "bid_id": self.data.get("bid_id")}
        elif self.action_type == "create_worker":
            return {"workers": [], "worker_id": self.data.get("worker_id")}
        elif self.action_type == "update_priority":
            return {"tasks": [], "task_id": self.data.get("task_id")}
        elif self.action_type == "update_bid_amount":
            return {"bids": [], "bid_id": self.data.get("bid_id")}
        elif self.action_type == "update_bid_status":
            return {"bids": [], "bid_id": self.data.get("bid_id")}
        elif self.action_type == "update_task_status":
            return {"tasks": [], "task_id": self.data.get("task_id")}
        elif self.action_type == "update_task_description":
            return {"tasks": [], "task_id": self.data.get("task_id")}
        elif self.action_type == "update_task_deadline":
            return {"tasks": [], "task_id": self.data.get("task_id")}
        elif self.action_type == "update_worker_expertise":
            return {"workers": [], "worker_id": self.data.get("worker_id")}
        elif self.action_type == "delete_task":
            return {"tasks": []}
        elif self.action_type == "delete_bid":
            return {"bids": []}
        elif self.action_type == "delete_worker":
            return {"workers": []}
        else:
            return None
