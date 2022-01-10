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
import retrofit2.http.GET;
import retrofit2.http.Header;
import retrofit2.http.Headers;
import retrofit2.http.POST;
import retrofit2.http.PUT;

public interface ApiService {

    @POST("/login")
    Call<ResponseBody> sendLogin(@Body RequestBody loginRequest);

    @POST("/register")
    Call<ResponseBody> sendRegister(@Body RequestBody registerRequest);

    @POST("/logout")
    Call<Void> sendLogout(@Header("Authorization") String token);

    @GET("/popular_games")
    Call<ResponseBody> getPopGames();

    @POST("/forgot")
    Call<ResponseBody> forgotPassword(@Header("Authorization") String token);

    @POST("/update_password")
    Call<ResponseBody> updatePassword(@Header("Authorization") String token, @Body RequestBody password);

    @GET("/new_games")
    Call<ResponseBody> getNewGames();

    @GET("/games")
    Call<ResponseBody> getGames();

    @GET("/genre")
    Call<ResponseBody> getGenre();

    @GET("/publisher")
    Call<ResponseBody> getPublisher();

    @GET("/user")
    Call<ResponseBody> getOwnProfile(@Header("Authorization") String token);

    @PUT("/user")
    Call<ResponseBody> updateOwnProfile(@Header("Authorization") String token, @Body RequestBody updatedProfile);

    @PUT("/list")
    Call<ResponseBody> createList (@Header("Authorization") String token, @Body RequestBody listName);

    @PUT("/review")
    Call<ResponseBody> createReview (@Header("Authorization") String token, @Body RequestBody reviewBody);

    @GET("/time_played")
    Call<ResponseBody> getTime(@Header("Authorization") String token);

}
