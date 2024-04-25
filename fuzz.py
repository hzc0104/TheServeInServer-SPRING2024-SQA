import hypothesis.strategies as st
from hypothesis import given
import subprocess
import os
from git.repo.miner import (deleteRepo, makeChunks, cloneRepo, dumpContentIntoFile,
                         getPythonCount, getMLLibraryUsage) 
 
# Fuzzing deleteRepo() function
@given(st.text(), st.text())
def test_deleteRepo(dirName, type_):
    try:
        deleteRepo(dirName, type_)
        # Print or log the deletion message to check for errors
        print("Deleted", type_, "in", dirName)
    except Exception as e:
        print(f"Error in deleteRepo({dirName}, {type_}): {e}")
 
# Fuzzing makeChunks() function
@given(st.lists(st.text()), st.integers(min_value=1, max_value=10))
def test_makeChunks(the_list, size_):
    try:
        chunks = makeChunks(the_list, size_)
        # Print or log the chunks to check for errors
        print("Chunks:", list(chunks))
    except Exception as e:
        print(f"Error in makeChunks({the_list}, {size_}): {e}")
 
# Fuzzing cloneRepo() function
@given(st.text(), st.text())
def test_cloneRepo(repo_name, target_dir):
    try:
        cloneRepo(repo_name, target_dir)
        # Print or log the cloning message to check for errors
        print("Cloned", repo_name, "to", target_dir)
    except Exception as e:
        print(f"Error in cloneRepo({repo_name}, {target_dir}): {e}")
 
# Fuzzing dumpContentIntoFile() function
@given(st.text(), st.text())
def test_dumpContentIntoFile(strP, fileP):
    try:
        size = dumpContentIntoFile(strP, fileP)
        # Print or log the file size to check for errors
        print("Dumped content into", fileP, "with size", size)
    except Exception as e:
        print(f"Error in dumpContentIntoFile({strP}, {fileP}): {e}")
 
# Fuzzing getPythonCount() function
@given(st.text())
def test_getPythonCount(input_dir):
    try:
        count = getPythonCount(input_dir)
        # Print or log the count to check for errors
        print("Python file count in", input_dir, ":", count)
    except Exception as e:
        print(f"Error in getPythonCount({input_dir}): {e}")
 
# Run fuzz tests for each function
if __name__ == "__main__":
    print("Running fuzz tests for deleteRepo()...")
    for _ in range(5):
        test_deleteRepo()
    print("Running fuzz tests for makeChunks()...")
    for _ in range(5):
        test_makeChunks()
    print("Running fuzz tests for cloneRepo()...")
    for _ in range(5):
        test_cloneRepo()
    print("Running fuzz tests for dumpContentIntoFile()...")
    for _ in range(5):
        test_dumpContentIntoFile()
    print("Running fuzz tests for getPythonCount()...")
    for _ in range(5):
        test_getPythonCount()
