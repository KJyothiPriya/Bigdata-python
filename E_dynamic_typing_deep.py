#Oka dabba undi anuko, daani meeda fee ani sticker vesav.
fee = 45000
#Concept 1 : DYNAMIC INFERENCE - Python eh CID la kanipettadam
#Java / C language lo ela untundi? Neeku dabba kavali ante mundu cheppali "Naku number pette dabba kavali" ani.
# in java int {fee = 45000;} // Nene chepthunna idi int ani

#Python lo ela?

#Nuvvu emi cheppavu. Just fee = 45000 ani pettav. Python vachi dabba lopala chusi 
#"Oh, idi 45000, number la undi, idhi int " ani thane kanipettesindi.
#Daannine Inference antaru.Proof ento? type() function - chepthundhi ye type ani

fee = 45000
print(type(fee)) # Output: <class 'int'> - Chusava, nuvvu cheppakapoina int anukundi

fee_gst = fee * 0.18 # 0.18 ante float
print(type(fee_gst)) # Output: <class 'float'> - int * float = float ani kuda thane kanipettesindi
# Manam  type cheppakapoina Python eh type ni infer chesukovatam valla daanni Dynamic Inference antaru.

#Concept 2: DYNAMIC TYPING - Oke dabba lo emaina pettukovachu
#Java lo ela? Oka number dabba lo number ne pettav. Apple pettalevu. Error ostadi.

# python lo error radhu 
fee = 45000
print(fee, type(fee)) # int

fee = "Forty Five Thousand"
print(fee, type(fee)) # str - Ade dabba, ippudu string ayyindi, error ledu

fee = True
print(fee, type(fee)) # bool - Ippudu bool ayyindi

fee = 45000 # Malli number ayyindi - Deeniki limit ledu
#note: Interview Point: Python lo variable ki type undadu, value ki type untundi. Variable just oka sticker anthe.

#Concept 3: STRONGLY TYPED - Python chala strict, cheating kudaradu
#Strongly Typed language ante - Python:
#Python chala strict. int + str kalapadam ante ventane error isthundhi 
fee = 45000
result = fee + "Eighteen percent gst"
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
# Nenu int ki str ni kalapanu ani error isthundhi 
#Idhe Strong Typing ante. Type ni automatic ga marchadu, ninnu convert cheyamantadu.

#3 ways to convert FEE and GST
fee = 45000

# Way 1: Nenne manual ga convert cheyali (Explicit Conversion)
# int ni str chesi kalapali
message1 = str(fee) + " Eighteen percent gst" # str(45000) = "45000"
print(message1) # 45000 Eighteen percent gst

# Way 2: f-string - Best way (Python eh convert chestadi, kani nuvvu cheppali)
message2 = f"{fee} Eighteen percent gst"
print(message2)

# Way 3: Correct calculation tho
gst = fee * 0.18
total = fee + gst
message3 = f"Fee is {fee}, GST 18% is {gst}, Total is {total}"
#message3 = "Fee is " + str(fee) + ", GST 18% is " + str(gst) + ", Total is " + str(total) ila kuda rayachu
print(message3) # Fee is 45000, GST 18% is 8100.0, Total is 53100.0
