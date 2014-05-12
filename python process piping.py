from multiprocessing import Process, Pipe
import time
import os

def printMe(pipe_connection, x):
	##  Send this process ID back to the parent process
	##   through a pipe connection
	##
	pipe_connection.send( os.getpid() )
	pipe_connection.close()
	
	##  Do something
	##
	print '  ' + str(x)
	print 'I did an action and my pid is:  ' + str(os.getpid())

	##  Testing, so sleep the function so you can read the PID in activity monitor
	##
	time.sleep(3)
	print '  I am dead'



def p():
	##  Create a multiprocessing pip connection
	##   It has a parent and child connection object
	##    Pass the child object to receive messages back
	##
	parent_connection, child_connection = Pipe()

	##  Create the Process
	##
	d = 
	p = Process(target=printMe, args=(child_connection,'bob',))
	p.start()
	print 'The parent knows the childs PID:'
	print parent_connection.recv()  #prints the PID of the process
	p.join()