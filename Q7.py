def access_control(authorized_user_id):
    def secure_function(user_id,*args,**kwargs):
        if user_id==authorized_user_id:
            return "Access granted.Logic executed."
        else:
            return "Unauthorized"
        
    return secure_function

secure_function=access_control("13579")

print(secure_function("13579"))
print(secure_function("97531"))
