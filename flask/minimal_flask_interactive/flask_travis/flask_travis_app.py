from flask import Flask, request

app = Flask(__name__)
print("app initiated. name is :", __name__)

class Travis(object):

    def __init__(self):
        self.r_customer_check = False
        self.n_customer_check = False

# adds bootstrap support
def render_template_mini(html_to_be_wrapped, prettify=True):
    html_out = """
    <link rel="stylesheet" media="screen" href="https://maxcdn.bootstrapcdn.com/bootswatch/4.0.0-beta.3/flatly/bootstrap.min.css">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    """

    if prettify:
        # prettify input boxes. html_to_be_wrapped has to be a html-formatted string
        pretty_formatting_input = 'type="text" class="form-control mr-sm-2" placeholder="input text"'
        if 'type="text"' in html_to_be_wrapped:
            # split all instances
            temp_list = html_to_be_wrapped.split('type="text"')
            # and glue them all together again with formatting added
            html_to_be_wrapped = pretty_formatting_input.join(temp_list)

        # prettify submit button.
        pretty_formatting_btn = 'type="submit" class="btn btn-secondary my-2 my-sm-0"'
        if 'type="submit"' in html_to_be_wrapped and 'class="btn' not in html_to_be_wrapped:
            # check if the butotn already has a format
            temp_list = html_to_be_wrapped.split('type="submit"')
            html_to_be_wrapped = pretty_formatting_btn.join(temp_list)
        #'<button class="btn btn-secondary my-2 my-sm-0" type="submit">Search</button>'

        # prettify forms
        pretty_formatting_form = '<form class="form-inline my-2 my-lg-0 mx-auto"'
        if '<form' in html_to_be_wrapped:
            temp_list = html_to_be_wrapped.split('<form')
            html_to_be_wrapped = pretty_formatting_form.join(temp_list)

        html_out += """
        <div class="jumbotron" style="background-color:#F9F9F9">
        <div class="container" style="background-color:#F1F1F1;border-radius:5px;display:flex;align-items:center;padding:5%">
            {0}
        </div>
        </div>
        """.format(html_to_be_wrapped)

    else:
        html_out += '<div class="jumbotron">' + html_to_be_wrapped + '</div>'

    #print('final html: \n', html_out)
    return html_out

# turns a list from python into html formatting for use with <ul></ul> or <ol></ol>
def format_list_html(namelist_in):
    namelist_in = ['<li>' + name + '</li>\n' for name in namelist_in]
    return ''.join(namelist_in)


# travis is not running & isn't initiated as of yet
travis = None
name_counter = 0
new_customer = None
returning_customer = None
namelist = [
    'travis',
    'john',
    'jacob',
    'jingleheimer',
    'smith'
]


@app.route('/', methods=['GET', 'POST'])
def travis_web():
    # all the global variables are persistent variables (data and changes are maintained)
    global name_counter, namelist, travis, returning_customer, new_customer
    if not travis:
        print('initializing travis!')
        travis = Travis()  # only make a travis instance when travis_web is called

    def default_response():
        html_out = render_template_mini(
            """
            <div>
                <h1>hello, i am Travis the robot. what is your name?</h1>
                <form method="POST">
                    <input type="text" name="text">
                    <button type="submit">Submit</button>
                </form> 
            </div>
            """
        )
        return html_out


    # do the following only if the request has extra
    # POST data (if you typed something before)
    if request.method == 'POST':
        # check for the reset button first
        try:
            check_for_retry = request.form['retry']
            print('retry found!', check_for_retry)
            if 'reset' in check_for_retry:
                return default_response()
        except:
            pass

        print(request.form)
        check_for_inputs = request.form['text']
        check_for_inputs = check_for_inputs.split(' ')
        print(check_for_inputs)



        result = check_for_inputs  # no reason, just nice to change names sometimes
        if travis.r_customer_check == False and travis.n_customer_check == False:
            for input_name in result:
                if input_name in namelist:
                    returning_customer = input_name
                    name_counter += 1
                    travis.r_customer_check = True
                    html_out = render_template_mini("""
                            <div>
                                <h1>welcome back, {0}!</h1>
                                <h2>do you want to delete your name from the list?</h2>
                                <form method='POST'>
                                    <input type="text" name="text">
                                    <button type="submit">Submit</button>
                                </form> 
                            </div>
                            """.format(returning_customer))
                    return html_out
                else:
                    new_customer = input_name
                    travis.n_customer_check = True
                    html_out = render_template_mini("""
                            <div>
                                <h1>hmm...</h1>
                                <h2>you are not on the list, {0}.</h2>
                                <h2>do you want me to add you to the list?</h2>
                                <form method='POST'>
                                    <input type="text" name="text">
                                    <button type="submit">Submit</button>
                                </form>
                            </div> 
                            """.format(new_customer))
                    return html_out

        for received_input in check_for_inputs:
            if travis.r_customer_check:
                travis.r_customer_check = False # reset checking token
                if received_input.lower() == 'yes':
                    # delete customer from namelist
                    if returning_customer in namelist:
                        namelist.remove(returning_customer)
                    html_out = render_template_mini("""
                    <div>
                        <h2>sad to see you go man/woman/squirrel.</h2>
                        <p>vaunted list of members:</p>
                        <ul>{0}</ul>
                        <p style='color:grey'>you are a squirrel are you not?</p>
                        <form method="POST">
                            <button name="retry" value="reset" type="submit" class="btn btn-warning">retry</button>
                        </form>
                    </div>
                    """.format(format_list_html(namelist)))
                    return html_out
                else:
                    html_out = render_template_mini("""
                    <div>
                        <h2 style='color: rgb(200,200,200)'>phew... felt like i just dodged a bullet.</h2>
                        <p>vaunted list of members:</p>
                        <ul>{0}</ul>
                        <form method="POST">
                            <button name="retry" value="reset" type="submit" class="btn btn-warning">retry</button>
                        </form>
                    </div>
                    """.format(format_list_html(namelist)))
                    return html_out

            if travis.n_customer_check:
                travis.n_customer_check = False # reset checking token
                if received_input.lower() == 'yes':
                    namelist.append(new_customer)
                    html_out = render_template_mini("""
                    <div>
                    <h2>ok, welcome to the family!</h2>
                    <p>vaunted list of members:</p>
                    <ul>{0}</ul>
                    <form method="POST">
                        <button name="retry" value="reset" type="submit" class="btn btn-warning">retry</button>
                    </form>
                    </div>
                    """.format(format_list_html(namelist)))
                    return html_out
                else:
                    html_out = render_template_mini("""
                    <div>
                    <h2>boo boo! go find someone else to be your family!</h2>
                    <p>vaunted list of members:</p>
                    <ul>{0}</ul>
                    <form method="POST">
                        <button name="retry" value="reset" type="submit" class="btn btn-warning">retry</button>
                    </form>
                    </div>
                    """.format(format_list_html(namelist)))
                    return html_out

    # do this when first loading the page (when there is no POST input from the html
    else:
        return default_response()


@app.route('/original/')
def travis_local():
    result = input("hello, i am Travis the robot. what is your name? ")
    result = result.split(' ')

    jjjs_counter = 0
    for name in result:
        if name in namelist:
            if 'john' or 'jacob' or 'jingleheimer' or 'smith' in name:
                jjjs_counter += 1
            print("welcome back!, {0}".format(name))
            returning_customer = input('do you want to delete your name from the list?')
            if 'yes' in returning_customer.lower():
                namelist.remove(name)
                print('sad to see you go man/woman/squirrel.')
            if jjjs_counter == 4:
                print('john jacob jingleheimer smith, his name was my name too~')
        else:
            new_customer = input('you are not on the list, {0}. do you want me to add you to the list?'.format(name))
            if 'yes' in new_customer.lower():
                print('ok, welcome to the family!')
                namelist.append(name)
            elif 'no' in new_customer.lower():
                print('boo boo!')
            else:
                print("you're not making any sense to me. speak english, or check my code.")

    print('this is the final list.')
    print(namelist)
    rerun = input('do you wanna try again?')
    if 'yes' in rerun.lower():
        travis()
    else:
        print('sound of scary robot sounds powering down with a whirr')


# make the program run
if __name__ == '__main__':
    app.run(debug=True, port=8000)