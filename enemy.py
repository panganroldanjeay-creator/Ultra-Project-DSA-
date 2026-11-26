from src.api import EnemyDefinition, Position


class Enemy:
    """Expose read-only identity, position, and nonnegative encounter penalty."""

    def __init__(self, enemy_id: str, position: Position, encounter_penalty: int) -> None:
        EnemyDefinition(enemy_id, position, encounter_penalty)
        self._enemy_id = enemy_id
        self._position = position
        self._encounter_penalty = encounter_penalty

    @property
    def enemy_id(self) -> str:
        return self._enemy_id

    @property
    def position(self) -> Position:
        return self._position

    @property
    def encounter_penalty(self) -> int:
        return self._encounter_penalty
