#!/usr/bin/env	python

import curses
import traceback

import Host

def build_interface(stdscr):
	global screen #TODO Why does this need to be global?

	(max_y, max_x) = stdscr.getmaxyx()
 	master_pad = curses.newpad(max_y, max_x)
	
	#screen_topleft = curses.newwin(max_y/2, max_x/2, 0, 0)
        #screen_topleft.addstr(0, 2, "Client List")
	
	#declare some commonly used string graphics
	hline_break = '-' * (max_x/2)
        hline = "  -----   -----   ----- "
        vline = "| ' ' ' | ' ' ' | ' ' ' |"
        usg_msg = "Use arrow keys to move.\n  1-9 are valid entries.\n  Use 0 to reset a value.\n  Options: [d]one, [q]uit"
        sure_msg = "Are you sure? (y/n): "
        another_msg = "Try another? (y/n): "
        
	'''
	for y in xrange(1,14):
                if ((y-1)%4 == 0):
                        screen.addstr(y, 1, hline)
                else:
                        screen.addstr(y, 1, vline)
	'''
	#add necessary strings to screen
	screen_topleft.addstr(1,0, hline_break)
        #screen_topleft.addstr((max_y/2)-1,0, usg_msg)
	screen_topleft.move(2, 3)
	
        #screen.box()
        #screen.hline()
        screen_topleft.refresh()
        #screen.nodelay(1)
        while True:
                c = screen_topleft.getch()
		
                (y,x) = screen_topleft.getyx()
                #screen.addstr(0,0, str(c))
                if c == ord('d') or c == ord('q'):
                        screen_topleft.addstr(19, 2, sure_msg)
                        screen_topleft.refresh()
                        ans = screen_topleft.getch()
                        if ans != ord('y'):
                                screen_topleft.move(19,0)
                                screen_topleft.clrtoeol()
                                screen_topleft.move(y,x)        #move back to where the cursor was
                        else:
                                if c == 'q':
                                        #quit signal received, break out of the while loop
                                        #break
                                        return
def read_in_hosts(infile):
	"""arg: filename to open
	   out: A list of Host instances 
	   description: open infile, read items, create list of Host instances
	"""
	try:
		file_handle = open(infile)
		file_lines = file_handle.readlines()
		file_handle.close()
	except IOError:
		#TODO Take into account curses...
		print ("Error opening %s" % infile)
		exit(1)

	host_list = []
	for line in file_lines:
		#Split the line by whitespace, and verify it's not a comment
		if (line.strip()[0] != '#'): 
			line_items = line.split()
			host_list.append(Host.Host(line_items[0].strip(), line_items[1].strip()))
			
	return host_list		

	

def main():
	#TODO add curses wrapper???

	#TODO actually read from a .cfg file
	#TEMP
	client_infile = "clients.txt"
	server_infile = "servers.txt"	
	#/TEMP

	clientHost_list = read_in_hosts(client_infile)
	serverHost_list = read_in_hosts(server_infile)	

	#build_main_window(stdscr)

	print("***%d clients read in" % len(clientHost_list))
	print("***%d servers read in" % len(serverHost_list))	
	
	

if __name__=='__main__':
	main ()
	'''
	try:
		stdscr = curses.initscr()

		curses.noecho()
		curses.cbreak()
		stdscr.keypad(1)
		
		#Launch main
		main (stdscr)

		#Remove curses settings
		stdscr.keypad(0)
		curses.echo()
		curses.nocbreak()
		curses.endwin() 	#terminates curses
	except:
		stdscr.keypad(0)
		curses.echo()
		curses.nocbreak()
		curses.endwin()
		traceback.print_exc()
	'''
