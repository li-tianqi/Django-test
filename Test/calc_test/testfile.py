import os

def testfile():
    print("start")
    os.mknod("test.txt")
    print("done")
	
	
if __name__ == "__main__":
    testfile()