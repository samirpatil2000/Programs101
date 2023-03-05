curl --location --request POST 'http://localhost:8080/customers/101/delivery-addresses' \
--header 'Content-Type: application/json;charset=UTF-8' \
--header 'Cookie: session_id=71e04592fde4b64392fa0bbdb5b99c42033e9287; visitor_uuid=03c1a90388114f90a99094760b2f5801' \
--form 'full_name="Samir Patil"' \
--form 'full_address="At.OSar"' \
--form 'zip_code="401503"' \
--form 'city="Mumbai"' \
--form 'state="Maharahstra"' \
--form 'country="India"'