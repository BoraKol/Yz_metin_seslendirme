import streamlit as st
from gtts import gTTS
from googletrans import Translator 

## Uygulamaya başlık verelim
st.title('Metin Seslendirme Uygulaması @borakol')

## Kullanıcıdan metin alalım
text_message = st.text_area('Metin giriniz: ')

## dil seçeneğini ayarlayalım
language = st.selectbox('Dil Seçiniz: ' , ['Türkçe' , 'İngilizce' , 'Rusça'])

if st.button('Seslendir'):
    ## metin girilmesi gereken alanın boş olup olmadığını kontrol edelim.   
    if not text_message :
           st.error('Lütfen bir metin giriniz...)
    else :
                           
           ## Dil seçimine göre lang_code ayarlama
           lang_code = {
               'Türkçe' : 'tr' ,
               'İngilizce' : 'en', 
               'Rusça' : 'ru'
           }.get(language,None) 
       
           # seçilen dile göre çeviri yap
           translator = Translator()
  
    if lang_code :

        ## metni istenen dile çevir
        translated_text = translator.translate(text = text_message , dest=lang_code).text

        ## gTTS ile ses kaydetme işlemini yapalım               
        record = gTTS(text = translated_text , lang = lang_code)

        ## mp3 olarak ses dosyasını kaydedelim.
        record.save('text.mp3')

        ## Ses dosyasını oynatalım.
        st.audio('text.mp3')
        st.success('Metin başarıyla "text.mp3" dosyasına kaydedildi. ')


    else:
        st.error("Bir dil seçmelisiniz.")
