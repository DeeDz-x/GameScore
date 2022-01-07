package data.remotes;

import com.example.gamescore2.SignIn;

import data.models.Login;
import data.models.LoginRequest;
import retrofit2.Call;
import retrofit2.http.Body;
import retrofit2.http.POST;

public interface ApiService {

    @POST("/login")
    Call<Login> sendLogin(@Body LoginRequest loginRequest);
}
