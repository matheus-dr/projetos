package prova.firebase;

import java.util.List;

import org.springframework.web.client.RestTemplate;

public abstract class MyFirebaseService {
	
	protected String signUpUrl =  "https://identitytoolkit.googleapis.com/v1/accounts:signUp?key=AIzaSyARgY_59EJG7sTVG1FbcheASa_8N3l8x2s";
	protected String signInUrl =  "https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key=AIzaSyARgY_59EJG7sTVG1FbcheASa_8N3l8x2s";
	protected RestTemplate restTemplate = new RestTemplate();
	
	public abstract boolean createUser(String email, String password);
	public abstract boolean login(String email, String password, List<String> tokens);

}
