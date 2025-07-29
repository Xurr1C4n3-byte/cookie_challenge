from flask import Flask, request, redirect, make_response, render_template_string

app = Flask(__name__)
app.secret_key = 'super_secret_ctf_key_123!'

LOGIN_HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Cookie Monster</title>
</head>
<body>
    <h1>Please log in to eat admin cookie 🍪</h1>
    {% if message %}
        <p style="color: red;">{{ message }}</p>
    {% endif %}
    <form method="POST">
        <label>Username:</label>
        <input type="text" name="username"><br>
        <label>Password:</label>
        <input type="password" name="password"><br>
        <button type="submit">Login</button>
    </form>
</body>
</html>
"""

STORY_HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Not Admin</title>
</head>
<body>
    <h2>I am not Admin but I can tell you a good story...</h2>
    <p style="font-size:25px;margin:10px; word-spacing:10px;text-align:justify;letter-spacing:1px">
        Once upon a time, there were four youths studying under the famous professor Disaparmauk of Taxila. They all came of rich families from different lands.  Each followed his natural bent and specialized in different branches of study. One studied music and dancing; another studied medicine; another studied astrology; and the fourth, philosophy.


           After studying for three years they were considered proficient in their respective subject, and the time came to say good-bye to their professor and return to their respective parents. As a parting gift the professor gave them a cooking pot, as well as some grain, in order that they would have something to cook and eat should their dry rations runs out before they reached home.

          Then, as his final gift to his students, the professor gave them a piece of advice. "Remember," he said to them," the four of you may be proficient, each in your own subject, but if you don't have the sense to act suitably to the time and circumstance of situation, you may have to go hungry."

Not quite comprehending what the great teacher meant, they looked at one another, but said nothing, and great teacher meant, they looked at one another, but said nothing, and after paying their respects to their professor, set forth on their journey home.


             After travelling for a number of days their dry rations ran out and the pot and the grain given to them by their professor came in very useful indeed. "How thoughtful our great teacher is!" they felt and got down to the business of cooking themselves a meal. There was rice enough for all four of them all right, but they would have to do something about the curry. So they drew lots for the different tasks to be carried out in order to get a decent meal.

             Thus, the man of music and dancing was to cook the rice. The medico was to buy meat and fish; the astrologer was to gather vegetables; and the philosopher was to get some ghee (which is clarified butter) to cook the curry in. And they each set out to do his task.

            The medico went to the nearest village and there in the bazaar he found various kinds of meat and fish. He looked around for some time and found that nothing suited him. His medical knowledge now seemed to warn him which meat or fish was indigestible, which not nutritious, which unseasonable, which would cause what disease, which would upset the stomach and which the bile, till finally he left without buying any meat or fish!


           The philosopher, however, got the required ghee, which he packed in a green leaf, and retraced his steps. On the way he soon became lost in philosophical speculations. "Ghee," he said to himself, "comes from cow's milk. Cow eats grass, and yes, leaves, too. Ah then, in a way, ghee comes from cow's milk, and cow's milk comes from leaves, and so the ghee and the leaf are related!"On and on he philosophized, quite happily unaware of the ghee in the leaf in his hand melting gradually and dripping.

            By the time he met the medico, who was coming back empty-handed from the village market, there was nothing left of the ghee he had bought!  He, too, was now empty-handed. The two of them looked at each other, not knowing whether to smile or weep and each recounted to the other what had happened to him, as they walked back to where the man of music and dancing was supposed to be cooking the rice. But there, to their horror, they found their friend looking as disconsolate as ever, moping beside a broken pot with the rice strewn all over the fire-place.


           "Soon after the three of you left," wailed the cook,"  I built a fire, rinsed the rice, put it in the pot, added the required amount of water, and placed the pot on the fire. After some time, the pot began to simmer, and then it started to boil. I watched and could not help but hear the bubbling noise of the boiling rice. To my ears, it sounded so much like the rhythmic beats of music coming from a drum that I started dancing to it. And, … and …"


             "And what happened?" asked his two friends. " And," continued the cook," one backward kick of my right heel caught the pot. And there, as you can see, is the end of our rice!"
The other two, who had come back empty-handed, now found it quite easy to admit to the cook that they, too, had failed to accomplish what they had set out to do. Suddenly, they remembered their astrologer friend, who was to get some vegetables. Off they went to look for him in the forest, and there atop a tall bael tree was their friend, sitting tight.

             Before they could say anything, the astrologer called out to them. "Hey, I've got all the tender bael leaves that should go well with our meal. See!" he said, holding up the leaves he had plucked.
"Then why are you still there astride that branch? What are you staying on there for?"  <a href="/4dm1nAdmin" hidden>Go to Admin Page</a>

"Ah," replied the astrologer, "the climbing up was easy because at that moment I was under the influence of an ascending constellation. But now, the climbing down is quite a different matter. You see, the stars are not just right as yet and I am waiting for the moment when I'll be under the influence of a descending constellation."

               "Oh, to hell with your stars and constellations!" the three on the ground yelled, almost in unison. "Just come you down!"


             The poor astrologer was frightened out of his wits. He started to climb down slowly, shakily. But he was trembling so much that he half-slipped and half-fell, and lay in a stunned heap on the ground. His three friends lifted him up and all he had were bruises and cuts. No tender bael leaves!

             Now with no meal in sight, each began to realize how and why he had failed in carrying out his lot. Then, slowly, the wisdom of the parting advice given to them by their great teacher dawned upon them.
"Remember, the four of you may be proficient, each in your own subject, but if you don't have the sense to act suitably to the time and circumstance of a situation, you may have to go hungry."     
    </p>
</body>
</html>
"""

ROBOT_HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Robot</title>
    <style>
        body {
            background: url('https://example.com/robot.jpg') no-repeat center center;
            background-size: cover;
            text-align: center;
            padding-top: 20%;
        }
    </style>
</head>
<body>
    <h1>Oh, I am not Admin again. I am just the robot following admin🤖</h1>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def login():
    # Check cookie first for both GET and POST
    if request.cookies.get('admin') == '1000':
        return redirect('/story')
        
    if request.method == 'POST':
        username = request.form.get('username', '')
        password = request.form.get('password', '')
        
        if username and password:  # If both fields are filled
            resp = make_response(render_template_string(LOGIN_HTML, 
                   message="Do you think I will use admin:1000?"))
            resp.set_cookie('user', 'guest')
            return resp
    
    return render_template_string(LOGIN_HTML)

@app.route('/story')
def story():
    if request.cookies.get('admin') != '1000':
        return redirect('/')
    return render_template_string(STORY_HTML)


@app.route('/4dm1nAdmin')
def robot():
    return render_template_string(ROBOT_HTML)


@app.route('/4dm1nAdmin/robots.txt')
def robots_txt():
    # Flag is hidden here
    resp = make_response("User-agent: *\nDisallow: *\n\nINFOSEC{r0b07_1n5p3c7_c00k13}")
    resp.headers['Content-Type'] = 'text/plain'
    return resp


if __name__ == '__main__':
    app.run(debug=True, port=8000)
