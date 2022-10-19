behavior: BackedUpList should be a class that is an interface for a list. It should hold the following functions:
	__init__(newlist) initializes the list to the given one
	-set(newlist) sets the current list to a given one (like init but if you wanna change it)
	-set_element(index,newvalue) sets an item in the list at index to newvalue
	-append(value) adds a value to the end of the list
	-pop() removes the last value from the list
	-get_element(index) returns the value at index in the list
	-get() returns the current list
	-backup() saves the list in a second place, "backs it up", for retrieving later; only one backup is saved.
	-rollback() sets the list to its current backup, and the current backup is cleared (extra credit if the current list is now saved as a backup)