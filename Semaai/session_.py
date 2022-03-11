response_session_id = "888f92431f580009282f0da82fdd4f140bbb2752"
x = """frontend_lang=en_US; visitor_uuid=53121f4b2e384028974a862f59cd3513; tz=Asia/Calcutta; im_livechat_history=["/en","/en/web/login"]; session_id=736f92431f580009282f0da82fdd4f140bbb2752"""
sessions_ = x.split(" ")
sessions_[-1] = "session_id="+str(response_session_id)

print(" ".join(sessions_))