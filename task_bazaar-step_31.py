# === Stage 31: Добавь переключение активного пользовательского профиля ===
# Project: TaskBazaar
def switch_profile(self, profile_name: str) -> dict:
        """Переключение активного профиля пользователя."""
        if profile_name not in self.profiles:
            return {"error": f"Профиль '{profile_name}' не найден"}
        self._active_profile = profile_name
        return {
            "message": f"Переключено на профиль: {profile_name}",
            "active_profile": profile_name,
        }
