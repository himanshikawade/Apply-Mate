from flask import Flask, render_template, request, jsonify
from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)

scholarship_data = {
    'Andhra Pradesh': {
        'scholarships': ['AP Scholarship for Minorities', 'Jnanabhumi Scholarship'],
        'eligibility': 'Income below 2 lakh, resident of Andhra Pradesh',
        'documents': ['Income Certificate', 'Caste Certificate', 'Aadhaar Card'],
        'application_procedure': 'Apply online through Jnanabhumi portal',
        'application_dates': {'start_date': '2024-01-15', 'end_date': '2024-03-31'}
    },
    'Arunachal Pradesh': {
        'scholarships': ['Arunachal Pradesh State Scholarship', 'North East Council Scholarship'],
        'eligibility': 'Income criteria vary based on scholarship',
        'documents': ['Income Certificate', 'Domicile Certificate', 'Marksheet'],
        'application_procedure': 'Check the state scholarship portal for details',
        'application_dates': {'start_date': '2024-02-01', 'end_date': '2024-04-30'}
    },
    'Assam': {
        'scholarships': ['Assam Scholarship for SC/ST', 'Madrassa Scholarship'],
        'eligibility': 'Income below 2.5 lakh, resident of Assam',
        'documents': ['Income Certificate', 'Caste Certificate', 'Marksheet'],
        'application_procedure': 'Apply online via Assam Scholarship Portal',
        'application_dates': {'start_date': '2024-01-10', 'end_date': '2024-03-15'}
    },
    'Bihar': {
        'scholarships': ['Bihar Scholarship for SC/ST', 'Mukhyamantri Kanya Suraksha Yojana'],
        'eligibility': 'Income below 2.5 lakh, resident of Bihar',
        'documents': ['Income Certificate', 'Caste Certificate', 'Marksheet'],
        'application_procedure': 'Applications are accepted online on the state portal',
        'application_dates': {'start_date': '2024-01-20', 'end_date': '2024-04-15'}
    },
    'Chhattisgarh': {
        'scholarships': ['Chhattisgarh State Scholarship', 'Post Matric Scholarship'],
        'eligibility': 'Income below 2 lakh, resident of Chhattisgarh',
        'documents': ['Income Certificate', 'Caste Certificate', 'Domicile Certificate'],
        'application_procedure': 'Apply online through the Chhattisgarh scholarship portal',
        'application_dates': {'start_date': '2024-01-25', 'end_date': '2024-03-31'}
    },
    'Goa': {
        'scholarships': ['Goa Scholarship for SC/ST', 'Goa Domicile Scholarship'],
        'eligibility': 'Varies by scholarship; generally income-based',
        'documents': ['Income Certificate', 'Domicile Certificate'],
        'application_procedure': 'Applications are submitted via state education department website',
        'application_dates': {'start_date': '2024-01-15', 'end_date': '2024-03-30'}
    },
    'Gujarat': {
        'scholarships': ['Gujarat Scholarship for SC/ST', 'Sardar Patel Scholarship'],
        'eligibility': 'Income below 2.5 lakh, resident of Gujarat',
        'documents': ['Income Certificate', 'Caste Certificate', 'Domicile Certificate'],
        'application_procedure': 'Apply online through the official state portal',
        'application_dates': {'start_date': '2024-01-20', 'end_date': '2024-04-15'}
    },
    'Haryana': {
        'scholarships': ['Haryana Scholarship for SC/ST', 'Post Matric Scholarship'],
        'eligibility': 'Income below 3 lakh, resident of Haryana',
        'documents': ['Income Certificate', 'Caste Certificate', 'Aadhaar Card'],
        'application_procedure': 'Submit applications through the state scholarship website',
        'application_dates': {'start_date': '2024-02-05', 'end_date': '2024-05-05'}
    },
    'Himachal Pradesh': {
        'scholarships': ['Himachal Pradesh Scholarship for SC/ST', 'Himachal Pradesh Pre Matric Scholarship'],
        'eligibility': 'Income below 2 lakh, resident of Himachal Pradesh',
        'documents': ['Income Certificate', 'Caste Certificate', 'Domicile Certificate'],
        'application_procedure': 'Apply online via the state education department portal',
        'application_dates': {'start_date': '2024-01-30', 'end_date': '2024-04-10'}
    },
    'Jharkhand': {
        'scholarships': ['Jharkhand State Scholarship', 'Post Matric Scholarship'],
        'eligibility': 'Income below 2 lakh, resident of Jharkhand',
        'documents': ['Income Certificate', 'Caste Certificate', 'Marksheet'],
        'application_procedure': 'Applications are processed online through the state portal',
        'application_dates': {'start_date': '2024-01-15', 'end_date': '2024-04-15'}
    },
    'Karnataka': {
        'scholarships': ['Karnataka State Scholarship', 'Vidyasiri Scholarship'],
        'eligibility': 'Income below 2 lakh, resident of Karnataka',
        'documents': ['Income Certificate', 'Domicile Certificate', 'Caste Certificate'],
        'application_procedure': 'Apply online via state scholarship portal',
        'application_dates': {'start_date': '2024-01-10', 'end_date': '2024-03-31'}
    },
    'Kerala': {
        'scholarships': ['Kerala State Scholarship', 'Post Matric Scholarship'],
        'eligibility': 'Income below 2.5 lakh, resident of Kerala',
        'documents': ['Income Certificate', 'Caste Certificate', 'Aadhaar Card'],
        'application_procedure': 'Applications are submitted through the state portal',
        'application_dates': {'start_date': '2024-02-01', 'end_date': '2024-05-30'}
    },
    'Madhya Pradesh': {
        'scholarships': ['Madhya Pradesh Scholarship for SC/ST', 'Post Matric Scholarship'],
        'eligibility': 'Income below 2 lakh, resident of Madhya Pradesh',
        'documents': ['Income Certificate', 'Caste Certificate', 'Marksheet'],
        'application_procedure': 'Apply online through the Madhya Pradesh scholarship portal',
        'application_dates': {'start_date': '2024-01-05', 'end_date': '2024-04-15'}
    },
    'Maharashtra': {
        'scholarships': ['Maharashtra Merit Scholarship', 'Eklavya Scholarship'],
        'eligibility': 'Income below 3 lakh, resident of Maharashtra',
        'documents': ['Income Certificate', 'Birth Certificate', 'Marksheet'],
        'application_procedure': 'Register through MahaDBT portal',
        'application_dates': {'start_date': '2024-01-15', 'end_date': '2024-04-30'}
    },
    'Manipur': {
        'scholarships': ['Manipur State Scholarship', 'Chief Minister’s Scholarship'],
        'eligibility': 'Income criteria vary based on scholarship',
        'documents': ['Income Certificate', 'Domicile Certificate', 'Marksheet'],
        'application_procedure': 'Applications are accepted online on the state portal',
        'application_dates': {'start_date': '2024-01-20', 'end_date': '2024-03-30'}
    },
    'Meghalaya': {
        'scholarships': ['Meghalaya State Scholarship', 'Pre Matric Scholarship'],
        'eligibility': 'Income below 2 lakh, resident of Meghalaya',
        'documents': ['Income Certificate', 'Caste Certificate'],
        'application_procedure': 'Apply online through the Meghalaya education department website',
        'application_dates': {'start_date': '2024-02-05', 'end_date': '2024-04-20'}
    },
    'Mizoram': {
        'scholarships': ['Mizoram State Scholarship', 'Mizoram Pre Matric Scholarship'],
        'eligibility': 'Income criteria vary by scholarship',
        'documents': ['Income Certificate', 'Domicile Certificate'],
        'application_procedure': 'Applications are processed through the Mizoram state portal',
        'application_dates': {'start_date': '2024-01-25', 'end_date': '2024-03-31'}
    },
    'Nagaland': {
        'scholarships': ['Nagaland State Scholarship', 'Chief Minister’s Scholarship'],
        'eligibility': 'Income below 2 lakh, resident of Nagaland',
        'documents': ['Income Certificate', 'Domicile Certificate'],
        'application_procedure': 'Apply online via the state government website',
        'application_dates': {'start_date': '2024-01-15', 'end_date': '2024-04-15'}
    },
    'Odisha': {
        'scholarships': ['Odisha State Scholarship', 'Post Matric Scholarship'],
        'eligibility': 'Income below 2.5 lakh, resident of Odisha',
        'documents': ['Income Certificate', 'Caste Certificate', 'Domicile Certificate'],
        'application_procedure': 'Applications are submitted through the Odisha scholarship portal',
        'application_dates': {'start_date': '2024-01-15', 'end_date': '2024-04-15'}
    },
    'Punjab': {
        'scholarships': ['Punjab Scholarship for SC/ST', 'Post Matric Scholarship'],
        'eligibility': 'Income below 2.5 lakh, resident of Punjab',
        'documents': ['Income Certificate', 'Caste Certificate', 'Domicile Certificate'],
        'application_procedure': 'Apply online through the Punjab government scholarship portal',
        'application_dates': {'start_date': '2024-01-10', 'end_date': '2024-03-30'}
    },
    'Rajasthan': {
        'scholarships': ['Rajasthan State Merit Scholarship', 'Post Matric Scholarship'],
        'eligibility': 'Income below 2 lakh, resident of Rajasthan',
        'documents': ['Income Certificate', 'Domicile Certificate', 'Caste Certificate'],
        'application_procedure': 'Apply online via the Rajasthan scholarship portal',
        'application_dates': {'start_date': '2024-02-01', 'end_date': '2024-04-15'}
    },
    'Sikkim': {
        'scholarships': ['Sikkim Merit Scholarship', 'State Scholarship for SC/ST'],
        'eligibility': 'Income below 2 lakh, resident of Sikkim',
        'documents': ['Income Certificate', 'Caste Certificate', 'Domicile Certificate'],
        'application_procedure': 'Apply through the Sikkim government portal',
        'application_dates': {'start_date': '2024-01-15', 'end_date': '2024-03-20'}
    },
    'Tamil Nadu': {
        'scholarships': ['Tamil Nadu Govt Scholarship', 'First Graduate Scholarship'],
        'eligibility': 'Income below 2.5 lakh, resident of Tamil Nadu',
        'documents': ['Domicile Certificate', 'Caste Certificate', 'Marksheet'],
        'application_procedure': 'Apply on state government website',
        'application_dates': {'start_date': '2024-01-20', 'end_date': '2024-03-25'}
    },
    'Telangana': {
        'scholarships': ['Telangana State Scholarship', 'Post Matric Scholarship'],
        'eligibility': 'Income below 2 lakh, resident of Telangana',
        'documents': ['Income Certificate', 'Caste Certificate', 'Domicile Certificate'],
        'application_procedure': 'Apply online through the Telangana scholarship portal',
        'application_dates': {'start_date': '2024-02-05', 'end_date': '2024-04-10'}
    },
    'Tripura': {
        'scholarships': ['Tripura State Scholarship', 'Merit-Cum-Means Scholarship'],
        'eligibility': 'Income below 2 lakh, resident of Tripura',
        'documents': ['Income Certificate', 'Domicile Certificate', 'Caste Certificate'],
        'application_procedure': 'Apply online through the Tripura government website',
        'application_dates': {'start_date': '2024-01-25', 'end_date': '2024-03-30'}
    },
    'Uttar Pradesh': {
        'scholarships': ['UP State Scholarship', 'Post Matric Scholarship'],
        'eligibility': 'Income below 2.5 lakh, resident of Uttar Pradesh',
        'documents': ['Income Certificate', 'Caste Certificate', 'Domicile Certificate'],
        'application_procedure': 'Register on the UP scholarship portal',
        'application_dates': {'start_date': '2024-01-01', 'end_date': '2024-03-31'}
    },
    'Uttarakhand': {
        'scholarships': ['Uttarakhand State Scholarship', 'Post Matric Scholarship'],
        'eligibility': 'Income below 2 lakh, resident of Uttarakhand',
        'documents': ['Income Certificate', 'Caste Certificate', 'Domicile Certificate'],
        'application_procedure': 'Apply through the Uttarakhand scholarship portal',
        'application_dates': {'start_date': '2024-01-15', 'end_date': '2024-04-05'}
    },
    'West Bengal': {
        'scholarships': ['West Bengal Merit-cum-Means Scholarship', 'Post Matric Scholarship'],
        'eligibility': 'Income below 2.5 lakh, resident of West Bengal',
        'documents': ['Income Certificate', 'Domicile Certificate', 'Caste Certificate'],
        'application_procedure': 'Apply online on the West Bengal scholarship portal',
        'application_dates': {'start_date': '2024-01-10', 'end_date': '2024-03-15'}
    }
}



# Initialize user state
user_state = {}


@app.route('/')
def home():
    return render_template('/home.html')


@app.route('/home.html')
def first_page():
    return render_template('/home.html')

@app.route('/index.html')
def chatbot():
    return render_template('/index.html')


@app.route('/homeState.html')
def homeState():
    return render_template('/homeState.html')


@app.route('/contact.html')
def contact():
    return render_template('/contact.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    global user_state
    user_message = request.form['message'].lower()
    user_id = request.remote_addr  # Track users by IP address

    # Initialize user state if not present
    if user_id not in user_state:
        user_state[user_id] = {'step': 'initial'}

    # Ask for home state
    if user_state[user_id]['step'] == 'initial':
        if user_message in ['hello', 'hi', 'hey']:
            user_state[user_id]['step'] = 'ask_home_state'
            return jsonify({'response': 'Hello! Please enter your home state to know about the scholarships available.'})
        else:
            return jsonify({'response': 'Please greet me first by saying "hello", "hi", or "hey".'})

    # Ask for the user's home state
    if user_state[user_id]['step'] == 'ask_home_state':
        # Normalize the input to match state keys
        state = user_message.title()
        if state in scholarship_data:
            user_state[user_id]['home_state'] = state
            user_state[user_id]['step'] = 'home_state_details'
            response = f"Here are the scholarships available in {state}: " + ", ".join(scholarship_data[state]['scholarships'])
            response += "<br>Would you like to know about eligibility, application procedure, required documents, or application dates?"
            return jsonify({'response': response})
        else:
            return jsonify({'response': 'Sorry, I don’t have information about that state. Please provide a different home state.'})

    # Provide home state scholarship details
    if user_state[user_id]['step'] == 'home_state_details':
        state = user_state[user_id]['home_state']
        if 'eligibility' in user_message:
            return jsonify({'response': f"Eligibility: {scholarship_data[state]['eligibility']}"})
        elif 'application procedure' in user_message or 'process' in user_message:
            return jsonify({'response': f"Application Procedure: {scholarship_data[state]['application_procedure']}"})
        elif 'documents' in user_message:
            return jsonify({'response': 'Required Documents: ' + ', '.join(scholarship_data[state]['documents'])})
        elif 'dates' in user_message or 'start' in user_message or 'end' in user_message:
            return jsonify({'response': f"Application Dates: {scholarship_data[state]['application_dates']}"})
        else:
            return jsonify({'response': 'Please ask about eligibility, application procedure, required documents, or dates.'})

    # Handle other queries or unrecognized inputs
    return jsonify({'response': "Sorry, I didn't understand your query. Please try again with questions about eligibility, application procedure, required documents, or application dates."})


@app.route('/scholarship_form.html')
def other_state():
    return render_template('scholarship_form.html')


@app.route('/scholarship', methods=['GET', 'POST'])
def scholarship_form():
    if request.method == 'POST':
        # Get form data
        form_data = {
            # Student Name
            'fullname': request.form['fullname'],
            # Date of Birth
            'dob': request.form['date'],
            'gender': request.form['gender'],                      # Gender
            # Contact Number
            'contact': request.form['contactNumber'],
            'address': request.form['address'],                    # Address
            # Caste Education Institute
            'name_of_institute': request.form.get('institution'),
            'course': request.form['course'],                      # Course
            'year_of_study': request.form['year'],        # Year for Study
            # Scholarship Applying For
            'scholorship_applying_for': request.form['scholarship'],
            # State of Domicile
            'state': request.form['state'],
            # Nationality
            'nationality': request.form['nationality'],
            'caste_certificate': request.form['caste'],  # Caste Certificate
            'aadhar_card': request.form['aadhar'],            # Aadhar Card
            'income_certificate': request.form['income'],  # Income Certificate
            # Domicile Certificate
            'domicile_certificate': request.form['domicile'],
        }

        # Pass form data to the certificate page
        # return redirect(url_for('certificate.', **form_data))
        try:
            return redirect(url_for('certificate',**form_data))
        except Exception as e:
            print(f"Error: {e}")
            return "An error occurred", 500


    return render_template('scholarship_form.html')

# Route for the scholarship eligibility certificate


@app.route('/certificate.html')
def certificate():
    # Retrieve data passed from the form
    return render_template('certificate.html', data=request.args)



if __name__ == '__main__':
    app.run(debug=True)
