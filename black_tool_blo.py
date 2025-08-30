import os
import shutil
from datetime import datetime

def main():
    print("📦 Простой инструмент резервного копирования")
    print("—" * 50)

    # Ввод путей
    source = input("📁 Путь к папке для резервного копирования: ").strip()
    
    if not os.path.exists(source):
        print("❌ Исходная папка не найдена. Проверь путь.")
        return
    if not os.path.isdir(source):
        print("❌ Указанный путь — не папка.")
        return

    backup_dir = input("💾 Путь к папке для бэкапов (например, D:/Backups): ").strip()
    backup_dir = os.path.expanduser(backup_dir)  # Поддержка ~
    
    if not os.path.exists(backup_dir):
        create = input("❓ Папка для бэкапов не существует. Создать? (д/н): ").strip().lower()
        if create in ('д', 'y', 'yes', 'да'):
            try:
                os.makedirs(backup_dir)
                print(f"✅ Создана папка: {backup_dir}")
            except Exception as e:
                print(f"❌ Не удалось создать папку: {e}")
                return
        else:
            print("🛑 Операция отменена.")
            return

    # Генерация имени с датой и временем
    folder_name = os.path.basename(os.path.normpath(source))
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    backup_path = os.path.join(backup_dir, f"{folder_name}_backup_{timestamp}")

    print("\n🔍 Начинаем копирование...")
    try:
        shutil.copytree(source, backup_path)
        print("✅ Резервная копия создана!")
        print(f"📍 Сохранено в: {backup_path}")
    except Exception as e:
        print(f"❌ Ошибка при копировании: {e}")
        return

    print("\n📌 Совет: Добавь этот скрипт в расписание (через cron или Планировщик задач), чтобы бэкапы были автоматическими.")

if __name__ == "__main__":
    main()
