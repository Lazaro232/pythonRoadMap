from food import Food
from flask import Flask, render_template, request, url_for, redirect


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/result/<food_name>/<int:amount_to_craft>/<int:tax_fee>/<focus>',
           methods=['GET', 'POST'])
def meal(food_name, amount_to_craft, tax_fee, focus):
    user_info = [amount_to_craft, tax_fee, focus]
    food = Food()
    food_type, tier = food_name.split("_")  # ['stew', 't4']
    _, tier_number = tier.split("t")  # ['', '4']
    food_type_title = food_type.title()  # 'Stew'

    food_str = 'Tier ' + tier_number + ' ' + food_type_title

    food_dict = food.all_foods(user_info, food_name)
    return render_template('food_result.html',
                           food=food_dict,
                           food_name=food_str)


@app.route('/form/<food_name>', methods=['GET', 'POST'])
def form(food_name):
    if request.method == 'POST':
        amount_to_craft = request.form.get('quantity')
        tax_fee = request.form.get('tax')
        focus = request.form.get('focus')
        if focus:
            focus = 1
        else:
            focus = 0
        return redirect(url_for('meal',
                                food_name=food_name,
                                amount_to_craft=amount_to_craft,
                                tax_fee=tax_fee,
                                focus=focus))
    return render_template('craft_info.html')


if __name__ == '__main__':
    app.run(debug=True)
