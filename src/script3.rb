# Carga de los ficheros de configuración
require 'capybara'
include Capybara::DSL

# Inicializamos Capybara
Capybara.run_server = false
Capybara.default_driver = :selenium

url = "http://161.67.212.235"


i = 6400

while true do
	visit url

	page.all('#participant_email')[0].set("pedroma.almagro@gmail.com")

	page.all('#participant_password')[0].set("juanypedroma1")

	page.first('INPUT.btn.small-input.btn.btn-info').click

	i+=1

	page.all('#user_email')[0].set("bot"+i.to_s)

	page.all('#user_password')[0].set("bot"+i.to_s+"@correo.es")

	page.first('input.btn').click

	sleep 1

	page.first('a.navbar-brand:nth-child(5)').click

	while true
		for i in 0..25
			page.all('.btn.btn-pimary')[0].click
		end
	end

	page.all('next')[i].click

	page.first('.btn.btn-danger').click

end
