package data.remotes;

import android.util.Log;

import com.example.gamescore2.SignIn;

import data.models.Login;
import data.models.LoginRequest;

import okhttp3.RequestBody;
import okhttp3.ResponseBody;
import retrofit2.Call;
import retrofit2.Response;
import retrofit2.http.Body;
import retrofit2.http.Field;
import retrofit2.http.FormUrlEncoded;
import retrofit2.http.Header;
import retrofit2.http.Headers;
import retrofit2.http.POST;

public interface ApiService {

//    @POST("/login")
//    @Headers({"Accept: application/json"})
//    Call<Login> sendLogin(@Body LoginRequest loginRequest);

    @POST("/login")
    Call<ResponseBody> sendLogin(@Body RequestBody loginRequest);

    @POST("/register")
    Call<ResponseBody> sendRegister(@Body RequestBody registerRequest);

    @POST("/logout")
    Call<Void> sendLogout(@Header("Authorization") String token);

}
