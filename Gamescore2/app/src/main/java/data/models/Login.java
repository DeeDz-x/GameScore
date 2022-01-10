package data.models;


public class Login {


    private String key;

    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }

    @Override
    public String toString() {
        return "Login{" +
                "key='" + key + "'" +
        '}';
    }
}
