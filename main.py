import os

output_dir = "/output"
os.makedirs(output_dir, exist_ok=True)

joke = "I told my boss I'm 'multitasking,' which is just typing fast while panicking silently in a tab the boss can't see."
entry_path = os.path.join(output_dir, "entry.txt")
with open(entry_path, "w") as f:
    f.write(joke)