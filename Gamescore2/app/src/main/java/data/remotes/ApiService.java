package data.remotes;

import com.example.gamescore2.SignIn;

import data.models.LogRequest;
import data.models.Login;
import data.models.LoginRequest;
import data.models.LoginResponse;
import retrofit2.Call;
import retrofit2.Response;
import retrofit2.http.Body;
import retrofit2.http.Headers;
import retrofit2.http.POST;

public interface ApiService {

//    @POST("/login")
//    @Headers({"Accept: application/json"})
//    Call<Login> sendLogin(@Body LoginRequest loginRequest);

    @POST("/login")
    @Headers({"Content-Type: application/json"})
    Call<String> postJson(@Body String logRequest);

}
