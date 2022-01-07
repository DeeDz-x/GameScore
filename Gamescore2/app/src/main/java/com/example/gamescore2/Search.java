package com.example.gamescore2;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

public class Search extends AppCompatActivity implements View.OnClickListener{

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_search);

        //Button rating = findViewById(R.id.ratingButtonSearch);
        Button search = findViewById(R.id.startButtonSearch);

        //rating.setOnClickListener(this);
        search.setOnClickListener(this);
    }

    @Override
    public void onClick(View v) {
        switch (v.getId()){
            case R.id.startButtonSearch:
                Intent intent = new Intent(this, GameProfil.class);
                startActivity(intent);
                break;


        }

    }
}