package data.models;
import android.media.session.MediaSession;
import android.util.Log;

import com.google.gson.annotations.Expose;
import com.google.gson.annotations.SerializedName;

public class LoginRequest {



    private String password;
    private String e_mail;

    public LoginRequest(String password, String e_mail){


        this.password = password;
        this.e_mail = e_mail;

    }

}

