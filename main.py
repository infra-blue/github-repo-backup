"""Main module"""
import os
import schedule
from modules.backup import backup_task
from modules.config import config_map

def main() -> None:
    """Main function"""
    os.chdir(os.path.dirname(__file__) + '/backup')
    backup_task()
    schedule.every(config_map['auto_update_time']).minutes.do(backup_task)

    while True:
        schedule.run_pending()

if __name__ == "__main__":
    main()
