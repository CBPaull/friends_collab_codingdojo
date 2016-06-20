from system.core.controller import *

class Friends(Controller):
    def __init__(self, action):
        super(Friends, self).__init__(action)
        self.load_model('Friend')

    def index(self):
        all_friends = self.models['Friend'].get_all_friends()
        return self.load_view('index.html', all_friends= all_friends)

    def create(self):
        friend = None
        return self.load_view('create.html', friend = friend)

    def new(self):
        in_data = {
            'firstname': request.form['firstname'],
            'lastname': request.form['lastname'],
            'occupation': request.form['occupation'],
			'knownfor': request.form['knownfor']
        }
        f_id = self.models['Friend'].new_friend(in_data)
        return redirect('/friends/show/' + str(f_id))

    def show(self, f_id):
        friend_id = {'id': f_id}
    	friend = self.models['Friend'].get_friend_by_id(friend_id)
    	return self.load_view('show.html', friend=friend[0])

    def edit(self, f_id):
    	f_id = {'id': f_id}
    	friend = self.models['Friend'].get_friend_by_id(f_id)
    	return self.load_view('create.html', friend=friend[0])

    def update(self):
    	in_data = {
    		'firstname': request.form['firstname'],
            'lastname': request.form['lastname'],
            'occupation': request.form['occupation'],
			'knownfor': request.form['knownfor'],
			'id': request.form['f_id']
    	}
    	f_id = self.models['Friend'].update_friend(in_data)
    	return redirect('/friends/show/'+str(f_id))

    def delete(self):
        friend_id = {'id': request.form['f_id']}
        self.models['Friend'].delete_friend(friend_id)
        return redirect('/')


