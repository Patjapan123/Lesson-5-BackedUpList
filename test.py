from code import BackedUpList

foo = BackedUpList([4,3])
foo.set([3,4])

foo.append(3)
foo.set_element(2,2)
if foo.get() == [3,4,2]:
	print("Test Case 1 Passed!")
else:
	print("Test Case 1 Failed, view test.py code")

foo.backup()
foo.pop()
foo.get() #shouldn't alter value
if foo.get() == [3,4]:
	print("Test Case 2 Passed!")
else:
	print("Test Case 2 Failed, view test.py code")

foo.rollback()
if foo.get() == [3,4,2]:
	print("Test Case 3 Passed!")
else:
	print("Test Case 3 Failed, view test.py code")
foo.rollback()
foo.rollback()
if foo.get_element(1) == 4:
	print("Test Case 4 Passed!")
else:
	print("Test Case 4 Failed, view test.py code")

