package prova.firebase;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
@AllArgsConstructor
public class FBResponse {
	
	private String email;
	private String idToken;
	private String refreshToken;
	private String expiresIn;
	private String localId;
	private boolean registered;
	
}
