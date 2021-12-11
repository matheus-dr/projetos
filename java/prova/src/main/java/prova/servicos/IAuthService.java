package prova.servicos;

import java.util.List;

public interface IAuthService {
	
	boolean createUser(String email, String password);
	boolean login(String email, String password, List<String> tokens);
	void logout(String token, List<String> tokens);

}
