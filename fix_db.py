from app import app, db
from sqlalchemy import text

def update_database():
    with app.app_context():
        try:
            # On exécute les commandes SQL
            db.session.execute(text("ALTER TABLE intention ADD COLUMN IF NOT EXISTS telephone VARCHAR(20);"))
            db.session.execute(text("ALTER TABLE intention ADD COLUMN IF NOT EXISTS nature_id VARCHAR(10);"))
            db.session.execute(text("ALTER TABLE intention ADD COLUMN IF NOT EXISTS paye BOOLEAN DEFAULT FALSE;"))
            db.session.execute(text("UPDATE intention SET paye = TRUE WHERE paye IS NULL;"))
            
            db.session.commit()
            print("✅ Félicitations ! Les colonnes ont été ajoutées avec succès.")
        except Exception as e:
            db.session.rollback()
            print(f"❌ Erreur lors de la mise à jour : {e}")

if __name__ == "__main__":
    update_database()
