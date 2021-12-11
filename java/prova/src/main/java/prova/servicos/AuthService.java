package prova.servicos;

import java.util.List;

import prova.firebase.MyFirebaseServiceImpl;

public class AuthService implements IAuthService {
	
	MyFirebaseServiceImpl fb = new MyFirebaseServiceImpl();
	
	@Override
	public boolean createUser(String email, String password) {
		return fb.createUser(email, password);
	}
	
	@Override
	public boolean login(String email, String password, List<String> tokens) {
		return fb.login(email, password, tokens);
	}
	
	@Override
	public void logout(String token, List<String> tokens) {
		tokens.remove(token);
		
	}

}
