# Launch a web app with a simple form to demonstrate how to respond to a button click.
# python app_ui.py

import param
import panel as pn

class AppUI(param.Parameterized):
    start_id = param.String(label="Start ID", default="")
    end_id = param.String(label="End ID", default="")
    fetch_button = param.Action(lambda x: x.param.trigger('fetch_button'), label="Fetch")
    
    @param.depends('fetch_button', watch=True)
    def fetch_data(self):
        start = self.start_id
        end = self.end_id
        
        # Call your desired function here with the start_id and end_id
        print(f"Fetching data for IDs from {start} to {end}")

def main():
    app = AppUI()
    layout = pn.Row(app.param)
    layout.show()

if __name__ == "__main__":
    main()