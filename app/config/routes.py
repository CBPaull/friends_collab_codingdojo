from system.core.router import routes

routes['default_controller'] = 'Friends'
# Render index page
routes['/friends'] = 'Friends#index'
# Render show friend page
routes['/friends/show/<f_id>'] = 'Friends#show'
# Render edit friend page
routes['/friends/edit/<f_id>'] = 'Friends#edit'
# Render create friend page
routes['/friends/create'] = 'Friends#create'
# Process update friend form
routes['POST']['/friends/update'] = 'Friends#update'
# Process delete friend
routes['POST']['/friends/delete'] = 'Friends#delete'
# Process new friend form
routes['POST']['/friends/new'] = 'Friends#new'