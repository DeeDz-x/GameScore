package data.remotes;



import okhttp3.RequestBody;
import okhttp3.ResponseBody;
import retrofit2.Call;
import retrofit2.http.Body;
import retrofit2.http.POST;

public interface ApiService {



    @POST("/login")
    Call<ResponseBody> sendLogin(@Body RequestBody loginRequest);

    @POST("/register")
    Call<ResponseBody> sendRegister(@Body RequestBody registerRequest);

}
