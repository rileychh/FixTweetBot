"""AddSilent Migration."""

from masoniteorm.migrations import Migration

class AddSilent(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.table("guilds") as table:
            table.boolean("silent").default(False)

    def down(self):
        """
        Revert the migrations.
        """
        with self.schema.table("guilds") as table:
            table.drop_column("silent")