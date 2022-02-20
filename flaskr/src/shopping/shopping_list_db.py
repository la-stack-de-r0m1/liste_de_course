import array
import string

class ShoppingListDb:
    def __init__(self, db_object) -> None:
        self.db_object = db_object

    def find_one_by(self, user_id: int, list_name: string) -> array:
        shopping_list = self.db_object.execute(
            'SELECT * '
            ' FROM shopping_list '
            ' WHERE owner_id = ? AND list_name = ?',
            (user_id, list_name,)
        ).fetchone()

        return shopping_list

    def find_all_by_user(self, user_id: int) -> list:
        user_shopping_list = self.db_object.execute(
            'SELECT id, list_name'
            ' FROM shopping_list '
            ' WHERE owner_id = ?',
            (user_id,)
        ).fetchall()

        return user_shopping_list

    def create_one(self, user_id: int, new_list_name: str) -> None:
        content = f'{{"items":[], "name": "{new_list_name}" }}'
        self.db_object.execute(
            "INSERT INTO shopping_list (owner_id, content, list_name) VALUES (?, ?, ?)",
            (user_id, content, new_list_name),
        )
        self.db_object.commit()

    def delete_one(self, user_id: int, list_name: str) -> None:
        self.db_object.execute(
            "DELETE FROM shopping_list WHERE owner_id = ? AND list_name = ?",
            (user_id, list_name),
        )
        self.db_object.commit()

    def update_list_name(self, user_id: int, old_name: str, new_name: str) -> None:
        self.db_object.execute(
            'UPDATE shopping_list SET list_name = ? '
            ' WHERE owner_id = ? AND list_name = ?',
            (new_name, user_id, old_name,)
        )
        self.db_object.commit()

    

    