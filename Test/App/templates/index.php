<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <title>Home</title>
</head>
<body>
<form method="POST">
    {% csrf_token %}
    <table align="center">
        <tr>
            <td>
                <label for="{{ form.name.html_name }}">{{ form.name.label }}</label>
            </td>
            <td>{{ form.name }}<span style="color: red">{{ form.name.errors }}</span></td>
        </tr>
        <tr>
            <td>
                <label for="{{ form.email.html_name }}">{{ form.email.label }}</label>
            </td>
            <td>{{ form.email }}<span style="color: red">{{ form.email.errors }}</span></td>
        </tr>
        <tr>
            <td></td>
            <td><button type="submit">Submit</button></td>
        </tr>
        <tr>
            <td></td>
            <td style="color: green">
            {% for message in messages %}
                {{ message }}
            {% endfor %}
            </td>
        </tr>
    </table>
</form>
<?php echo "Hello from PHP!";?>
</body>
</html>