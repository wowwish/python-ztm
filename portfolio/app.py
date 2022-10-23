# Flask for the app object, render_template to render HTML files, url_for to create static asset url, request handler, page redirection
import email
from flask import Flask, render_template, url_for, request, redirect
import csv # built-in module to write/read to CSV file

app = Flask(__name__) # __name__ = '__main__' - The name of the app is set to '__main__' essentially

@app.route("/")
def my_home():
    return render_template('index.html')

# @app.route('/about.html')
# def about():
#     return render_template('about.html')

# @app.route('/works.html')
# def works():
#     return render_template('works.html')

# @app.route('/contact.html')
# def contacts():
#     return render_template('contact.html')

@app.route('/<string:page_name>') # url query variable of type string 
def html_page(page_name): # route-handler that takes the page name as an argument
    return render_template(page_name)


def write_to_file(data): # function to write submitted contact form info (dictionary) to a file on the server machine
    with open('database.txt', 'a') as database: # append to 'database.txt'
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{email},{subject},{message}')


def write_to_csv(data): # write request data from the contact form into a CSV file on the server machine
    with open('database.csv', newline='', mode='a') as database2: # append to 'database.csv'
        email = data['email']
        subject = data['subject']
        message = data['message']
        # Initialize a writer to CSV file, delimiting columns with ',' and with quotes around the values
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL) # use csv.QUOTE_MINIMAL for no quotes
        # write a single row into the CSV file through the csv_writer object
        csv_writer.writerow([email, subject, message])

# Handle requests from the Contact Form in 'contact.html'
@app.route('/submit_form', methods=['POST', 'GET']) # Route with allowed HTTP Methods for requests
def submit_form():
    # Data submitted from the Form using GET/POST method to this route can be accessed using its "name" attribute
    # The 'request' object is a proxy global object that acts as a context local to the data submitted to the route
    if request.method == 'POST':
        try:
            data = request.form.to_dict() # Get all the passed data in the form of a dictionary 
            # where key is the "name" attribute of the input and value is the data corresponding to that input
            # print(data) # print the data dictionary to the console running this script
            write_to_csv(data)
            return redirect('/thankyou.html') # redirect to 'thankyou.html' route
        except:
            return 'did not save to database!'
    else:
        return 'something went wrong, try again !'