import os, scriptengine, sys

class Checkout_Project:

	try:
		if projects.primary:
			projects.primary.close()

		def set_username(req):
			req.username = svn-service
			req.password = 'PASSWORD'
			req.save = True 

		svn.auth_username_password += set_username
		print('scriptmessage: checking out ' + sys.argv[1] + ' to ' + sys.argv[2])
		proj = svn.checkout(sys.argv[1], sys.argv[2], sys.argv[3])

		proj.save()
		proj.close()
		system.exit()
		
	except Exception as exception:
		print("scriptmessage: ERROR running script: " + os.path.basename(__file__) + "  -  " + str(exception))
		system.exit()
		
