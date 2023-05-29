samir = {
  "version": '1',
  "region": 'eu-west-1',
  "userPoolId": 'eu-west-1_l92QFzuf2',
  "userName": 'f29d98f3-b0ca-41a4-aaed-8b1a7c68239a',
  "callerContext": {
    "awsSdkVersion": 'aws-sdk-unknown-unknown',
    "clientId": "2s7o2e6evna9i9tt334vgd55ml"
  },
  "triggerSource": 'VerifyAuthChallengeResponse_Authentication',
  "request": {
    "userAttributes": {
      "sub": "f29d98f3-b0ca-41a4-aaed-8b1a7c68239a",
      "cognito:user_status": "FORCE_CHANGE_PASSWORD",
      "phone_number_verified": "true",
      "phone_number": "+918077649429"
    },
    "privateChallengeParameters": { "secretLoginCode": '9629' },
    "challengeAnswer": '9629'
  },
  "response": { "answerCorrect": None }
}
import json
print(json.dumps(samir))


