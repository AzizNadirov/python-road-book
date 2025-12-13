from pathlib import Path

def find_files(path: Path, 
               pattern: str,
               recursive: bool=True)->list[Path]:
    """ search for files matching `pattern` in `path` directory """
    if not path.is_dir():
        raise ValueError(f"'{path}' must be a directory!")
    if recursive:
        return list(path.rglob(pattern))
    else:
        return list(path.glob(pattern))

# Documents qovluğunda bütün .pdf fayllarını tapaq
print(find_files(Path.home() / "Documents", "*.pdf", recursive=True))





def rm_tree(path: Path)->bool:
    """ remove all files and directories in `path` """
    if not path.is_dir():
        print(f"{path.as_posix()} must be a directory!")
        return False
    if not path.exists():
        print(f"{path.as_posix()} does not exist!")
        return False
    
    for child in path.iterdir():
        if child.is_file():
            print(f"Removing file: '{child}'")
            child.unlink()
        else:
            print(f"Removing directory: {child}")
            rm_tree(child)
    path.rmdir()
    print(f"'{path}' deleted.")
    return True

test_dir = Path.cwd() / "test_dir"
rm_tree(test_dir)