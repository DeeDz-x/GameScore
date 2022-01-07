package com.example.gamescore2;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;

public class WriteReview extends AppCompatActivity implements View.OnClickListener{

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_write_review);
    }

    @Override
    public void onClick(View v) {
        switch (v.getId()){
            case R.id.cancelButtonWriteReview:
                Intent i = new Intent(this, Landingpage.class);
                startActivity(i);
                break;
            case R.id.confirmButtonWriteReview:
                Intent j = new Intent(this, Lists.class);
                startActivity(j);
                break;

        }

    }
}