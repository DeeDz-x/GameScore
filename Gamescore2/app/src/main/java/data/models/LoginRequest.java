package data.models;
import android.media.session.MediaSession;
import com.google.gson.annotations.Expose;
import com.google.gson.annotations.SerializedName;

public class LoginRequest {

    @SerializedName("e_mail")
    @Expose
    private String email;
    @SerializedName("password")
    @Expose
    private String password;

    public LoginRequest(String email, String password){
        this.email = email;
        this.password = password;
    }

}

