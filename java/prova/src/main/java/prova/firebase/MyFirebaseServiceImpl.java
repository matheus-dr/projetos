package prova.firebase;

import java.util.List;

public class MyFirebaseServiceImpl extends MyFirebaseService {

	@Override
	public boolean createUser(String email, String password) {
		FBRequest request = new FBRequest(email, password, true);
		try {
			this.restTemplate.postForEntity(this.signUpUrl, request, FBResponse.class);
			return true;
		} catch (Exception e) {
			e.printStackTrace();
			return false;
		}
	}

	@Override
	public boolean login(String email, String password, List<String> tokens) {
		FBRequest request = new FBRequest(email, password, true);
		try {
			FBResponse response = this.restTemplate.postForEntity(this.signInUrl, request, FBResponse.class).getBody();
			tokens.add(response.getIdToken());
			return true;
		} catch (Exception e) {
			e.printStackTrace();
			return false;
		}
	}

}
