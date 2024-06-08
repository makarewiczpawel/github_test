# Smarfon może być włączony lub wyłączony oraz posiada określoną pamięć wewnętrzną
# Można na nim instalować aplikacje, które zużywają pamięć
# Napisz klasę, która obsłuży ten przypadek
# Stwórz jej instancję i sprawdź działanie

class Smartphone:
    all_apps_list = []

    def __init__(self, name, phone_memory):
        self.name = name
        self.phone_memory = phone_memory
        self.app_list = []
        self.power_on = False

    def describe_phone(self):
        # Smartphone description
        installed_apps = ', '.join([app.app_name for app in self.app_list]) if self.app_list else "no apps installed"
        print(f"Your phone {self.name} contains {self.phone_memory} MB memory and has installed: {installed_apps}.")

    def power(self, state):
        # Turning on the phone
        if state == 'on':
            self.power_on = True
            print(f"{self.name} is now ON.")
        elif state == 'off':
            self.power_on = False
            print(f"{self.name} is now OFF.")
        else:
            print("Invalid power state. Use 'on' or 'off'.")

    def install_app(self, app):
        if not self.power_on:
            print(f"Cannot install {app.app_name}. {self.name} is OFF.")
            return

        if any(installed_app.app_name == app.app_name for installed_app in self.app_list):
            print(f"Installing {app.app_name} on {self.name}.")
            print(f"{app.app_name} is already installed.")
        elif self.phone_memory < app.app_memory:
            print(f"Installing {app.app_name} on {self.name}.")
            print("Not enough phone memory.")
        else:
            self.phone_memory -= app.app_memory
            print(f"Installing {app.app_name} on {self.name}.")
            self.app_list.append(app)
            print(f"List of installed apps on {self.name}: {[app.app_name for app in self.app_list]}.")
            print(f"Your actual {self.name} memory: {self.phone_memory} MB.")

    def uninstall_app(self, app_name):
        if not self.power_on:
            print(f"Cannot uninstall {app_name}. {self.name} is OFF.")
            return

        for app in self.app_list:
            if app.app_name == app_name:
                self.phone_memory += app.app_memory
                self.app_list.remove(app)
                print(f"Uninstalling {app_name} from {self.name}.")
                print(f"List of installed apps on {self.name}: {[app.app_name for app in self.app_list]}.")
                print(f"Your actual {self.name} memory: {self.phone_memory} MB.")
                return
        print(f"{app_name} is not installed on {self.name}.")

    def list_installed_apps(self):
        return [app.app_name for app in self.app_list]

    @classmethod
    def uninstall_all_apps(cls):
        cls.all_apps_list.clear()


class App:
    def __init__(self, app_name, app_memory):
        self.app_name = app_name
        self.app_memory = app_memory


iphone = Smartphone("iPhone", 500)
iphone.describe_phone()

# Turning on the phone before app installation
iphone.power('on')

facebook = App("Facebook", 300)
whatsapp = App("WhatsApp", 100)
messenger = App("Messenger", 100)

iphone.install_app(facebook)
iphone.install_app(whatsapp)
iphone.install_app(messenger)
iphone.install_app(facebook)  # Próba ponownej instalacji aplikacji

# Wyłączanie telefonu przed próbą odinstalowania aplikacji
iphone.power('off')
iphone.uninstall_app("WhatsApp")  # Próba odinstalowania przy wyłączonym telefonie

# Włączanie telefonu i odinstalowywanie aplikacji
iphone.power('on')
iphone.uninstall_app("WhatsApp")

print("Installed apps:", iphone.list_installed_apps())
