package data.remotes;

public class ApiUtils {

    private ApiUtils(){}

    public static final String BASE_URL =  "http://127.0.0.1:5000/";


    public static ApiService getApiService(){

        return RetrofitClient.getClient(BASE_URL).create(ApiService.class);

    }
}
