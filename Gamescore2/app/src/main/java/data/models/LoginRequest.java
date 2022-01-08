package data.models;


public class LoginRequest {



    private String password;
    private String e_mail;

    public LoginRequest(String password, String e_mail){


        this.password = password;
        this.e_mail = e_mail;

    }

}

