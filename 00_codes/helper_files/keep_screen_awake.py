import ctypes
import time
from tqdm import tqdm
import sys


def keep_screen_awake(interval=60, duration=5*60*60):
    """
    Prevents the screen from going to sleep by simulating a mouse movement every `interval` seconds.
    """
    total_intervals = duration // interval
    start_time = time.time()
    try:
        
        # pbar = tqdm(range(total_intervals), desc="Elapsed Time: 00:00", unit="intervals", ncols=80)
        # pbar = tqdm(range(total_intervals), desc="Keeping Screen Awake", unit="intervals", ncols=80)
        # for _ in range(total_intervals):
        for _ in tqdm(range(total_intervals), desc="Keeping Screen Awake", unit="intervals", ncols=80):
            # elapsed_time = time.time() - start_time
            # minutes, seconds = divmod(int(elapsed_time), 60)
            # time_str = f"{minutes:02}:{seconds:02}"
            
            # pbar.set_description(f"Elapsed Time: {time_str}")
            # pbar.update(1)
            
            # sys.stdout.write(f"\r{time_str}")
            # sys.stdout.flush()
            # Move the mouse slightly to keep the screen awake
            ctypes.windll.user32.mouse_event(0x0001, 1, 0, 0, 0)  # Move mouse right
            ctypes.windll.user32.mouse_event(0x0001, -1, 0, 0, 0)  # Move mouse left
            
            # mouse_event(dwFlags, dx, dy, dwData, dwExtraInfo) 
            # -- dx dy are specified in mickey -- amount that a mouse has to move for it to report that it has mvoed
            # print("Moved mouse to keep screen awake")
            time.sleep(interval)
            
            
    except KeyboardInterrupt:
        print("Program terminated by user.")

if __name__ == "__main__":
    keep_screen_awake()
