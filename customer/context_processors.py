from customer.forms import LoginForm, SignUpForm


def message_processor(request,*args,**kwargs):
    hasSignUp = False
    User = {"role":""}
    background = "background1"
    path = str(request.path[1:])
    if path.startswith("customer"):
        User["role"]="customer"
        hasSignUp = True
    elif path.startswith("admins"):
        User["role"]="admins"
        hasSignUp = True
        background = "background"
    elif path.startswith("manager"):
        User["role"]="manager"
        hasSignUp = True
        background="background"
    elif path.startswith("employee"):
        User["role"]="employee"
        hasSignUp = True
        background = "background"
        
    return {"background":background,"hasSignedIn":hasSignUp,"User":User,
            'signup_form':SignUpForm(),'login_form':LoginForm()}