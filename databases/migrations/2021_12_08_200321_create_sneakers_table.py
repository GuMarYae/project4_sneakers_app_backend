"""CreateTodosTable Migration."""

from masoniteorm.migrations import Migration

class CreateSneakersTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("sneakers") as table:
            table.increments("id")
            table.string("brand")
            table.string("name")
            table.string("cost")
            table.string("year")
            table.string("image")
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("sneakers")
        
        
        
        
        
       