package com.example.gamescore2;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.util.ArrayMap;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

import com.example.gamescore2.Dialogs.EmailMatchDialog;
import com.example.gamescore2.Dialogs.FillFormDialog;
import com.example.gamescore2.Dialogs.LengthDialog;
import com.example.gamescore2.Dialogs.PasswordMatchDialog;

import org.json.JSONObject;

import java.util.Map;

import data.remotes.ApiService;
import data.remotes.ApiUtils;
import okhttp3.RequestBody;
import okhttp3.ResponseBody;
import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;

public class Register extends AppCompatActivity implements View.OnClickListener{

    private static final String TAG = "";
    private ApiService mApiService;
    EditText username, email, confirmEmail, password, confirmPassword;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_register);

        Button register = findViewById(R.id.registerButton);
        register.setOnClickListener(this);

        mApiService = ApiUtils.getApiService();
        username = findViewById(R.id.usernameRegister);
        email = findViewById(R.id.emailRegister);
        confirmEmail = findViewById(R.id.confirmEmail);
        password = findViewById(R.id.passwordRegister);
        confirmPassword = findViewById(R.id.confirmPassword);

    }

    @Override
    public void onClick(View v) {

        Log.d("test", "clicked");

        username = findViewById(R.id.usernameRegister);
        email = findViewById(R.id.emailRegister);
        confirmEmail = findViewById(R.id.confirmEmail);
        password = findViewById(R.id.passwordRegister);
        confirmPassword = findViewById(R.id.confirmPassword);

        if (!email.getText().toString().equals(confirmEmail.getText().toString())){
            //email.getText().clear();
            confirmEmail.getText().clear();
            EmailMatchDialog emailMatchDialog = new EmailMatchDialog();
            emailMatchDialog.show(getSupportFragmentManager(),"dialog email do not match");


        }
        else if(username.getText().toString().equals("") || email.getText().toString().equals("") || password.getText().toString().equals("") || confirmPassword.getText().toString().equals("") || confirmEmail.getText().toString().equals("") ||!email.getText().toString().contains("@")){
            FillFormDialog fillFormDialog = new FillFormDialog();
            fillFormDialog.show(getSupportFragmentManager(), "empty form");

            Log.d("test","fill in form");

        }
        else if (!password.getText().toString().equals(confirmPassword.getText().toString())){
            confirmPassword.getText().clear();
            password.getText().clear();
            PasswordMatchDialog passwordMatchDialog = new PasswordMatchDialog();
            passwordMatchDialog.show(getSupportFragmentManager(),"dialog password do not match");
        }
        else if(username.getText().toString().length() < 3 || password.getText().toString().length() < 3){
            confirmPassword.getText().clear();
            password.getText().clear();
            LengthDialog lengthDialog = new LengthDialog();
            lengthDialog.show(getSupportFragmentManager(), "dialog length to short");
        }
        else if(email.getText().toString().equals(confirmEmail.getText().toString())&& password.getText().toString().equals(confirmPassword.getText().toString())) {
            sendRegister(email.getText().toString(), password.getText().toString(), username.getText().toString());
            Intent intent = new Intent(this,SignIn.class);
            startActivity(intent);


    }
}

    private void sendRegister(String mEmail, String mPassword, String mUsername) {

        Map<String, Object> jsonParams = new ArrayMap<>();
        jsonParams.put("password", mPassword);
        jsonParams.put("e_mail", mEmail);
        jsonParams.put("username", mUsername);

        RequestBody body = RequestBody.create(okhttp3.MediaType.parse("application/json; charset=utf-8"),(new JSONObject(jsonParams)).toString());

        Call<ResponseBody> response = mApiService.sendRegister(body);

        response.enqueue(new Callback<ResponseBody>() {
            @Override
            public void onResponse(Call<ResponseBody> call, Response<ResponseBody> response) {
                if(response.isSuccessful()) {

                    Log.d("test", "klappt jetzt");
                } else {
                    Log.d("test", "klappt nicht");

                }

            }

            @Override
            public void onFailure(Call<ResponseBody> call, Throwable t) {
                System.out.println("Exception: " + t);
                Log.e(TAG, "Unable to submit login to API.");
            }

        });
    }}


